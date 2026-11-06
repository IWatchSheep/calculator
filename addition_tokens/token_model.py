"""Token data model, AST, parser, and semantic binder for addition_tokens.

Features:
- Deterministic mathematical template validator and parser for pasted addition expressions.
- Named, typed placeholder slots (TemplateSlot) keeping structure separate from runtime values.
- Persisted custom templates with optional saving (MathTemplateManager).
- Row types: ADDEND, LABEL, and non-executable ALGEBRA_STEP placeholder.
- Three representations of each addend (ordered subcolumns, parsed mathematical structure, aggregated results).
- Strict validation, unit identity preservation, and safe error reporting.
"""

from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from enum import Enum, auto
import json
from pathlib import Path
import re
import sys
from typing import Dict, List, Optional, Set, Tuple

# Ensure calculator_core and addition_chat are importable
_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from calculator_core.expression import evaluate_addition
from addition_chat.addition import WordSummerChatbot


def is_valid_number(s: str) -> bool:
    """Accurately validate a finite decimal or integer string."""
    if not isinstance(s, str):
        return False
    clean = s.strip()
    if not clean:
        return False
    if not re.fullmatch(r"^(?:\d+(?:\.\d*)?|\.\d+)$", clean):
        return False
    try:
        Decimal(clean)
        return True
    except (InvalidOperation, ValueError):
        return False


class TokenType(Enum):
    GROUP_OPEN = auto()   # "("
    GROUP_CLOSE = auto()  # ")"
    OPERATOR = auto()     # "+" (subtraction reserved for next stage)
    NUMBER = auto()       # "1", "2.5", etc.
    ITEM = auto()         # "pen", "pens", "apple", etc.
    CONTEXT = auto()      # "in the drawer", "on the desk", etc.

    @classmethod
    def from_str(cls, name: str) -> "TokenType":
        mapping = {
            "group_open": cls.GROUP_OPEN,
            "(": cls.GROUP_OPEN,
            "group_close": cls.GROUP_CLOSE,
            ")": cls.GROUP_CLOSE,
            "operator": cls.OPERATOR,
            "+": cls.OPERATOR,
            "number": cls.NUMBER,
            "quantity": cls.NUMBER,
            "item": cls.ITEM,
            "word": cls.ITEM,
            "context": cls.CONTEXT,
            "description": cls.CONTEXT,
        }
        key = name.strip().lower()
        if key in mapping:
            return mapping[key]
        raise ValueError(f"Unknown TokenType: '{name}'")

    @property
    def label(self) -> str:
        labels = {
            TokenType.GROUP_OPEN: "(",
            TokenType.GROUP_CLOSE: ")",
            TokenType.OPERATOR: "+",
            TokenType.NUMBER: "Number",
            TokenType.ITEM: "Item",
            TokenType.CONTEXT: "Context",
        }
        return labels.get(self, self.name)


class RowType(Enum):
    """Distinguishes calculation rows, descriptive rows, and future placeholders."""
    ADDEND = auto()        # Mathematical addend row (Col 1 = Math template, Col 2+ = Descriptions)
    LABEL = auto()         # Descriptive or explanation row (does not contribute numbers)
    ALGEBRA_STEP = auto()  # Future capability placeholder (not allowed to execute in this stage)


# -----------------------------------------------------------------------------
# Mathematical Templates & Named Typed Placeholder Slots
# -----------------------------------------------------------------------------

@dataclass
class SlotMetadata:
    """Metadata defining a named, typed placeholder slot in a template."""
    slot_id: int
    name: str                       # e.g. "term_1", "term_2"
    expected_type: str = "NUMBER"   # Expects a valid finite decimal / integer


@dataclass
class TemplateSlot:
    """An instance of an editable value slot, keeping values separate from structure."""
    slot_id: int
    name: str
    expected_type: str = "NUMBER"
    value: str = ""                 # User-entered quantity (e.g. "1", "2.5")
    bound_unit: str = ""            # Associated item/unit if explicitly bound to slot
    bound_context: str = ""         # Associated context if explicitly bound to slot

    @property
    def is_filled(self) -> bool:
        return bool(self.value.strip())


@dataclass
class MathTemplate:
    """Mathematical structure template with fixed syntax and named, typed slots."""
    template_id: str
    pattern: str                    # e.g. "(□ + □) + □"
    name: str = ""
    slots_meta: List[SlotMetadata] = field(default_factory=list)
    is_custom: bool = False

    def __post_init__(self) -> None:
        if not self.slots_meta:
            count = self.pattern.count("□")
            self.slots_meta = [
                SlotMetadata(slot_id=i, name=f"term_{i + 1}", expected_type="NUMBER")
                for i in range(count)
            ]

    @property
    def slot_count(self) -> int:
        return len(self.slots_meta)

    def create_instance(self, initial_values: Optional[List[str]] = None) -> "TemplateInstance":
        slots = [
            TemplateSlot(
                slot_id=meta.slot_id,
                name=meta.name,
                expected_type=meta.expected_type,
                value=initial_values[idx] if initial_values and idx < len(initial_values) else ""
            )
            for idx, meta in enumerate(self.slots_meta)
        ]
        return TemplateInstance(template=self, slots=slots)


class TemplateValidator:
    """Deterministic mathematical validator for template patterns and pasted expressions."""

    @classmethod
    def validate_addition_pattern(cls, pattern: str) -> None:
        """Validates that a template pattern is structurally sound for addition and parentheses."""
        clean = pattern.strip()
        if not clean:
            raise ValueError("Template pattern cannot be empty")
        if "□" not in clean:
            raise ValueError("Template must contain at least one editable placeholder '□'")

        # Enforce addition and parentheses only in this development stage
        for ch in clean:
            if ch not in ("□", "(", ")", "+", " "):
                raise ValueError(
                    f"Unsupported character '{ch}' in addition template. "
                    f"Only addition '+', parentheses '()', and placeholder '□' are supported."
                )

        # Build dummy expression replacing □ with valid number 1 to test syntax
        dummy_expr = clean.replace("□", " 1 ")
        tokens: List[Token] = []
        raw_parts = re.findall(r"\(|\)|\+|\d+(?:\.\d*)?|\.\d+|[^\s()+\d]+", dummy_expr)
        for part in raw_parts:
            part = part.strip()
            if not part:
                continue
            if part in ("(", ")", "+"):
                tokens.append(Token(value=part))
            elif is_valid_number(part):
                tokens.append(Token(value=part, token_type=TokenType.NUMBER, explicit_type=True))
            else:
                raise ValueError(f"Invalid symbol in template pattern: '{part}'")

        TokenModelParser.validate_syntax(tokens)


class ExpressionTemplateParser:
    """Parses pasted mathematical expressions into a structured template with editable value slots."""

    @classmethod
    def parse_pasted_expression(cls, expr: str) -> Tuple[MathTemplate, List[str]]:
        """
        Parses a pasted expression (e.g. '(15.5 + 4.25) + 8.0' or '(□ + □) + □')
        into an immutable MathTemplate and a list of extracted initial slot values.
        """
        clean = expr.strip()
        if not clean:
            raise ValueError("Pasted expression is empty")

        # Tokenize expression respecting numbers, parens, operators, and □
        raw_tokens = re.findall(r"\(|\)|\+|\□|\d+(?:\.\d*)?|\.\d+|[^\s()+\d□]+", clean)

        pattern_parts: List[str] = []
        initial_values: List[str] = []

        for tok in raw_tokens:
            tok = tok.strip()
            if not tok:
                continue
            if tok in ("(", ")", "+"):
                pattern_parts.append(tok)
            elif tok == "□":
                pattern_parts.append("□")
                initial_values.append("")
            elif is_valid_number(tok):
                pattern_parts.append("□")
                initial_values.append(tok)
            else:
                raise ValueError(
                    f"Unsupported token '{tok}' in pasted addition expression. "
                    f"Only addition '+', parentheses '()', and finite numbers are supported in this stage."
                )

        pattern_str = " ".join(pattern_parts)
        # Deterministic mathematical validation
        TemplateValidator.validate_addition_pattern(pattern_str)

        tpl_id = f"custom_{re.sub(r'[^a-zA-Z0-9]', '_', pattern_str)}"
        template = MathTemplate(
            template_id=tpl_id,
            pattern=pattern_str,
            name=f"Template ({pattern_str})",
            is_custom=True,
        )
        return template, initial_values


class MathTemplateManager:
    """Manages standard and custom persisted mathematical templates."""

    BUILTIN_PATTERNS = [
        ("□ + □", "Two terms (a + b)"),
        ("(□ + □)", "Parenthesized pair (a + b)"),
        ("□ + □ + □", "Three terms (a + b + c)"),
        ("(□ + □) + □", "Group plus term ((a + b) + c)"),
        ("(□ + (□ + □))", "Nested group (a + (b + c))"),
    ]

    def __init__(self, storage_file: Optional[Path] = None) -> None:
        if storage_file is None:
            storage_file = _PROJECT_ROOT / "addition_tokens" / "custom_templates.json"
        self.storage_file = Path(storage_file)
        self.templates: List[MathTemplate] = []
        self._load_templates()

    def _load_templates(self) -> None:
        self.templates = [
            MathTemplate(
                template_id=f"builtin_{idx}",
                pattern=p,
                name=n,
                is_custom=False,
            )
            for idx, (p, n) in enumerate(self.BUILTIN_PATTERNS, start=1)
        ]
        if self.storage_file.exists():
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for item in data:
                        p = item.get("pattern", "")
                        n = item.get("name", p)
                        tid = item.get("template_id", f"custom_{len(self.templates)}")
                        if p and not any(t.pattern == p for t in self.templates):
                            self.templates.append(
                                MathTemplate(template_id=tid, pattern=p, name=n, is_custom=True)
                            )
            except Exception:
                pass

    def save_custom_template(self, template: MathTemplate) -> None:
        """Explicitly saves a reviewed template to the permanent templates registry."""
        TemplateValidator.validate_addition_pattern(template.pattern)
        template.is_custom = True
        if not any(t.pattern == template.pattern for t in self.templates):
            self.templates.append(template)
            self._persist()

    def _persist(self) -> None:
        customs = [
            {"template_id": t.template_id, "pattern": t.pattern, "name": t.name}
            for t in self.templates if t.is_custom
        ]
        try:
            self.storage_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.storage_file, "w", encoding="utf-8") as f:
                json.dump(customs, f, indent=2)
        except Exception:
            pass


@dataclass
class TemplateInstance:
    """An active template instance applied to Column 1 of an addend row."""
    template: MathTemplate
    slots: List[TemplateSlot] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.slots:
            self.slots = [
                TemplateSlot(slot_id=meta.slot_id, name=meta.name, expected_type=meta.expected_type)
                for meta in self.template.slots_meta
            ]

    def to_token_stream(self, trailing_labels: Optional[List[str]] = None) -> List[Token]:
        """
        Converts the active template into an evaluated Token stream,
        verifying that all slots are filled.
        """
        tokens: List[Token] = []
        pattern = self.template.pattern
        slot_idx = 0

        row_item = ""
        row_context = ""
        extra_contexts: List[str] = []
        if trailing_labels:
            if len(trailing_labels) > 0 and trailing_labels[0].strip():
                row_item = trailing_labels[0].strip()
            if len(trailing_labels) > 1 and trailing_labels[1].strip():
                row_context = trailing_labels[1].strip()
            if len(trailing_labels) > 2:
                extra_contexts = [lbl.strip() for lbl in trailing_labels[2:] if lbl.strip()]

        i = 0
        while i < len(pattern):
            ch = pattern[i]
            if ch == "□":
                if slot_idx < len(self.slots):
                    slot = self.slots[slot_idx]
                    val = slot.value.strip()
                    if not val:
                        raise ValueError(f"Template field '{slot.name}' is empty (□). Please enter a number before calculating.")
                    tokens.append(Token(value=val, token_type=TokenType.NUMBER, explicit_type=True))

                    # Item / Unit
                    unit = slot.bound_unit.strip() or row_item
                    if unit:
                        tokens.append(Token(value=unit, token_type=TokenType.ITEM))

                    # Context
                    ctx = slot.bound_context.strip() or row_context
                    if ctx:
                        tokens.append(Token(value=ctx, token_type=TokenType.CONTEXT))

                    for extra in extra_contexts:
                        tokens.append(Token(value=extra, token_type=TokenType.CONTEXT))

                    slot_idx += 1
                i += 1
            elif ch == "(":
                tokens.append(Token(value="(", token_type=TokenType.GROUP_OPEN, explicit_type=True))
                i += 1
            elif ch == ")":
                tokens.append(Token(value=")", token_type=TokenType.GROUP_CLOSE, explicit_type=True))
                i += 1
            elif ch == "+":
                tokens.append(Token(value="+", token_type=TokenType.OPERATOR, explicit_type=True))
                i += 1
            elif ch.isspace():
                i += 1
            else:
                i += 1

        return tokens


@dataclass
class TemplateRow:
    """Represents a row in the template-driven calculator."""
    row_type: RowType = RowType.ADDEND
    template_instance: Optional[TemplateInstance] = None
    explanation_text: str = ""                              # For RowType.LABEL
    description_columns: List[str] = field(default_factory=lambda: ["", ""])  # Col 2: Item, Col 3: Context

    def __post_init__(self) -> None:
        if self.row_type == RowType.ADDEND and self.template_instance is None:
            default_tpl = MathTemplate(template_id="default", pattern="□ + □", name="Two terms (a + b)")
            self.template_instance = default_tpl.create_instance()
        if not self.description_columns:
            self.description_columns = ["", ""]


class TemplateGridModel:
    """
    Data model managing template-driven rows, slot editing,
    descriptive columns, and mathematical evaluation.
    """

    def __init__(self, template_manager: Optional[MathTemplateManager] = None) -> None:
        self.template_manager = template_manager or MathTemplateManager()
        self.rows: List[TemplateRow] = [TemplateRow(row_type=RowType.ADDEND)]
        # Selection Cursor
        self.cursor_row: int = 0
        self.cursor_col: int = 1   # 1 = Math Template (Col 1), 2 = Item, 3 = Context, 4+ = extra
        self.cursor_slot: int = 0  # Which slot (0..N) in Column 1 is active
        self.last_parse_result: Optional[ParseResult] = None

    def get_max_description_columns(self) -> int:
        counts = [len(r.description_columns) for r in self.rows if r.row_type == RowType.ADDEND]
        return max(counts) if counts else 2

    def select_slot(self, row_idx: int, slot_idx: int) -> None:
        if 0 <= row_idx < len(self.rows):
            self.cursor_row = row_idx
            self.cursor_col = 1
            row = self.rows[row_idx]
            if row.template_instance and row.template_instance.slots:
                self.cursor_slot = max(0, min(slot_idx, len(row.template_instance.slots) - 1))
            else:
                self.cursor_slot = 0

    def select_col(self, row_idx: int, col_idx: int) -> None:
        if 0 <= row_idx < len(self.rows):
            self.cursor_row = row_idx
            self.cursor_col = col_idx

    def apply_template_to_row(
        self,
        row_idx: int,
        template: MathTemplate,
        initial_values: Optional[List[str]] = None
    ) -> TemplateInstance:
        """Applies a mathematical template to Row `row_idx`, Column 1."""
        if not (0 <= row_idx < len(self.rows)):
            row_idx = 0
        row = self.rows[row_idx]
        row.row_type = RowType.ADDEND
        inst = template.create_instance(initial_values)
        row.template_instance = inst
        self.cursor_row = row_idx
        self.cursor_col = 1
        self.cursor_slot = 0
        return inst

    def add_description_column(self) -> int:
        """Adds another descriptive column to the right across all rows."""
        for r in self.rows:
            r.description_columns.append("")
        return self.get_max_description_columns()

    def add_row(self, row_type: RowType, explanation: str = "") -> int:
        """Explicitly creates a new row with designated row type."""
        if row_type == RowType.ALGEBRA_STEP:
            raise ValueError("Algebra steps are reserved for a future development stage and cannot be executed yet.")

        new_row = TemplateRow(row_type=row_type, explanation_text=explanation)
        self.rows.append(new_row)
        new_row_idx = len(self.rows) - 1
        self.cursor_row = new_row_idx
        self.cursor_col = 1 if row_type == RowType.ADDEND else 0
        self.cursor_slot = 0
        return new_row_idx

    def input_number(self, val: str) -> None:
        """Inputs number string into the currently selected slot or cell."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.explanation_text = (row.explanation_text + val).strip()
            return

        if self.cursor_col == 1:
            if row.template_instance and row.template_instance.slots:
                slot = row.template_instance.slots[self.cursor_slot]
                slot.value = (slot.value + val).strip()
        else:
            desc_idx = self.cursor_col - 2
            if 0 <= desc_idx < len(row.description_columns):
                row.description_columns[desc_idx] = (row.description_columns[desc_idx] + val).strip()

    def set_active_value(self, val: str) -> None:
        """Replaces the value of the currently selected slot or description cell."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.explanation_text = val
            return

        if self.cursor_col == 1:
            if row.template_instance and row.template_instance.slots:
                if is_valid_number(val):
                    row.template_instance.slots[self.cursor_slot].value = val
                else:
                    # Non-numeric labels route to description columns (Col 2: Item, Col 3: Context)
                    lower = val.lower().strip()
                    context_prefixes = ("in ", "on ", "at ", "under ", "with ", "near ", "inside ")
                    if any(lower.startswith(p) for p in context_prefixes):
                        row.description_columns[1] = val
                    else:
                        row.description_columns[0] = val
        else:
            desc_idx = self.cursor_col - 2
            if 0 <= desc_idx < len(row.description_columns):
                row.description_columns[desc_idx] = val

    def backspace(self) -> None:
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.explanation_text = row.explanation_text[:-1]
            return

        if self.cursor_col == 1:
            if row.template_instance and row.template_instance.slots:
                slot = row.template_instance.slots[self.cursor_slot]
                slot.value = slot.value[:-1]
        else:
            desc_idx = self.cursor_col - 2
            if 0 <= desc_idx < len(row.description_columns):
                row.description_columns[desc_idx] = row.description_columns[desc_idx][:-1]

    def clear(self) -> None:
        self.rows = [TemplateRow(row_type=RowType.ADDEND)]
        self.cursor_row = 0
        self.cursor_col = 1
        self.cursor_slot = 0
        self.last_parse_result = None

    def calculate(self) -> Optional[ParseResult]:
        """Calculates global mathematical total across all active addend rows."""
        all_tokens: List[Token] = []

        for row in self.rows:
            if row.row_type != RowType.ADDEND:
                continue  # Label rows do not contribute numbers
            if not row.template_instance:
                continue

            row_tokens = row.template_instance.to_token_stream(row.description_columns)
            if not row_tokens:
                continue

            if all_tokens:
                if all_tokens[-1].token_type != TokenType.OPERATOR and row_tokens[0].token_type != TokenType.OPERATOR:
                    all_tokens.append(Token(value="+", token_type=TokenType.OPERATOR, explicit_type=True))
            all_tokens.extend(row_tokens)

        if not all_tokens:
            self.last_parse_result = None
            return None

        parse_res = TokenModelParser.parse_tokens(all_tokens)
        self.last_parse_result = parse_res
        return parse_res


# -----------------------------------------------------------------------------
# Core AST and Legacy Token Model (Preserved)
# -----------------------------------------------------------------------------

@dataclass
class Token:
    """Represents a single token in the left-to-right statement."""
    value: str
    token_type: TokenType = field(default=TokenType.ITEM)
    explicit_type: bool = False

    def __post_init__(self) -> None:
        if not self.explicit_type:
            self.token_type = self.auto_classify(self.value)

    @classmethod
    def auto_classify(cls, val: str) -> TokenType:
        s = val.strip()
        if s == "(":
            return TokenType.GROUP_OPEN
        if s == ")":
            return TokenType.GROUP_CLOSE
        if s == "+":
            return TokenType.OPERATOR
        if is_valid_number(s):
            return TokenType.NUMBER

        lower = s.lower()
        context_prefixes = ("in ", "on ", "at ", "under ", "with ", "near ", "inside ")
        if any(lower.startswith(prefix) for prefix in context_prefixes):
            return TokenType.CONTEXT

        return TokenType.ITEM

    def set_type(self, new_type: TokenType) -> None:
        self.token_type = new_type
        self.explicit_type = True


@dataclass
class Subcolumn:
    value: str
    token_type: TokenType = field(default=TokenType.ITEM)
    explicit_type: bool = False

    def __post_init__(self) -> None:
        if not self.explicit_type:
            self.token_type = Token.auto_classify(self.value)

    def to_token(self) -> Token:
        return Token(value=self.value, token_type=self.token_type, explicit_type=self.explicit_type)

    @classmethod
    def from_token(cls, tok: Token) -> "Subcolumn":
        return cls(value=tok.value, token_type=tok.token_type, explicit_type=tok.explicit_type)


@dataclass
class SemanticTerm:
    quantity: str
    item: str
    context: str = ""
    extra_contexts: List[str] = field(default_factory=list)

    @property
    def full_description(self) -> str:
        parts = [self.item]
        if self.context:
            parts.append(self.context)
        parts.extend(self.extra_contexts)
        return " ".join(p for p in parts if p).strip()

    @property
    def is_single_unit(self) -> bool:
        try:
            return Decimal(self.quantity) == Decimal(1)
        except Exception:
            return self.quantity in ("1", "1.0")


@dataclass
class AddendRepresentation:
    ordered_subcolumns: List[Subcolumn] = field(default_factory=list)
    parsed_terms: List[SemanticTerm] = field(default_factory=list)
    aggregated_results: List[SemanticTerm] = field(default_factory=list)
    raw_expression: str = ""
    total_number: str = ""

    def evaluate(self) -> None:
        tokens = [sc.to_token() for sc in self.ordered_subcolumns if sc.value.strip()]
        if not tokens:
            self.parsed_terms = []
            self.aggregated_results = []
            self.raw_expression = ""
            self.total_number = ""
            return

        res = TokenModelParser.parse_tokens(tokens)
        self.raw_expression = res.raw_expression
        self.total_number = res.total_number
        self.parsed_terms = res.individual_terms
        self.aggregated_results = res.aggregated_terms


@dataclass
class GridRow:
    row_type: RowType = RowType.ADDEND
    label_text: str = ""
    addend_columns: List[AddendRepresentation] = field(default_factory=list)
    description_columns: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.row_type == RowType.ADDEND and not self.addend_columns:
            self.addend_columns.append(AddendRepresentation())


@dataclass
class ParseResult:
    raw_expression: str
    total_number: str
    individual_terms: List[SemanticTerm]
    aggregated_terms: List[SemanticTerm]
    word_result: str


class TokenModelParser:
    @classmethod
    def validate_syntax(cls, tokens: List[Token]) -> None:
        if not tokens:
            raise ValueError("Expression is empty")

        depth = 0
        for idx, tok in enumerate(tokens):
            if tok.token_type == TokenType.GROUP_OPEN:
                depth += 1
            elif tok.token_type == TokenType.GROUP_CLOSE:
                depth -= 1
                if depth < 0:
                    raise ValueError(f"Unmatched closing parenthesis at token position {idx + 1}")
        if depth > 0:
            raise ValueError("Missing closing parenthesis: unclosed '(' in expression")

        for i in range(len(tokens) - 1):
            if (tokens[i].token_type == TokenType.GROUP_OPEN and
                    tokens[i + 1].token_type == TokenType.GROUP_CLOSE):
                raise ValueError(f"Empty group: '()' contains no operands at position {i + 1}")

        math_tokens: List[Tuple[int, Token]] = [
            (idx, tok) for idx, tok in enumerate(tokens)
            if tok.token_type in (TokenType.NUMBER, TokenType.OPERATOR, TokenType.GROUP_OPEN, TokenType.GROUP_CLOSE)
        ]

        if not any(tok.token_type == TokenType.NUMBER for _, tok in math_tokens):
            raise ValueError("Missing operands: statement contains no numbers")

        if math_tokens and math_tokens[0][1].token_type == TokenType.OPERATOR:
            raise ValueError(f"Leading operator: expected operand before '+' at position {math_tokens[0][0] + 1}")

        if math_tokens and math_tokens[-1][1].token_type == TokenType.OPERATOR:
            raise ValueError(f"Trailing operator: expected operand after '+' at position {math_tokens[-1][0] + 1}")

        for i in range(len(math_tokens) - 1):
            orig_idx, tok = math_tokens[i]
            next_orig_idx, next_tok = math_tokens[i + 1]

            if tok.token_type == TokenType.OPERATOR and next_tok.token_type == TokenType.OPERATOR:
                raise ValueError(f"Consecutive operators: '+' cannot follow '+' at position {next_orig_idx + 1}")

            if tok.token_type == TokenType.GROUP_OPEN and next_tok.token_type == TokenType.OPERATOR:
                raise ValueError(f"Missing operand before '+' inside group at position {next_orig_idx + 1}")

            if tok.token_type == TokenType.OPERATOR and next_tok.token_type == TokenType.GROUP_CLOSE:
                raise ValueError(f"Missing operand after '+' inside group at position {orig_idx + 1}")

            if tok.token_type == TokenType.NUMBER and next_tok.token_type == TokenType.NUMBER:
                raise ValueError(f"Missing operator between numbers at positions {orig_idx + 1} and {next_orig_idx + 1}")

    @classmethod
    def parse_tokens(cls, tokens: List[Token]) -> ParseResult:
        cls.validate_syntax(tokens)

        math_parts: List[str] = []
        for tok in tokens:
            if tok.token_type == TokenType.NUMBER:
                math_parts.append(tok.value)
            elif tok.token_type in (TokenType.OPERATOR, TokenType.GROUP_OPEN, TokenType.GROUP_CLOSE):
                math_parts.append(tok.value)

        expr_str = " ".join(math_parts)
        total_number = evaluate_addition(expr_str)

        individual_terms = cls._extract_semantic_terms(tokens)

        for term in individual_terms:
            if not term.item.strip():
                raise ValueError(f"Unlabeled quantity: '{term.quantity}' has no item label")

        items_for_chatbot = [
            (t.quantity, t.item, t.context, *t.extra_contexts)
            for t in individual_terms
        ]
        word_result = WordSummerChatbot.summarize(items_for_chatbot, total_number)

        if word_result and not re.match(r"^\d", word_result.strip()):
            word_result = f"{total_number} {word_result}"

        aggregated_terms = cls._aggregate_terms(individual_terms)

        return ParseResult(
            raw_expression=expr_str,
            total_number=total_number,
            individual_terms=individual_terms,
            aggregated_terms=aggregated_terms,
            word_result=word_result,
        )

    @classmethod
    def _extract_semantic_terms(cls, tokens: List[Token]) -> List[SemanticTerm]:
        @dataclass
        class TermDraft:
            quantity: str
            item: str = ""
            context: str = ""
            extra_contexts: List[str] = field(default_factory=list)
            inside_group_depth: int = 0
            group_id: int = 0

        drafts: List[TermDraft] = []
        group_stack: List[int] = []
        current_group_counter = 0
        group_members: Dict[int, List[int]] = {}
        trailing_group_labels: Dict[int, Tuple[str, str, List[str]]] = {}

        i = 0
        n = len(tokens)
        last_closed_group: Optional[int] = None

        while i < n:
            tok = tokens[i]

            if tok.token_type == TokenType.GROUP_OPEN:
                current_group_counter += 1
                group_stack.append(current_group_counter)
                group_members[current_group_counter] = []
                last_closed_group = None
                i += 1
                continue

            elif tok.token_type == TokenType.GROUP_CLOSE:
                if group_stack:
                    last_closed_group = group_stack.pop()
                i += 1
                continue

            elif tok.token_type == TokenType.NUMBER:
                draft = TermDraft(
                    quantity=tok.value,
                    inside_group_depth=len(group_stack),
                    group_id=group_stack[-1] if group_stack else 0,
                )
                draft_idx = len(drafts)
                drafts.append(draft)
                if group_stack:
                    group_members[group_stack[-1]].append(draft_idx)

                last_closed_group = None
                i += 1

                while i < n and tokens[i].token_type in (TokenType.ITEM, TokenType.CONTEXT):
                    sub_tok = tokens[i]
                    if sub_tok.token_type == TokenType.ITEM:
                        if not draft.item:
                            draft.item = sub_tok.value
                        else:
                            draft.extra_contexts.append(sub_tok.value)
                    elif sub_tok.token_type == TokenType.CONTEXT:
                        if not draft.context:
                            draft.context = sub_tok.value
                        else:
                            draft.extra_contexts.append(sub_tok.value)
                    i += 1
                continue

            elif tok.token_type in (TokenType.ITEM, TokenType.CONTEXT):
                if last_closed_group is not None:
                    trailing_item = ""
                    trailing_ctx = ""
                    trailing_extras: List[str] = []
                    while i < n and tokens[i].token_type in (TokenType.ITEM, TokenType.CONTEXT):
                        lbl = tokens[i]
                        if lbl.token_type == TokenType.ITEM and not trailing_item:
                            trailing_item = lbl.value
                        elif lbl.token_type == TokenType.CONTEXT and not trailing_ctx:
                            trailing_ctx = lbl.value
                        else:
                            trailing_extras.append(lbl.value)
                        i += 1
                    trailing_group_labels[last_closed_group] = (trailing_item, trailing_ctx, trailing_extras)
                    continue

                elif drafts:
                    last_draft = drafts[-1]
                    if tok.token_type == TokenType.ITEM and not last_draft.item:
                        last_draft.item = tok.value
                    elif tok.token_type == TokenType.CONTEXT and not last_draft.context:
                        last_draft.context = tok.value
                    else:
                        last_draft.extra_contexts.append(tok.value)
                i += 1

            elif tok.token_type == TokenType.OPERATOR:
                last_closed_group = None
                i += 1

            else:
                i += 1

        for gid, (t_item, t_ctx, t_extras) in trailing_group_labels.items():
            member_indices = group_members.get(gid, [])
            for idx in member_indices:
                member = drafts[idx]
                if not member.item and t_item:
                    member.item = t_item

                if not member.context and t_ctx:
                    member.context = t_ctx
                elif member.context and t_ctx and t_ctx not in member.extra_contexts:
                    member.extra_contexts.append(t_ctx)

                if t_extras:
                    for ext in t_extras:
                        if ext not in member.extra_contexts:
                            member.extra_contexts.append(ext)

        final_terms: List[SemanticTerm] = []
        for d in drafts:
            qty = d.quantity
            item = d.item
            if item:
                is_one = False
                try:
                    is_one = (Decimal(qty) == Decimal(1))
                except Exception:
                    is_one = (qty in ("1", "1.0"))
                item = WordSummerChatbot._pluralize_word(item, is_one)

            final_terms.append(SemanticTerm(
                quantity=qty,
                item=item,
                context=d.context,
                extra_contexts=list(d.extra_contexts),
            ))

        return final_terms

    @classmethod
    def _aggregate_terms(cls, terms: List[SemanticTerm]) -> List[SemanticTerm]:
        groups: Dict[Tuple[str, str], Decimal] = {}
        order: List[Tuple[str, str]] = []

        for t in terms:
            lemma = WordSummerChatbot._lemmatize_word(t.item)
            key = (lemma, t.context)
            try:
                val = Decimal(t.quantity)
            except Exception:
                val = Decimal(0)

            if key not in groups:
                groups[key] = val
                order.append(key)
            else:
                groups[key] += val

        aggregated: List[SemanticTerm] = []
        for key in order:
            total_val = groups[key]
            fmt = format(total_val, "f")
            if "." in fmt:
                fmt = fmt.rstrip("0").rstrip(".")
            if not fmt or fmt == "-0":
                fmt = "0"
            is_one = (total_val == Decimal(1))
            disp_item = WordSummerChatbot._pluralize_word(key[0], is_one)
            aggregated.append(SemanticTerm(quantity=fmt, item=disp_item, context=key[1]))

        return aggregated


class TokenGridModel:
    """
    Adapter model providing backward compatibility for previous test suites.
    """

    def __init__(self) -> None:
        self.rows: List[GridRow] = [GridRow(row_type=RowType.ADDEND)]
        self.cursor_row: int = 0
        self.cursor_area: str = "addend"
        self.cursor_addend_col: int = 0
        self.cursor_subcol: int = 0
        self.cursor_desc_col: int = 0
        self.last_parse_result: Optional[ParseResult] = None

    def get_max_addend_columns(self) -> int:
        counts = [len(r.addend_columns) for r in self.rows if r.row_type == RowType.ADDEND]
        return max(counts) if counts else 1

    def select_cell(
        self,
        row_idx: int,
        area: str = "addend",
        col_idx: int = 0,
        subcol_idx: int = 0
    ) -> None:
        if not (0 <= row_idx < len(self.rows)):
            row_idx = max(0, min(row_idx, len(self.rows) - 1))
        self.cursor_row = row_idx
        row = self.rows[row_idx]

        if row.row_type == RowType.LABEL:
            self.cursor_area = "label"
            return

        if area == "description":
            self.cursor_area = "description"
            self.cursor_desc_col = max(0, min(col_idx, len(row.description_columns) - 1)) if row.description_columns else 0
            return

        self.cursor_area = "addend"
        if not row.addend_columns:
            row.addend_columns.append(AddendRepresentation())
        self.cursor_addend_col = max(0, min(col_idx, len(row.addend_columns) - 1))
        addend = row.addend_columns[self.cursor_addend_col]
        self.cursor_subcol = max(0, min(subcol_idx, len(addend.ordered_subcolumns) - 1)) if addend.ordered_subcolumns else 0

    def get_selection_label(self) -> str:
        if not (0 <= self.cursor_row < len(self.rows)):
            return "No selection"
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            return f"Row {self.cursor_row + 1} [Label Row]"

        col_num = self.cursor_addend_col + 1
        if self.cursor_area == "description":
            val = row.description_columns[self.cursor_desc_col] if self.cursor_desc_col < len(row.description_columns) else "empty"
            return f"Row {self.cursor_row + 1} | Description Col {self.cursor_desc_col + 1} ('{val}')"

        if self.cursor_addend_col < len(row.addend_columns):
            addend = row.addend_columns[self.cursor_addend_col]
            if not addend.ordered_subcolumns:
                return f"Row {self.cursor_row + 1} | Main Col {col_num} [empty column]"
            if self.cursor_subcol < len(addend.ordered_subcolumns):
                sc = addend.ordered_subcolumns[self.cursor_subcol]
                return f"Row {self.cursor_row + 1} | Main Col {col_num} | Subcol {self.cursor_subcol + 1} ('{sc.value}')"
            else:
                return f"Row {self.cursor_row + 1} | Main Col {col_num} | New Subcol {len(addend.ordered_subcolumns) + 1}"
        return f"Row {self.cursor_row + 1} | Main Col {col_num}"

    def delete_selected_column(self) -> None:
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.label_text = ""
            return

        if self.cursor_area == "addend":
            if len(row.addend_columns) > 1:
                row.addend_columns.pop(self.cursor_addend_col)
                self.cursor_addend_col = max(0, min(self.cursor_addend_col, len(row.addend_columns) - 1))
                self.cursor_subcol = 0
            else:
                row.addend_columns[0].ordered_subcolumns = []
                self.cursor_subcol = 0
        else:
            if len(row.description_columns) > 1:
                row.description_columns.pop(self.cursor_desc_col)
                self.cursor_desc_col = max(0, min(self.cursor_desc_col, len(row.description_columns) - 1))
            elif row.description_columns:
                row.description_columns[0] = ""

    def delete_selected_subcolumn(self) -> None:
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.ADDEND and self.cursor_area == "addend":
            if 0 <= self.cursor_addend_col < len(row.addend_columns):
                addend = row.addend_columns[self.cursor_addend_col]
                if addend.ordered_subcolumns:
                    idx = max(0, min(self.cursor_subcol, len(addend.ordered_subcolumns) - 1))
                    addend.ordered_subcolumns.pop(idx)
                    self.cursor_subcol = max(0, min(self.cursor_subcol, len(addend.ordered_subcolumns) - 1))

    def next_subcolumn(self) -> Tuple[int, int, int]:
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            return self.cursor_row, 0, 0

        self.cursor_area = "addend"
        addend = row.addend_columns[self.cursor_addend_col]
        self.cursor_subcol = len(addend.ordered_subcolumns)
        return self.cursor_row, self.cursor_addend_col, self.cursor_subcol

    def next_column(self) -> Tuple[int, str, int]:
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            return self.cursor_row, "label", 0

        if self.cursor_area == "addend":
            self.cursor_addend_col += 1
            if self.cursor_addend_col >= len(row.addend_columns):
                row.addend_columns.append(AddendRepresentation())
            self.cursor_subcol = 0
            return self.cursor_row, "addend", self.cursor_addend_col
        else:
            self.cursor_desc_col += 1
            if self.cursor_desc_col >= len(row.description_columns):
                row.description_columns.append("")
            return self.cursor_row, "description", self.cursor_desc_col

    def next_addend(self) -> int:
        new_row = GridRow(row_type=RowType.ADDEND)
        self.rows.append(new_row)
        self.cursor_row = len(self.rows) - 1
        self.cursor_area = "addend"
        self.cursor_addend_col = 0
        self.cursor_subcol = 0
        self.cursor_desc_col = 0
        return self.cursor_row

    def add_label_row(self, text: str = "") -> int:
        new_row = GridRow(row_type=RowType.LABEL, label_text=text)
        self.rows.append(new_row)
        self.cursor_row = len(self.rows) - 1
        self.cursor_area = "label"
        return self.cursor_row

    def input_value(self, val: str, token_type: Optional[TokenType] = None) -> Subcolumn:
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.label_text = (row.label_text + " " + val).strip()
            return Subcolumn(value=row.label_text, token_type=TokenType.CONTEXT)

        if self.cursor_area == "description":
            if self.cursor_desc_col >= len(row.description_columns):
                row.description_columns.append(val)
                self.cursor_desc_col = len(row.description_columns) - 1
            else:
                row.description_columns[self.cursor_desc_col] = val
            return Subcolumn(value=val, token_type=TokenType.CONTEXT)

        addend = row.addend_columns[self.cursor_addend_col]
        subcol = Subcolumn(value=val)
        if token_type is not None:
            subcol.token_type = token_type
            subcol.explicit_type = True

        if not addend.ordered_subcolumns:
            addend.ordered_subcolumns.append(subcol)
            self.cursor_subcol = 0
        elif self.cursor_subcol >= len(addend.ordered_subcolumns):
            addend.ordered_subcolumns.append(subcol)
            self.cursor_subcol = len(addend.ordered_subcolumns) - 1
        else:
            addend.ordered_subcolumns[self.cursor_subcol] = subcol

        return subcol

    def backspace(self) -> None:
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.explanation_text = row.explanation_text[:-1]
            return

        if self.cursor_area == "addend":
            addend = row.addend_columns[self.cursor_addend_col]
            if addend.ordered_subcolumns:
                idx = min(self.cursor_subcol, len(addend.ordered_subcolumns) - 1)
                addend.ordered_subcolumns.pop(idx)
                if self.cursor_subcol > 0:
                    self.cursor_subcol -= 1

    def clear(self) -> None:
        self.rows = [GridRow(row_type=RowType.ADDEND)]
        self.cursor_row = 0
        self.cursor_area = "addend"
        self.cursor_addend_col = 0
        self.cursor_subcol = 0
        self.cursor_desc_col = 0
        self.last_parse_result = None

    def calculate(self) -> Optional[ParseResult]:
        all_tokens: List[Token] = []

        for row in self.rows:
            if row.row_type != RowType.ADDEND:
                continue

            row_tokens: List[Token] = []
            for addend in row.addend_columns:
                addend.evaluate()
                addend_toks = [sc.to_token() for sc in addend.ordered_subcolumns if sc.value.strip()]
                if not addend_toks:
                    continue

                if row_tokens:
                    if row_tokens[-1].token_type != TokenType.OPERATOR and addend_toks[0].token_type != TokenType.OPERATOR:
                        row_tokens.append(Token(value="+", token_type=TokenType.OPERATOR, explicit_type=True))
                row_tokens.extend(addend_toks)

            if not row_tokens:
                continue

            for desc in row.description_columns:
                if desc.strip():
                    row_tokens.append(Token(value=desc.strip(), token_type=TokenType.CONTEXT))

            if all_tokens:
                if all_tokens[-1].token_type != TokenType.OPERATOR and row_tokens[0].token_type != TokenType.OPERATOR:
                    all_tokens.append(Token(value="+", token_type=TokenType.OPERATOR, explicit_type=True))
            all_tokens.extend(row_tokens)

        if not all_tokens:
            self.last_parse_result = None
            return None

        parse_res = TokenModelParser.parse_tokens(all_tokens)
        self.last_parse_result = parse_res
        return parse_res

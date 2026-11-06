"""Token data model, AST, parser, and semantic binder for addition_tokens.

Features:
- Deterministic mathematical template validator and parser for pasted addition expressions.
- Named, typed placeholder slots (TemplateSlot) keeping structure separate from runtime values.
- Persisted custom templates with optional saving (MathTemplateManager).
- Row types: ADDEND, LABEL, and non-executable ALGEBRA_STEP placeholder.
- Three representations of each addend (ordered subcolumns, parsed mathematical structure, aggregated results).
- Strict validation, unit identity preservation, and safe error reporting.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from enum import Enum, auto
import json
from pathlib import Path
import re
import sys
import uuid
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
    UNKNOWN = auto()      # "□" or placeholder

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
            "unknown": cls.UNKNOWN,
            "placeholder": cls.UNKNOWN,
            "□": cls.UNKNOWN,
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
            TokenType.UNKNOWN: "Unknown",
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
class DescriptionField:
    """A typed descriptive field belonging to a specific numerical addend."""
    field_type: str = "item"         # "item", "context", "location", "time", "condition", "custom"
    value: str = ""
    field_label: str = "Item"        # Display label for UI column header


@dataclass
class TemplateSlot:
    """An instance of an editable value slot with stable identity and structured descriptions."""
    slot_id: int
    name: str
    expected_type: str = "NUMBER"
    value: str = ""                 # User-entered quantity (e.g. "1", "2.5")
    slot_uuid: str = field(default_factory=lambda: f"slot_{uuid.uuid4().hex[:8]}")
    descriptions: List[DescriptionField] = field(default_factory=lambda: [
        DescriptionField(field_type="item", value="", field_label="Item"),
        DescriptionField(field_type="context", value="", field_label="Context")
    ])

    @property
    def bound_unit(self) -> str:
        if self.descriptions and len(self.descriptions) > 0:
            return self.descriptions[0].value
        return ""

    @bound_unit.setter
    def bound_unit(self, val: str) -> None:
        if not self.descriptions:
            self.descriptions.append(DescriptionField(field_type="item", value=val, field_label="Item"))
        else:
            self.descriptions[0].value = val

    @property
    def bound_context(self) -> str:
        if len(self.descriptions) > 1:
            return self.descriptions[1].value
        return ""

    @bound_context.setter
    def bound_context(self, val: str) -> None:
        while len(self.descriptions) < 2:
            self.descriptions.append(DescriptionField(field_type="context", value="", field_label="Context"))
        self.descriptions[1].value = val

    @property
    def description_values(self) -> List[str]:
        return [d.value for d in self.descriptions]

    @property
    def is_filled(self) -> bool:
        return bool(self.value.strip())

    def add_description_field(self, field_type: str = "custom", label: str = "") -> DescriptionField:
        lbl = label or f"Description {len(self.descriptions) + 1}"
        df = DescriptionField(field_type=field_type, value="", field_label=lbl)
        self.descriptions.append(df)
        return df


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
        existing = next((t for t in self.templates if t.pattern == template.pattern), None)
        if existing is not None:
            # Prevent saving a duplicate of an existing built-in template from converting it into custom
            if not existing.is_custom:
                return
            existing.name = template.name
            self._persist()
            return

        template.is_custom = True
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
                json.dump(customs, f, indent=2, ensure_ascii=False)
        except Exception:
            pass


class BlockType(Enum):
    ADDEND = auto()      # Numerical slot + its own description fields
    STRUCTURAL = auto()  # Operator '+', Parenthesis '(', ')'


@dataclass
class TokenBlock:
    """Represents an ordered block in the mathematical row sequence."""
    block_type: BlockType
    structural_char: str = ""               # For STRUCTURAL: '(', ')', '+'
    structural_type: Optional[TokenType] = None
    slot: Optional[TemplateSlot] = None     # For ADDEND: numerical slot with its descriptions

    @property
    def is_addend(self) -> bool:
        return self.block_type == BlockType.ADDEND

    @property
    def is_structural(self) -> bool:
        return self.block_type == BlockType.STRUCTURAL


@dataclass
class TemplateInstance:
    """An active template instance applied to an addend row."""
    template: MathTemplate
    slots: List[TemplateSlot] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.slots:
            self.slots = [
                TemplateSlot(slot_id=meta.slot_id, name=meta.name, expected_type=meta.expected_type)
                for meta in self.template.slots_meta
            ]

    def append_addend_slot(self, new_pattern: str) -> TemplateSlot:
        """
        Appends a fresh Number Group slot to this active runtime instance in-place,
        updating the instance's authoritative template pattern while preserving
        all existing slots, UUIDs, values, item labels, contexts, and extra descriptions.
        """
        new_slot_idx = len(self.slots)
        new_slot = TemplateSlot(
            slot_id=new_slot_idx,
            name=f"Term {new_slot_idx + 1}",
            expected_type="NUMBER",
            descriptions=[
                DescriptionField(field_type="item", value="", field_label="Item"),
                DescriptionField(field_type="context", value="", field_label="Context"),
            ]
        )
        self.slots.append(new_slot)
        # Update template definition for this instance without modifying the stored blueprint
        self.template = MathTemplate(
            template_id=f"ext_{uuid.uuid4().hex[:8]}",
            pattern=new_pattern,
            name=f"Template ({new_pattern})",
            is_custom=True,
        )
        return new_slot

    def get_blocks(self) -> List[TokenBlock]:
        """Decomposes the template pattern into an ordered sequence of structural and addend blocks."""
        blocks: List[TokenBlock] = []
        slot_idx = 0
        i = 0
        pattern = self.template.pattern
        while i < len(pattern):
            ch = pattern[i]
            if ch == "□":
                if slot_idx < len(self.slots):
                    blocks.append(TokenBlock(
                        block_type=BlockType.ADDEND,
                        slot=self.slots[slot_idx]
                    ))
                    slot_idx += 1
                i += 1
            elif ch == "(":
                blocks.append(TokenBlock(
                    block_type=BlockType.STRUCTURAL,
                    structural_char="(",
                    structural_type=TokenType.GROUP_OPEN
                ))
                i += 1
            elif ch == ")":
                blocks.append(TokenBlock(
                    block_type=BlockType.STRUCTURAL,
                    structural_char=")",
                    structural_type=TokenType.GROUP_CLOSE
                ))
                i += 1
            elif ch == "+":
                blocks.append(TokenBlock(
                    block_type=BlockType.STRUCTURAL,
                    structural_char="+",
                    structural_type=TokenType.OPERATOR
                ))
                i += 1
            elif ch.isspace():
                i += 1
            else:
                i += 1
        return blocks

    def to_token_stream(self, trailing_labels: Optional[List[str]] = None) -> List[Token]:
        """
        Converts the active template into an evaluated Token stream,
        verifying that all slots are filled.
        Each addend block emits its own value and its own structured descriptions.
        """
        tokens: List[Token] = []
        blocks = self.get_blocks()

        has_any_slot_descriptions = any(
            any(d.value.strip() for d in s.descriptions) for s in self.slots
        )
        allow_row_fallback = not has_any_slot_descriptions and bool(trailing_labels)

        for b in blocks:
            if b.is_structural:
                tokens.append(Token(
                    value=b.structural_char,
                    token_type=b.structural_type or TokenType.OPERATOR,
                    explicit_type=True
                ))
            elif b.is_addend and b.slot:
                slot = b.slot
                val = slot.value.strip()
                if not val:
                    raise ValueError(f"Template field '{slot.name}' is empty (□). Please enter a number before calculating.")
                if not is_valid_number(val):
                    raise ValueError(f"Invalid number '{val}' in template field '{slot.name}'. Expected a valid finite number.")
                tokens.append(Token(value=val, token_type=TokenType.NUMBER, explicit_type=True, slot_id=slot.slot_uuid))

                # Item (Col 2 of block)
                item_val = slot.descriptions[0].value.strip() if len(slot.descriptions) > 0 else ""
                if not item_val and allow_row_fallback and len(trailing_labels) > 0 and trailing_labels[0].strip():
                    item_val = trailing_labels[0].strip()
                if item_val:
                    tokens.append(Token(value=item_val, token_type=TokenType.ITEM, explicit_type=True))

                # Context (Col 3 of block)
                ctx_val = slot.descriptions[1].value.strip() if len(slot.descriptions) > 1 else ""
                if not ctx_val and allow_row_fallback and len(trailing_labels) > 1 and trailing_labels[1].strip():
                    ctx_val = trailing_labels[1].strip()
                if ctx_val:
                    tokens.append(Token(value=ctx_val, token_type=TokenType.CONTEXT, explicit_type=True))

                # Extra descriptions (Col 4+ of block)
                for desc in slot.descriptions[2:]:
                    if desc.value.strip():
                        tokens.append(Token(value=desc.value.strip(), token_type=TokenType.CONTEXT, explicit_type=True))

                # Extra descriptions from trailing_labels fallback
                if allow_row_fallback and len(trailing_labels) > 2:
                    for extra in trailing_labels[2:]:
                        if extra.strip() and not any(d.value.strip() == extra.strip() for d in slot.descriptions):
                            tokens.append(Token(value=extra.strip(), token_type=TokenType.CONTEXT, explicit_type=True))
        return tokens

    def to_editing_token_stream(self, trailing_labels: Optional[List[str]] = None) -> List[Token]:
        """
        Non-validating, read-only editing projection preserving:
        - Template structure (operators, parentheses).
        - Current slot values (or '□' placeholder when unfilled).
        - Slot identifiers (slot_uuid on Token).
        - Current selection / metadata.
        - Associated labels and contexts without throwing validation errors.
        """
        tokens: List[Token] = []
        blocks = self.get_blocks()

        has_any_slot_descriptions = any(
            any(d.value.strip() for d in s.descriptions) for s in self.slots
        )
        allow_row_fallback = not has_any_slot_descriptions and bool(trailing_labels)

        for b in blocks:
            if b.is_structural:
                tokens.append(Token(
                    value=b.structural_char,
                    token_type=b.structural_type or TokenType.OPERATOR,
                    explicit_type=True
                ))
            elif b.is_addend and b.slot:
                slot = b.slot
                val = slot.value.strip() if slot.value else ""
                if val:
                    tok_val = val
                    tok_type = TokenType.NUMBER if is_valid_number(val) else TokenType.UNKNOWN
                else:
                    tok_val = "□"
                    tok_type = TokenType.UNKNOWN

                tokens.append(Token(
                    value=tok_val,
                    token_type=tok_type,
                    explicit_type=True if val else False,
                    slot_id=slot.slot_id,
                ))

                # Item (Col 2 of block)
                item_val = slot.descriptions[0].value.strip() if len(slot.descriptions) > 0 else ""
                if not item_val and allow_row_fallback and len(trailing_labels) > 0 and trailing_labels[0].strip():
                    item_val = trailing_labels[0].strip()
                if item_val:
                    tokens.append(Token(value=item_val, token_type=TokenType.ITEM, explicit_type=True))

                # Context (Col 3 of block)
                ctx_val = slot.descriptions[1].value.strip() if len(slot.descriptions) > 1 else ""
                if not ctx_val and allow_row_fallback and len(trailing_labels) > 1 and trailing_labels[1].strip():
                    ctx_val = trailing_labels[1].strip()
                if ctx_val:
                    tokens.append(Token(value=ctx_val, token_type=TokenType.CONTEXT, explicit_type=True))

                # Extra descriptions (Col 4+ of block)
                for desc in slot.descriptions[2:]:
                    if desc.value.strip():
                        tokens.append(Token(value=desc.value.strip(), token_type=TokenType.CONTEXT, explicit_type=True))

                # Extra descriptions from trailing_labels fallback
                if allow_row_fallback and len(trailing_labels) > 2:
                    for extra in trailing_labels[2:]:
                        if extra.strip() and not any(d.value.strip() == extra.strip() for d in slot.descriptions):
                            tokens.append(Token(value=extra.strip(), token_type=TokenType.CONTEXT, explicit_type=True))
        return tokens


@dataclass
class TemplateRow:
    """Represents a row in the template-driven calculator."""
    row_type: RowType = RowType.ADDEND
    template_instance: Optional[TemplateInstance] = None
    explanation_text: str = ""                              # For RowType.LABEL
    description_columns: List[str] = field(default_factory=lambda: ["", ""])  # Preserved for backward compatibility

    def __post_init__(self) -> None:
        if self.row_type == RowType.ADDEND and self.template_instance is None:
            default_tpl = MathTemplate(template_id="default", pattern="□ + □", name="Two terms (a + b)")
            self.template_instance = default_tpl.create_instance()
        if not self.description_columns:
            self.description_columns = ["", ""]

    def to_editing_tokens(self) -> List[Token]:
        """Projects non-validating editing tokens for this row."""
        if self.row_type == RowType.ADDEND:
            if self.template_instance:
                return self.template_instance.to_editing_token_stream(self.description_columns)
            return []
        elif self.row_type == RowType.LABEL:
            if self.explanation_text:
                return [Token(value=self.explanation_text, token_type=TokenType.CONTEXT)]
            return []
        return []


class TemplateGridModel:
    """
    Data model managing template-driven rows, slot editing,
    repeated-block addend columns, and mathematical evaluation.
    """

    def __init__(self, template_manager: Optional[MathTemplateManager] = None) -> None:
        self.template_manager = template_manager or MathTemplateManager()
        self.rows: List[TemplateRow] = [TemplateRow(row_type=RowType.ADDEND)]
        # Selection Cursor
        self.cursor_row: int = 0
        self.cursor_slot: int = 0       # Active numerical slot index (0..N-1) in active row
        self.cursor_desc_col: int = 0   # 0 = Number slot, 1 = Item (Col 2), 2 = Context (Col 3), 3+ = Extra
        self._target_is_slot: bool = True
        self.last_parse_result: Optional[ParseResult] = None

    @property
    def cursor_col(self) -> int:
        """Backward-compatibility mapping of cursor column."""
        return self.cursor_desc_col + 1

    @cursor_col.setter
    def cursor_col(self, val: int) -> None:
        self.cursor_desc_col = max(0, val - 1)
        self._target_is_slot = False

    def get_max_description_columns(self) -> int:
        max_c = 2
        for r in self.rows:
            if r.row_type == RowType.ADDEND and r.template_instance:
                for s in r.template_instance.slots:
                    max_c = max(max_c, len(s.descriptions))
        return max_c

    def select_slot(self, row_idx: int, slot_idx: int) -> None:
        if 0 <= row_idx < len(self.rows):
            self.cursor_row = row_idx
            self.cursor_desc_col = 0
            self._target_is_slot = True
            row = self.rows[row_idx]
            if row.template_instance and row.template_instance.slots:
                self.cursor_slot = max(0, min(slot_idx, len(row.template_instance.slots) - 1))
            else:
                self.cursor_slot = 0

    def select_col(self, row_idx: int, col_idx: int) -> None:
        if 0 <= row_idx < len(self.rows):
            self.cursor_row = row_idx
            self.cursor_desc_col = max(0, col_idx - 1)
            self._target_is_slot = False

    def select_slot_field(self, row_idx: int, slot_idx: int, desc_col_idx: int = 0) -> None:
        if 0 <= row_idx < len(self.rows):
            self.cursor_row = row_idx
            self._target_is_slot = True
            row = self.rows[row_idx]
            if row.template_instance and row.template_instance.slots:
                self.cursor_slot = max(0, min(slot_idx, len(row.template_instance.slots) - 1))
            else:
                self.cursor_slot = 0
            self.cursor_desc_col = desc_col_idx

    def apply_template_to_row(
        self,
        row_idx: int,
        template: MathTemplate,
        initial_values: Optional[List[str]] = None
    ) -> TemplateInstance:
        """Applies a mathematical template to Row `row_idx`."""
        if not (0 <= row_idx < len(self.rows)):
            row_idx = 0
        row = self.rows[row_idx]
        row.row_type = RowType.ADDEND
        inst = template.create_instance(initial_values)
        row.template_instance = inst
        self.cursor_row = row_idx
        self.cursor_slot = 0
        self.cursor_desc_col = 0
        self._target_is_slot = True
        return inst

    def add_description_column(self, slot_idx: Optional[int] = None) -> int:
        """Adds another descriptive column to the specified or active addend slot."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.ADDEND and row.template_instance:
            target_idx = slot_idx if slot_idx is not None else self.cursor_slot
            if 0 <= target_idx < len(row.template_instance.slots):
                slot = row.template_instance.slots[target_idx]
                col_num = len(slot.descriptions) + 1
                slot.add_description_field(field_type="custom", label=f"Context {col_num}")
                return len(slot.descriptions)
        return 2

    def extend_row_addition(self, row_idx: Optional[int] = None) -> bool:
        """
        Safely extends the addition sequence of Row `row_idx` by appending '+ □'
        outside existing groups, preserving all existing slots and UUIDs.
        """
        r_idx = row_idx if row_idx is not None else self.cursor_row
        if not (0 <= r_idx < len(self.rows)):
            return False
        row = self.rows[r_idx]
        if row.row_type != RowType.ADDEND or not row.template_instance:
            return False

        inst = row.template_instance
        cur_pat = inst.template.pattern.strip()
        new_pat = f"{cur_pat} + □"

        try:
            TemplateValidator.validate_addition_pattern(new_pat)
        except Exception:
            return False

        inst.append_addend_slot(new_pat)
        return True

    def add_row(self, row_type: RowType, explanation: str = "") -> int:
        """Explicitly creates a new row with designated row type."""
        if row_type == RowType.ALGEBRA_STEP:
            raise ValueError("Algebra steps are reserved for a future development stage and cannot be executed yet.")

        new_row = TemplateRow(row_type=row_type, explanation_text=explanation)
        self.rows.append(new_row)
        new_row_idx = len(self.rows) - 1
        self.cursor_row = new_row_idx
        self.cursor_slot = 0
        self.cursor_desc_col = 0
        self._target_is_slot = True
        return new_row_idx

    def input_number(self, val: str) -> None:
        """Inputs number string into the currently selected slot or cell."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.explanation_text = (row.explanation_text + val).strip()
            return

        if self.cursor_desc_col == 0:
            if row.template_instance and row.template_instance.slots:
                slot = row.template_instance.slots[self.cursor_slot]
                # Enforce valid numeric input for template slots (digits and single decimal point)
                if val.isdigit():
                    if slot.value == "0":
                        slot.value = val
                    else:
                        slot.value = slot.value + val
                elif val == ".":
                    if "." not in slot.value:
                        if not slot.value:
                            slot.value = "0."
                        else:
                            slot.value = slot.value + "."
                elif val.replace(".", "", 1).isdigit() and val.count(".") <= 1:
                    if not slot.value or slot.value == "0":
                        slot.value = val
                    else:
                        slot.value = slot.value + val
        else:
            if row.template_instance and row.template_instance.slots:
                slot = row.template_instance.slots[self.cursor_slot]
                desc_idx = self.cursor_desc_col - 1
                if 0 <= desc_idx < len(slot.descriptions):
                    slot.descriptions[desc_idx].value = (slot.descriptions[desc_idx].value + val).strip()

    def set_active_value(self, val: str) -> None:
        """Replaces the value of the currently selected slot or description cell."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.explanation_text = val
            return

        if row.template_instance and row.template_instance.slots:
            slot = row.template_instance.slots[self.cursor_slot]
            if self.cursor_desc_col == 0:
                if is_valid_number(val):
                    slot.value = val
                else:
                    # Non-numeric labels route to description columns of this slot
                    lower = val.lower().strip()
                    context_prefixes = ("in ", "on ", "at ", "under ", "with ", "near ", "inside ")
                    if any(lower.startswith(p) for p in context_prefixes):
                        slot.bound_context = val
                    else:
                        slot.bound_unit = val
            else:
                desc_idx = self.cursor_desc_col - 1
                if getattr(self, "_target_is_slot", True):
                    if 0 <= desc_idx < len(slot.descriptions):
                        slot.descriptions[desc_idx].value = val
                else:
                    while len(row.description_columns) <= desc_idx:
                        row.description_columns.append("")
                    row.description_columns[desc_idx] = val

    def backspace(self) -> None:
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.explanation_text = row.explanation_text[:-1]
            return

        if row.template_instance and row.template_instance.slots:
            slot = row.template_instance.slots[self.cursor_slot]
            if self.cursor_desc_col == 0:
                slot.value = slot.value[:-1]
            else:
                desc_idx = self.cursor_desc_col - 1
                if 0 <= desc_idx < len(slot.descriptions):
                    slot.descriptions[desc_idx].value = slot.descriptions[desc_idx].value[:-1]

    def get_editing_tokens(self) -> List[List[Token]]:
        """Returns non-validating editing tokens for all active addend rows."""
        return [row.to_editing_tokens() for row in self.rows if row.row_type == RowType.ADDEND]

    def delete_selected_column(self) -> None:
        """Deletes or clears the selected column or slot without deleting the entire row."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.explanation_text = ""
            return

        if row.template_instance and row.template_instance.slots:
            slot = row.template_instance.slots[self.cursor_slot]
            if self.cursor_desc_col == 0:
                slot.value = ""
            else:
                desc_idx = self.cursor_desc_col - 1
                if 0 <= desc_idx < len(slot.descriptions):
                    if len(slot.descriptions) > 2:
                        slot.descriptions.pop(desc_idx)
                        self.cursor_desc_col = min(self.cursor_desc_col, len(slot.descriptions))
                    else:
                        slot.descriptions[desc_idx].value = ""

    def clear(self) -> None:
        self.rows = [TemplateRow(row_type=RowType.ADDEND)]
        self.cursor_row = 0
        self.cursor_slot = 0
        self.cursor_desc_col = 0
        self._target_is_slot = True
        self.last_parse_result = None

    def calculate(self) -> Optional[ParseResult]:
        """Calculates global mathematical total across all active addend rows."""
        all_tokens: List[Token] = []

        for row in self.rows:
            if row.row_type != RowType.ADDEND:
                continue
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

        self.last_parse_result = TokenModelParser.parse_tokens(all_tokens)
        return self.last_parse_result


# -----------------------------------------------------------------------------
# Core AST and Legacy Token Model (Preserved)
# -----------------------------------------------------------------------------

@dataclass
class Token:
    """Represents a single token in the left-to-right statement."""
    value: str
    token_type: TokenType = field(default=TokenType.ITEM)
    explicit_type: bool = False
    slot_id: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.explicit_type:
            self.token_type = self.auto_classify(self.value)

    @classmethod
    def auto_classify(cls, val: str) -> TokenType:
        s = val.strip()
        if s == "□":
            return TokenType.UNKNOWN
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
    source_breakdown: List[str] = field(default_factory=list)

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
        groups: Dict[str, Dict] = {}
        order: List[str] = []

        for t in terms:
            lemma = WordSummerChatbot._lemmatize_word(t.item)
            try:
                val = Decimal(t.quantity)
            except Exception:
                val = Decimal(0)

            src_desc = f"{t.quantity} {t.item}"
            if t.context:
                src_desc += f" {t.context}"
            for ext in t.extra_contexts:
                if ext:
                    src_desc += f" {ext}"

            if lemma not in groups:
                groups[lemma] = {
                    "total": val,
                    "contexts": [t.context] if t.context else [],
                    "extra_contexts": list(t.extra_contexts),
                    "sources": [src_desc],
                    "raw_terms": [t],
                }
                order.append(lemma)
            else:
                groups[lemma]["total"] += val
                if t.context:
                    groups[lemma]["contexts"].append(t.context)
                for ext in t.extra_contexts:
                    if ext and ext not in groups[lemma]["extra_contexts"]:
                        groups[lemma]["extra_contexts"].append(ext)
                groups[lemma]["sources"].append(src_desc)
                groups[lemma]["raw_terms"].append(t)

        aggregated: List[SemanticTerm] = []
        for lemma in order:
            info = groups[lemma]
            total_val = info["total"]
            fmt = format(total_val, "f")
            if "." in fmt:
                fmt = fmt.rstrip("0").rstrip(".")
            if not fmt or fmt == "-0":
                fmt = "0"
            is_one = (total_val == Decimal(1))
            disp_item = WordSummerChatbot._pluralize_word(lemma, is_one)

            unique_contexts = list(dict.fromkeys(info["contexts"]))
            if len(unique_contexts) == 1 and len(info["raw_terms"]) == len(info["contexts"]):
                final_context = unique_contexts[0]
            else:
                final_context = ""

            aggregated.append(SemanticTerm(
                quantity=fmt,
                item=disp_item,
                context=final_context,
                extra_contexts=info["extra_contexts"] if not final_context else [],
                source_breakdown=info["sources"] if len(info["raw_terms"]) > 1 else [],
            ))

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

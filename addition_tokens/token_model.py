"""Token data model, AST, parser, and semantic binder for addition_tokens.

Preserves three representations of each addend:
1. Original ordered subcolumns (numbers, operators, parens, labels).
2. Parsed mathematical structure (unaggregated quantities attached to units/contexts).
3. Aggregated mathematical results grouped by compatible units.

Keeps structural precedence (visual column alignment) independent from
mathematical precedence (evaluation order and unit binding).
"""

from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from enum import Enum, auto
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
    """Distinguishes calculation rows from descriptive annotation rows."""
    ADDEND = auto()  # Active mathematical row contributing to calculation
    LABEL = auto()   # Pure descriptive/annotation row (does not contribute numbers)


@dataclass
class Token:
    """Represents a single token in the left-to-right statement."""
    value: str
    token_type: TokenType = field(default=TokenType.ITEM)
    explicit_type: bool = False  # Set True when user manually specifies the type

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

        # Prepositions typically indicate context/location phrases
        lower = s.lower()
        context_prefixes = ("in ", "on ", "at ", "under ", "with ", "near ", "inside ")
        if any(lower.startswith(prefix) for prefix in context_prefixes):
            return TokenType.CONTEXT

        # Default noun/item
        return TokenType.ITEM

    def set_type(self, new_type: TokenType) -> None:
        """Manually override or correct the token type."""
        self.token_type = new_type
        self.explicit_type = True


@dataclass
class Subcolumn:
    """Atomic subcolumn cell inside an addend column."""
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
    """Represents an individual labeled quantity before or after aggregation."""
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
    """
    Fulfills Refinement 1: Preserves three representations of each addend.
    1. ordered_subcolumns: Original entered subcolumns (numbers, operators, parens, labels).
    2. parsed_terms: Parsed mathematical structure (unaggregated quantities attached to units/contexts).
    3. aggregated_results: Aggregated mathematical results grouped by compatible units.
    """
    ordered_subcolumns: List[Subcolumn] = field(default_factory=list)
    parsed_terms: List[SemanticTerm] = field(default_factory=list)
    aggregated_results: List[SemanticTerm] = field(default_factory=list)
    raw_expression: str = ""
    total_number: str = ""

    def evaluate(self) -> None:
        """Parses and computes representations 2 and 3 from representation 1."""
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
    """Represents a row in the calculator grid."""
    row_type: RowType = RowType.ADDEND
    label_text: str = ""  # Used when row_type is RowType.LABEL
    addend_columns: List[AddendRepresentation] = field(default_factory=list)
    description_columns: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.row_type == RowType.ADDEND and not self.addend_columns:
            self.addend_columns.append(AddendRepresentation())


@dataclass
class ParseResult:
    """Complete result preserving both individual unaggregated terms and final result."""
    raw_expression: str
    total_number: str
    individual_terms: List[SemanticTerm]    # Unaggregated original labeled terms
    aggregated_terms: List[SemanticTerm]    # Combined/grouped terms
    word_result: str                        # Natural language summary sentence


class TokenModelParser:
    """Parser and semantic binder for lists of left-to-right Tokens."""

    @classmethod
    def validate_syntax(cls, tokens: List[Token]) -> None:
        """Validates parentheses, operators, operands, and token sequence."""
        if not tokens:
            raise ValueError("Expression is empty")

        # 1. Parentheses balance check
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

        # 2. Empty group check: ()
        for i in range(len(tokens) - 1):
            if (tokens[i].token_type == TokenType.GROUP_OPEN and
                    tokens[i + 1].token_type == TokenType.GROUP_CLOSE):
                raise ValueError(f"Empty group: '()' contains no operands at position {i + 1}")

        # 3. Math token stream validation (filtering down to math-affecting tokens)
        math_tokens: List[Tuple[int, Token]] = [
            (idx, tok) for idx, tok in enumerate(tokens)
            if tok.token_type in (TokenType.NUMBER, TokenType.OPERATOR, TokenType.GROUP_OPEN, TokenType.GROUP_CLOSE)
        ]

        if not any(tok.token_type == TokenType.NUMBER for _, tok in math_tokens):
            raise ValueError("Missing operands: statement contains no numbers")

        # Leading operator check
        if math_tokens and math_tokens[0][1].token_type == TokenType.OPERATOR:
            raise ValueError(f"Leading operator: expected operand before '+' at position {math_tokens[0][0] + 1}")

        # Trailing operator check
        if math_tokens and math_tokens[-1][1].token_type == TokenType.OPERATOR:
            raise ValueError(f"Trailing operator: expected operand after '+' at position {math_tokens[-1][0] + 1}")

        # Neighboring math tokens check
        for i in range(len(math_tokens) - 1):
            orig_idx, tok = math_tokens[i]
            next_orig_idx, next_tok = math_tokens[i + 1]

            # Consecutive operators: + +
            if tok.token_type == TokenType.OPERATOR and next_tok.token_type == TokenType.OPERATOR:
                raise ValueError(f"Consecutive operators: '+' cannot follow '+' at position {next_orig_idx + 1}")

            # Operator directly after open paren: ( +
            if tok.token_type == TokenType.GROUP_OPEN and next_tok.token_type == TokenType.OPERATOR:
                raise ValueError(f"Missing operand before '+' inside group at position {next_orig_idx + 1}")

            # Operator directly before close paren: + )
            if tok.token_type == TokenType.OPERATOR and next_tok.token_type == TokenType.GROUP_CLOSE:
                raise ValueError(f"Missing operand after '+' inside group at position {orig_idx + 1}")

            # Missing operator: number followed by number without operator in between
            if tok.token_type == TokenType.NUMBER and next_tok.token_type == TokenType.NUMBER:
                raise ValueError(f"Missing operator between numbers at positions {orig_idx + 1} and {next_orig_idx + 1}")

    @classmethod
    def parse_tokens(cls, tokens: List[Token]) -> ParseResult:
        """
        Parses tokens, applies context distribution rules, preserves individual
        labeled quantities, and computes exact mathematical and verbal results.
        """
        cls.validate_syntax(tokens)

        # Build raw mathematical expression string for exact decimal evaluator
        math_parts: List[str] = []
        for tok in tokens:
            if tok.token_type == TokenType.NUMBER:
                math_parts.append(tok.value)
            elif tok.token_type in (TokenType.OPERATOR, TokenType.GROUP_OPEN, TokenType.GROUP_CLOSE):
                math_parts.append(tok.value)

        expr_str = " ".join(math_parts)
        total_number = evaluate_addition(expr_str)

        # Parse semantic terms with groups and context distribution
        individual_terms = cls._extract_semantic_terms(tokens)

        # Validate that every quantity has an item label (do not guess missing items)
        for term in individual_terms:
            if not term.item.strip():
                raise ValueError(f"Unlabeled quantity: '{term.quantity}' has no item label")

        # Synthesize final word description using WordSummerChatbot
        items_for_chatbot = [
            (t.quantity, t.item, t.context, *t.extra_contexts)
            for t in individual_terms
        ]
        word_result = WordSummerChatbot.summarize(items_for_chatbot, total_number)

        # Prefix total quantity if the summary phrase doesn't already start with a number
        if word_result and not re.match(r"^\d", word_result.strip()):
            word_result = f"{total_number} {word_result}"

        # Also create aggregated terms grouped by item/context for inspection
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
        """
        Extracts individual labeled quantities preserving left-to-right binding
        and distributing group context without silently overwriting inner contexts.
        """
        # Intermediate structure representing a parsed quantity term
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

        # We keep track of groups: group_id -> list of draft term indices in that group
        group_members: Dict[int, List[int]] = {}

        # Trailing labels map: group_id -> (trailing_item, trailing_context, trailing_extras)
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

                # Consume immediately following ITEM or CONTEXT tokens (Left-Binding)
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
                # If these follow a closed group, associate them with the closed group
                if last_closed_group is not None:
                    # Gather all trailing labels for this closed group
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

                # Free floating item or context attached to previous draft term if any
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

        # Now apply Distributive Context Rules from groups
        # For each closed group with trailing labels:
        for gid, (t_item, t_ctx, t_extras) in trailing_group_labels.items():
            member_indices = group_members.get(gid, [])
            for idx in member_indices:
                member = drafts[idx]
                # If member has no item inside, inherit the group's trailing item
                if not member.item and t_item:
                    member.item = t_item

                # If member has no context inside, inherit group context
                # CRITICAL REFINEMENT: Do NOT overwrite if member already has context!
                if not member.context and t_ctx:
                    member.context = t_ctx
                elif member.context and t_ctx and t_ctx not in member.extra_contexts:
                    member.extra_contexts.append(t_ctx)

                if t_extras:
                    for ext in t_extras:
                        if ext not in member.extra_contexts:
                            member.extra_contexts.append(ext)

        # Convert drafts into SemanticTerms, normalizing singular/plural for 1 vs many
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
        """Groups terms with identical items and contexts together into summed totals."""
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
    Manages the 2D grid of Addend and Label rows, navigation cursor,
    centralized inputs, and mathematical evaluation.
    """

    def __init__(self) -> None:
        self.rows: List[GridRow] = [GridRow(row_type=RowType.ADDEND)]
        # Cursor tracking
        self.cursor_row: int = 0
        self.cursor_area: str = "addend"  # "addend" or "description"
        self.cursor_addend_col: int = 0
        self.cursor_subcol: int = 0
        self.cursor_desc_col: int = 0
        self.last_parse_result: Optional[ParseResult] = None

    def get_max_addend_columns(self) -> int:
        """Returns the maximum number of addend columns across all addend rows (for visual push-over)."""
        counts = [len(r.addend_columns) for r in self.rows if r.row_type == RowType.ADDEND]
        return max(counts) if counts else 1

    # Navigation Actions: Next Subcolumn, Next Column, Next Addend
    def next_subcolumn(self) -> Tuple[int, int, int]:
        """Advances cursor to the next subcolumn inside the current addend column."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            return self.cursor_row, 0, 0

        self.cursor_area = "addend"
        self.cursor_subcol += 1
        return self.cursor_row, self.cursor_addend_col, self.cursor_subcol

    def next_column(self) -> Tuple[int, str, int]:
        """Advances to the next main column in the same row."""
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
        """Completes current row and drops down to create a new Addend Row at Column 1, Subcolumn 0."""
        new_row = GridRow(row_type=RowType.ADDEND)
        self.rows.append(new_row)
        self.cursor_row = len(self.rows) - 1
        self.cursor_area = "addend"
        self.cursor_addend_col = 0
        self.cursor_subcol = 0
        self.cursor_desc_col = 0
        return self.cursor_row

    def add_label_row(self, text: str = "") -> int:
        """Explicitly adds a separate descriptive/annotation Label Row."""
        new_row = GridRow(row_type=RowType.LABEL, label_text=text)
        self.rows.append(new_row)
        self.cursor_row = len(self.rows) - 1
        self.cursor_area = "label"
        return self.cursor_row

    def input_value(self, val: str, token_type: Optional[TokenType] = None) -> Subcolumn:
        """Feeds a value from the central keypad into the active cell/subcolumn."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.label_text = (row.label_text + " " + val).strip()
            return Subcolumn(value=row.label_text, token_type=TokenType.CONTEXT)

        if self.cursor_area == "description":
            if self.cursor_desc_col >= len(row.description_columns):
                row.description_columns.append(val)
            else:
                row.description_columns[self.cursor_desc_col] = val
            return Subcolumn(value=val, token_type=TokenType.CONTEXT)

        # Addend area: feed into subcolumns
        addend = row.addend_columns[self.cursor_addend_col]
        subcol = Subcolumn(value=val)
        if token_type is not None:
            subcol.token_type = token_type
            subcol.explicit_type = True

        if self.cursor_subcol >= len(addend.ordered_subcolumns):
            addend.ordered_subcolumns.append(subcol)
            self.cursor_subcol = len(addend.ordered_subcolumns) - 1
        else:
            addend.ordered_subcolumns[self.cursor_subcol] = subcol

        return subcol

    def backspace(self) -> None:
        """Deletes the active subcolumn or character."""
        row = self.rows[self.cursor_row]
        if row.row_type == RowType.LABEL:
            row.label_text = row.label_text[:-1]
            return

        if self.cursor_area == "addend":
            addend = row.addend_columns[self.cursor_addend_col]
            if addend.ordered_subcolumns:
                idx = min(self.cursor_subcol, len(addend.ordered_subcolumns) - 1)
                addend.ordered_subcolumns.pop(idx)
                if self.cursor_subcol > 0:
                    self.cursor_subcol -= 1

    def clear(self) -> None:
        """Resets the grid model to an initial empty Addend Row."""
        self.rows = [GridRow(row_type=RowType.ADDEND)]
        self.cursor_row = 0
        self.cursor_area = "addend"
        self.cursor_addend_col = 0
        self.cursor_subcol = 0
        self.cursor_desc_col = 0
        self.last_parse_result = None

    def calculate(self) -> Optional[ParseResult]:
        """
        Evaluates each addend column to populate the 3 representations,
        and computes global calculation across all active addend rows.
        Label rows are ignored during mathematical calculation.
        """
        all_tokens: List[Token] = []

        for row in self.rows:
            if row.row_type != RowType.ADDEND:
                continue  # Label rows do not contribute mathematical terms

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

            # Append trailing description column tokens for this row
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

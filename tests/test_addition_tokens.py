"""Comprehensive test suite for addition_tokens prototype.

Tests:
1. Numeric token validation (re.fullmatch and Decimal).
2. Token classification and manual override (explicit_type).
3. Syntax validation (unmatched parens, empty groups, consecutive/missing operators, unlabeled quantities).
4. Semantic binding and unaggregated term retention:
   - (1 + 2) pens in the drawer -> preserves unaggregated terms + calculates 3 pens in the drawer.
   - (1 pen in the drawer + 2 pens on the desk) -> 3 pens (1 in the drawer, 2 on the desk).
   - (1 pen + 2 books) in the drawer -> separates categories while distributing context.
   - Context distribution without silent overwrite of inner contexts.
5. Refinement 1: Three representations of each addend (ordered subcolumns, parsed structure, aggregated results).
6. Refinement 2: Independent structural and mathematical precedence (visual push-over without modifying math).
7. Central keypad and navigation actions: Next Subcolumn (→), Next Column (⇒), Next Addend (↓).
8. Row classification: Addend rows vs. Label rows.
9. Clean display cells free of permanent dropdowns.
10. Clickable cell selection, delete column control, and safe GUI error handling (Problem 1 & 2 fixes).
"""

from decimal import Decimal
import os
from pathlib import Path
import sys
import tkinter as tk
from tkinter import ttk
import unittest

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from addition_tokens.token_model import (
    Token,
    TokenType,
    RowType,
    Subcolumn,
    SemanticTerm,
    AddendRepresentation,
    GridRow,
    ParseResult,
    TokenModelParser,
    TokenGridModel,
    SlotMetadata,
    TemplateSlot,
    MathTemplate,
    TemplateValidator,
    ExpressionTemplateParser,
    MathTemplateManager,
    TemplateInstance,
    TemplateRow,
    TemplateGridModel,
    is_valid_number,
)
from addition_tokens.addition import AdditionTokenCalculator


class TestNumberValidation(unittest.TestCase):
    """Test precise numeric validation using re.fullmatch and Decimal."""

    def test_valid_integers(self):
        self.assertTrue(is_valid_number("0"))
        self.assertTrue(is_valid_number("1"))
        self.assertTrue(is_valid_number("42"))
        self.assertTrue(is_valid_number("1000"))

    def test_valid_decimals(self):
        self.assertTrue(is_valid_number("0.5"))
        self.assertTrue(is_valid_number(".75"))
        self.assertTrue(is_valid_number("3.14159"))
        self.assertTrue(is_valid_number("10."))

    def test_invalid_strings(self):
        self.assertFalse(is_valid_number(""))
        self.assertFalse(is_valid_number("   "))
        self.assertFalse(is_valid_number("abc"))
        self.assertFalse(is_valid_number("1a"))
        self.assertFalse(is_valid_number("1..2"))
        self.assertFalse(is_valid_number("."))
        self.assertFalse(is_valid_number("1+2"))
        self.assertFalse(is_valid_number(None))


class TestTokenClassification(unittest.TestCase):
    """Test auto-classification and manual user correction."""

    def test_auto_classification(self):
        self.assertEqual(Token("(").token_type, TokenType.GROUP_OPEN)
        self.assertEqual(Token(")").token_type, TokenType.GROUP_CLOSE)
        self.assertEqual(Token("+").token_type, TokenType.OPERATOR)
        self.assertEqual(Token("5").token_type, TokenType.NUMBER)
        self.assertEqual(Token("12.5").token_type, TokenType.NUMBER)
        self.assertEqual(Token("pens").token_type, TokenType.ITEM)
        self.assertEqual(Token("in the drawer").token_type, TokenType.CONTEXT)
        self.assertEqual(Token("on the desk").token_type, TokenType.CONTEXT)

    def test_manual_type_override(self):
        tok = Token("5")
        self.assertEqual(tok.token_type, TokenType.NUMBER)
        self.assertFalse(tok.explicit_type)

        # Manually set to ITEM (e.g. model "5" as an item name)
        tok.set_type(TokenType.ITEM)
        self.assertEqual(tok.token_type, TokenType.ITEM)
        self.assertTrue(tok.explicit_type)

    def test_token_type_from_str(self):
        self.assertEqual(TokenType.from_str("number"), TokenType.NUMBER)
        self.assertEqual(TokenType.from_str("item"), TokenType.ITEM)
        self.assertEqual(TokenType.from_str("context"), TokenType.CONTEXT)
        self.assertEqual(TokenType.from_str("+"), TokenType.OPERATOR)
        self.assertEqual(TokenType.from_str("("), TokenType.GROUP_OPEN)
        self.assertEqual(TokenType.from_str(")"), TokenType.GROUP_CLOSE)


class TestTokenSyntaxValidation(unittest.TestCase):
    """Test strict validation for unmatched parens, empty groups, missing operands, etc."""

    def test_empty_tokens(self):
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax([])
        self.assertIn("empty", str(ctx.exception).lower())

    def test_unmatched_open_parenthesis(self):
        tokens = [
            Token("("), Token("1"), Token("pen"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("closing parenthesis", str(ctx.exception).lower())

    def test_unmatched_close_parenthesis(self):
        tokens = [
            Token("1"), Token("pen"), Token(")"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("unmatched closing", str(ctx.exception).lower())

    def test_empty_group(self):
        tokens = [
            Token("("), Token(")"), Token("pens"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("empty group", str(ctx.exception).lower())

    def test_missing_operands(self):
        tokens = [
            Token("pens"), Token("in the drawer"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("missing operands", str(ctx.exception).lower())

    def test_leading_operator(self):
        tokens = [
            Token("+"), Token("1"), Token("pen"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("leading operator", str(ctx.exception).lower())

    def test_trailing_operator(self):
        tokens = [
            Token("1"), Token("pen"), Token("+"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("trailing operator", str(ctx.exception).lower())

    def test_consecutive_operators(self):
        tokens = [
            Token("1"), Token("pen"), Token("+"), Token("+"), Token("2"), Token("pens"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("consecutive operators", str(ctx.exception).lower())

    def test_operator_directly_after_open_paren(self):
        tokens = [
            Token("("), Token("+"), Token("1"), Token("pen"), Token(")"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("missing operand before '+'", str(ctx.exception).lower())

    def test_operator_directly_before_close_paren(self):
        tokens = [
            Token("("), Token("1"), Token("pen"), Token("+"), Token(")"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("missing operand after '+'", str(ctx.exception).lower())

    def test_missing_operator_between_numbers(self):
        tokens = [
            Token("1"), Token("pen"), Token("2"), Token("pens"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.validate_syntax(tokens)
        self.assertIn("missing operator", str(ctx.exception).lower())

    def test_unlabeled_quantity_rejected(self):
        # 1 + 2 without item label must raise error (do not silently guess labels!)
        tokens = [
            Token("1"), Token("+"), Token("2"),
        ]
        with self.assertRaises(ValueError) as ctx:
            TokenModelParser.parse_tokens(tokens)
        self.assertIn("unlabeled quantity", str(ctx.exception).lower())


class TestSemanticBindingAndAST(unittest.TestCase):
    """Test AST context distribution and unaggregated term retention."""

    def test_group_with_trailing_item_and_context(self):
        # (1 + 2) pens in the drawer -> 3 pens in the drawer
        tokens = [
            Token("("), Token("1"), Token("+"), Token("2"), Token(")"),
            Token("pens"), Token("in the drawer"),
        ]
        res = TokenModelParser.parse_tokens(tokens)

        # 1. Math total
        self.assertEqual(res.total_number, "3")

        # 2. Individual unaggregated terms preserved!
        self.assertEqual(len(res.individual_terms), 2)
        term1, term2 = res.individual_terms
        self.assertEqual(term1.quantity, "1")
        self.assertEqual(term1.item, "pen")
        self.assertEqual(term1.context, "in the drawer")

        self.assertEqual(term2.quantity, "2")
        self.assertEqual(term2.item, "pens")
        self.assertEqual(term2.context, "in the drawer")

        # 3. Aggregated terms
        self.assertEqual(len(res.aggregated_terms), 1)
        self.assertEqual(res.aggregated_terms[0].quantity, "3")
        self.assertEqual(res.aggregated_terms[0].item, "pens")
        self.assertEqual(res.aggregated_terms[0].context, "in the drawer")

        # 4. Word summary
        self.assertEqual(res.word_result, "3 pens in the drawer")

    def test_group_with_internal_distinct_contexts(self):
        # (1 pen in the drawer + 2 pens on the desk) -> 3 pens (1 in the drawer, 2 on the desk)
        tokens = [
            Token("("),
            Token("1"), Token("pen"), Token("in the drawer"),
            Token("+"),
            Token("2"), Token("pens"), Token("on the desk"),
            Token(")"),
        ]
        res = TokenModelParser.parse_tokens(tokens)

        self.assertEqual(res.total_number, "3")
        self.assertEqual(len(res.individual_terms), 2)
        self.assertEqual(res.individual_terms[0].context, "in the drawer")
        self.assertEqual(res.individual_terms[1].context, "on the desk")
        self.assertIn("3 pens", res.word_result)
        self.assertIn("1 in the drawer", res.word_result)
        self.assertIn("2 on the desk", res.word_result)

    def test_group_with_multiple_categories_and_shared_context(self):
        # (1 pen + 2 books) in the drawer -> keeps categories separate while applying location to both
        tokens = [
            Token("("),
            Token("1"), Token("pen"),
            Token("+"),
            Token("2"), Token("books"),
            Token(")"),
            Token("in the drawer"),
        ]
        res = TokenModelParser.parse_tokens(tokens)

        self.assertEqual(res.total_number, "3")
        self.assertEqual(len(res.individual_terms), 2)
        self.assertEqual(res.individual_terms[0].item, "pen")
        self.assertEqual(res.individual_terms[0].context, "in the drawer")
        self.assertEqual(res.individual_terms[1].item, "books")
        self.assertEqual(res.individual_terms[1].context, "in the drawer")

        # Both categories retain "in the drawer"
        self.assertIn("1 pen in the drawer", res.word_result)
        self.assertIn("2 books in the drawer", res.word_result)

    def test_inner_contexts_not_overwritten_by_trailing_context(self):
        # (1 pen in the drawer + 2 pens on the desk) in the room
        # "in the drawer" and "on the desk" must NOT be silently overwritten!
        tokens = [
            Token("("),
            Token("1"), Token("pen"), Token("in the drawer"),
            Token("+"),
            Token("2"), Token("pens"), Token("on the desk"),
            Token(")"),
            Token("in the room"),
        ]
        res = TokenModelParser.parse_tokens(tokens)

        self.assertEqual(res.individual_terms[0].context, "in the drawer")
        self.assertEqual(res.individual_terms[1].context, "on the desk")
        # Trailing context placed in extra_contexts rather than overwriting
        self.assertIn("in the room", res.individual_terms[0].extra_contexts)
        self.assertIn("in the room", res.individual_terms[1].extra_contexts)


class TestRefinement1ThreeAddendRepresentations(unittest.TestCase):
    """Test Refinement 1: Each addend retains three distinct representations."""

    def test_three_representations_single_addend(self):
        # Representation 1: Ordered subcolumns
        subcols = [
            Subcolumn("("),
            Subcolumn("1"),
            Subcolumn("pen"),
            Subcolumn("+"),
            Subcolumn("2"),
            Subcolumn("pens"),
            Subcolumn(")"),
        ]
        addend = AddendRepresentation(ordered_subcolumns=subcols)
        addend.evaluate()

        # Rep 1: Ordered subcolumns preserved!
        self.assertEqual(len(addend.ordered_subcolumns), 7)
        self.assertEqual([s.value for s in addend.ordered_subcolumns], ["(", "1", "pen", "+", "2", "pens", ")"])

        # Rep 2: Parsed mathematical structure with individual unaggregated terms
        self.assertEqual(len(addend.parsed_terms), 2)
        self.assertEqual(addend.parsed_terms[0].quantity, "1")
        self.assertEqual(addend.parsed_terms[0].item, "pen")
        self.assertEqual(addend.parsed_terms[1].quantity, "2")
        self.assertEqual(addend.parsed_terms[1].item, "pens")

        # Rep 3: Aggregated mathematical results grouped by compatible units
        self.assertEqual(len(addend.aggregated_results), 1)
        self.assertEqual(addend.aggregated_results[0].quantity, "3")
        self.assertEqual(addend.aggregated_results[0].item, "pens")
        self.assertEqual(addend.total_number, "3")

    def test_three_representations_different_units_never_combined(self):
        # (1 pen + 2 books) -> Rep 3 must keep pen and books separate!
        subcols = [
            Subcolumn("("),
            Subcolumn("1"),
            Subcolumn("pen"),
            Subcolumn("+"),
            Subcolumn("2"),
            Subcolumn("books"),
            Subcolumn(")"),
        ]
        addend = AddendRepresentation(ordered_subcolumns=subcols)
        addend.evaluate()

        self.assertEqual(len(addend.ordered_subcolumns), 7)
        self.assertEqual(len(addend.parsed_terms), 2)
        # Aggregated results maintain separate unit totals
        self.assertEqual(len(addend.aggregated_results), 2)
        self.assertEqual(addend.aggregated_results[0].quantity, "1")
        self.assertEqual(addend.aggregated_results[0].item, "pen")
        self.assertEqual(addend.aggregated_results[1].quantity, "2")
        self.assertEqual(addend.aggregated_results[1].item, "books")


class TestRefinement2PrecedenceAndGridModel(unittest.TestCase):
    """Test Refinement 2: Independent structural and mathematical precedence."""

    def test_structural_push_over_does_not_affect_math(self):
        model = TokenGridModel()

        # Row 1: Addend Column 1: 1 pen in the drawer
        model.input_value("1")
        model.next_subcolumn()
        model.input_value("pen")
        model.next_column()  # Move to Description
        model.cursor_area = "description"
        model.input_value("in the drawer")

        # Row 2: Addend Column 1 and Addend Column 2 (expanding math columns)
        model.next_addend()
        model.input_value("2")
        model.next_subcolumn()
        model.input_value("pens")

        # Add second addend column in Row 2
        model.next_column()
        model.input_value("3")
        model.next_subcolumn()
        model.input_value("pens")

        # Max addend columns is now 2
        self.assertEqual(model.get_max_addend_columns(), 2)

        # Calculate: Row 1 has 1 pen, Row 2 has 2 pens + 3 pens = 5 pens
        # Total = 6 pens
        res = model.calculate()
        self.assertIsNotNone(res)
        self.assertEqual(res.total_number, "6")
        self.assertIn("pens", res.word_result)

    def test_separate_addend_and_label_row_types(self):
        model = TokenGridModel()

        # Row 1: Addend row with 1 pen
        model.input_value("1")
        model.next_subcolumn()
        model.input_value("pen")

        # Row 2: Pure Label row (annotation)
        model.add_label_row("Experiment Note: Day 1 Observations")

        # Row 3: Addend row with 2 pens
        model.next_addend()
        model.input_value("2")
        model.next_subcolumn()
        model.input_value("pens")

        # Calculate: Label row must not contribute numbers or zeros
        res = model.calculate()
        self.assertIsNotNone(res)
        self.assertEqual(res.total_number, "3")
        self.assertEqual(res.word_result, "3 pens")


class TestKeypadNavigationControls(unittest.TestCase):
    """Test the three explicit keypad navigation actions."""

    def test_next_subcolumn_navigation(self):
        model = TokenGridModel()
        self.assertEqual(model.cursor_subcol, 0)

        model.input_value("1")
        model.next_subcolumn()
        self.assertEqual(model.cursor_subcol, 1)

        model.input_value("pen")
        model.next_subcolumn()
        self.assertEqual(model.cursor_subcol, 2)

    def test_next_column_navigation(self):
        model = TokenGridModel()
        self.assertEqual(model.cursor_addend_col, 0)

        # Move to next main column in the same row
        model.next_column()
        self.assertEqual(model.cursor_addend_col, 1)
        self.assertEqual(len(model.rows[0].addend_columns), 2)

    def test_next_addend_navigation(self):
        model = TokenGridModel()
        self.assertEqual(len(model.rows), 1)

        new_row_idx = model.next_addend()
        self.assertEqual(new_row_idx, 1)
        self.assertEqual(len(model.rows), 2)
        self.assertEqual(model.cursor_row, 1)
        self.assertEqual(model.cursor_addend_col, 0)
        self.assertEqual(model.cursor_subcol, 0)


class TestAdditionTokenCalculatorGUI(unittest.TestCase):
    """Test Tkinter GUI prototype and automated button interactions."""

    @classmethod
    def setUpClass(cls):
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
            cls.gui_available = True
        except Exception:
            cls.gui_available = False

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, "gui_available", False) and hasattr(cls, "root"):
            try:
                cls.root.destroy()
            except Exception:
                pass

    def setUp(self):
        if not self.gui_available:
            self.skipTest("Tkinter display not available")
        import tempfile
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.app = AdditionTokenCalculator(root=self.root, mode="legacy_subcolumn")
        self.app.template_manager.storage_file = Path(self.tmp_dir.name) / "custom_templates.json"

    def tearDown(self):
        self.app.clear()
        if hasattr(self, "tmp_dir"):
            self.tmp_dir.cleanup()

    def test_keypad_anchoring_and_button_zero(self):
        # Keypad must be packed at bottom container
        self.assertIn("0", self.app.keypad_buttons)
        btn_0 = self.app.keypad_buttons["0"]
        self.root.update_idletasks()

        # Initial geometry of 0 button
        info_initial = btn_0.grid_info()
        self.assertEqual(int(info_initial["row"]), 4)
        self.assertEqual(int(info_initial["column"]), 0)

        # Add 5 more addend rows
        for _ in range(5):
            self.app.add_addend_row()
        self.root.update_idletasks()

        # Button 0 grid positioning remains exactly the same
        info_after = btn_0.grid_info()
        self.assertEqual(int(info_after["row"]), 4)
        self.assertEqual(int(info_after["column"]), 0)

    def test_clean_display_cells_without_permanent_dropdowns(self):
        # Verify that grid_frame does not use ttk.Combobox inside display cells
        self.app.add_token(0, "1")
        self.app.add_token(0, "pen")
        self.root.update_idletasks()

        def get_all_widgets(parent):
            widgets = []
            for child in parent.winfo_children():
                widgets.append(child)
                widgets.extend(get_all_widgets(child))
            return widgets

        grid_widgets = get_all_widgets(self.app.grid_frame)
        comboboxes = [w for w in grid_widgets if isinstance(w, ttk.Combobox)]
        # All display cells are clean labels, NOT permanent dropdown comboboxes!
        self.assertEqual(len(comboboxes), 0)

    def test_single_row_parentheses_flow(self):
        # ( 1 + 2 ) pens in the drawer
        tokens_to_add = ["(", "1", "+", "2", ")", "pens", "in the drawer"]
        for t in tokens_to_add:
            self.app.add_token(0, t)

        res = self.app.calculate()
        self.assertIsNotNone(res)
        self.assertEqual(self.app.result_var.get(), "3")
        self.assertEqual(self.app.result_word_var.get(), "3 pens in the drawer")

        # Verify inspector text contains the three representations
        inspector_content = self.app.inspector_text.get("1.0", "end")
        self.assertIn("Rep 1 (Ordered Subcolumns)", inspector_content)
        self.assertIn("Rep 2 (Parsed Structure - Unaggregated)", inspector_content)
        self.assertIn("Rep 3 (Aggregated Results by Units)", inspector_content)
        self.assertIn("Quantity: 1, Unit: 'pen'", inspector_content)
        self.assertIn("Quantity: 2, Unit: 'pens'", inspector_content)

    def test_multiple_rows_addition(self):
        # Row 1: 1 pen in the drawer
        self.app.add_token(0, "1")
        self.app.add_token(0, "pen")
        self.app.add_token(0, "in the drawer")

        # Row 2 explicitly created via + Addend
        row2 = self.app.add_addend_row()
        self.assertEqual(row2, 1)
        self.app.add_token(1, "2")
        self.app.add_token(1, "pens")
        self.app.add_token(1, "in the drawer")

        res = self.app.calculate()
        self.assertIsNotNone(res)
        self.assertEqual(self.app.result_var.get(), "3")
        self.assertEqual(self.app.result_word_var.get(), "3 pens in the drawer")

    def test_manual_type_correction_in_gui(self):
        # Add a number token and override it to ITEM
        tok = self.app.add_token(0, "5")
        self.assertEqual(tok.token_type, TokenType.NUMBER)

        self.app.set_token_type(0, 0, TokenType.ITEM)
        self.assertEqual(self.app.grid_model.rows[0].addend_columns[0].ordered_subcolumns[0].token_type, TokenType.ITEM)
        self.assertTrue(self.app.grid_model.rows[0].addend_columns[0].ordered_subcolumns[0].explicit_type)

    def test_operator_does_not_auto_create_row_or_column(self):
        # Pressing '+' should add a token to the current row, NOT create a new row
        initial_row_count = len(self.app.rows_tokens)
        self.app._on_keypad_press("+")
        self.assertEqual(len(self.app.rows_tokens), initial_row_count)
        self.assertEqual(len(self.app.rows_tokens[0]), 1)
        self.assertEqual(self.app.rows_tokens[0][0].value, "+")

    def test_clear_button(self):
        self.app.add_token(0, "1")
        self.app.add_token(0, "pen")
        self.app.calculate()
        self.assertEqual(self.app.result_var.get(), "1")

        self.app.clear()
        self.assertEqual(self.app.result_var.get(), "")
        self.assertEqual(self.app.result_word_var.get(), "")
        self.assertEqual(len(self.app.rows_tokens), 1)
        self.assertEqual(len(self.app.rows_tokens[0]), 0)


class TestClickableCellsAndSafeErrorHandling(unittest.TestCase):
    """
    Tests for Problem 1 & Problem 2 fixes:
    - Clickable cell selection and editing earlier columns.
    - Keypad inputs go strictly to the selected cell without shifting.
    - Delete Selected Column without removing the addend row.
    - Safe GUI exception boundary on parser errors (unlabeled quantities).
    - Recovering from validation error by selecting cell and recalculating.
    """

    @classmethod
    def setUpClass(cls):
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
            cls.gui_available = True
        except Exception:
            cls.gui_available = False

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, "gui_available", False) and hasattr(cls, "root"):
            try:
                cls.root.destroy()
            except Exception:
                pass

    def setUp(self):
        if not self.gui_available:
            self.skipTest("Tkinter display not available")
        import tempfile
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.app = AdditionTokenCalculator(root=self.root, mode="legacy_subcolumn")
        self.app.template_manager.storage_file = Path(self.tmp_dir.name) / "custom_templates.json"

    def tearDown(self):
        self.app.clear()
        if hasattr(self, "tmp_dir"):
            self.tmp_dir.cleanup()

    def test_create_multiple_empty_columns_then_fill_earlier_column(self):
        # Press Next Col (⇒) twice to create multiple empty columns
        self.app._on_keypad_press("Next Col (⇒)")
        self.app._on_keypad_press("Next Col (⇒)")
        self.root.update_idletasks()

        row = self.app.grid_model.rows[0]
        self.assertEqual(len(row.addend_columns), 3)

        # Now click and select Main Column 1 (index 0)
        self.app.select_cell(0, "addend", 0, 0)
        self.assertEqual(self.app.grid_model.cursor_addend_col, 0)

        # Feed input to Column 1
        self.app._on_keypad_press("1")
        self.app._on_keypad_press("Next Subcol (→)")
        self.app._on_vocab_click("pen", TokenType.ITEM)

        # Confirm Column 1 has the values while Column 2 and 3 remain empty
        self.assertEqual(len(row.addend_columns[0].ordered_subcolumns), 2)
        self.assertEqual(row.addend_columns[0].ordered_subcolumns[0].value, "1")
        self.assertEqual(row.addend_columns[0].ordered_subcolumns[1].value, "pen")
        self.assertEqual(len(row.addend_columns[1].ordered_subcolumns), 0)
        self.assertEqual(len(row.addend_columns[2].ordered_subcolumns), 0)

    def test_click_earlier_column_and_edit_it(self):
        # Populate column 1 and column 2
        self.app.add_token(0, "1")
        self.app._on_keypad_press("Next Subcol (→)")
        self.app._on_vocab_click("pen", TokenType.ITEM)

        # Advance to Col 2
        self.app._on_keypad_press("Next Col (⇒)")
        self.app._on_keypad_press("2")
        self.app._on_keypad_press("Next Subcol (→)")
        self.app._on_vocab_click("pens", TokenType.ITEM)

        # Now click back to Column 1, Subcolumn 0 (the '1') and edit it to '5'
        self.app.select_cell(0, "addend", 0, 0)
        self.app._on_keypad_press("5")

        row = self.app.grid_model.rows[0]
        self.assertEqual(row.addend_columns[0].ordered_subcolumns[0].value, "5")
        # Column 2 remains untouched!
        self.assertEqual(row.addend_columns[1].ordered_subcolumns[0].value, "2")

    def test_keypad_sends_input_only_to_selected_column(self):
        # Create 2 columns
        self.app._on_keypad_press("Next Col (⇒)")
        # Select column 2
        self.app.select_cell(0, "addend", 1, 0)
        self.app._on_keypad_press("9")

        row = self.app.grid_model.rows[0]
        self.assertEqual(len(row.addend_columns[0].ordered_subcolumns), 0)
        self.assertEqual(len(row.addend_columns[1].ordered_subcolumns), 1)
        self.assertEqual(row.addend_columns[1].ordered_subcolumns[0].value, "9")

    def test_delete_selected_column_leaves_addend_intact(self):
        # Create 2 columns in row 1
        self.app.add_token(0, "1")
        self.app._on_keypad_press("Next Col (⇒)")
        self.app.add_token(0, "2")
        self.root.update_idletasks()

        row = self.app.grid_model.rows[0]
        self.assertEqual(len(row.addend_columns), 2)

        # Select column 2 and delete it
        self.app.select_cell(0, "addend", 1, 0)
        self.app.delete_selected_column()

        # The row must still exist!
        self.assertEqual(len(self.app.grid_model.rows), 1)
        self.assertEqual(len(self.app.grid_model.rows[0].addend_columns), 1)
        self.assertEqual(self.app.grid_model.rows[0].addend_columns[0].ordered_subcolumns[0].value, "1")

        # Now delete the last remaining column: addend row is NOT deleted, just reset to empty!
        self.app.select_cell(0, "addend", 0, 0)
        self.app.delete_selected_column()
        self.assertEqual(len(self.app.grid_model.rows), 1)
        self.assertEqual(len(self.app.grid_model.rows[0].addend_columns), 1)
        self.assertEqual(len(self.app.grid_model.rows[0].addend_columns[0].ordered_subcolumns), 0)

    def test_delete_selected_subcolumn_leaves_addend_intact(self):
        # 1 + 2
        self.app.add_token(0, "1")
        self.app.add_token(0, "+")
        self.app.add_token(0, "2")

        addend = self.app.grid_model.rows[0].addend_columns[0]
        self.assertEqual(len(addend.ordered_subcolumns), 3)

        # Select subcolumn 1 ('+') and delete it
        self.app.select_cell(0, "addend", 0, 1)
        self.app.grid_model.delete_selected_subcolumn()

        # Addend column and row remain intact, now has 2 subcolumns ['1', '2']
        self.assertEqual(len(self.app.grid_model.rows), 1)
        self.assertEqual(len(addend.ordered_subcolumns), 2)
        self.assertEqual([sc.value for sc in addend.ordered_subcolumns], ["1", "2"])

    def test_selection_highlighting_and_status_label(self):
        self.app.add_token(0, "1")
        self.app._on_keypad_press("Next Subcol (→)")
        self.app._on_vocab_click("pen", TokenType.ITEM)
        self.root.update_idletasks()

        # Select subcolumn 1 ('pen')
        self.app.select_cell(0, "addend", 0, 1)
        status_text = self.app.selection_status_var.get()
        self.assertIn("Row 1", status_text)
        self.assertIn("Main Col 1", status_text)
        self.assertIn("Subcol 2", status_text)
        self.assertIn("pen", status_text)

    def test_safe_gui_error_boundary_on_unlabeled_quantity(self):
        # Enter unlabeled quantity '1' without an item
        self.app.add_token(0, "1")

        # In previous code, calculate() threw an uncaught ValueError.
        # Now it must catch it, return None, set result_var to 'Error', and NOT crash!
        res = self.app.calculate()
        self.assertIsNone(res)
        self.assertEqual(self.app.result_var.get(), "Error")
        self.assertIn("Unlabeled quantity: '1' has no item label", self.app.result_word_var.get())

        # Crucial requirement: user entered cells must remain completely intact!
        row = self.app.grid_model.rows[0]
        self.assertEqual(len(row.addend_columns[0].ordered_subcolumns), 1)
        self.assertEqual(row.addend_columns[0].ordered_subcolumns[0].value, "1")

    def test_correct_missing_label_and_recalculate_successfully(self):
        # Enter unlabeled quantity '1'
        self.app.add_token(0, "1")
        self.app.calculate()
        self.assertEqual(self.app.result_var.get(), "Error")

        # Now select the cell or next subcolumn and add the missing label 'pen'
        self.app._on_keypad_press("Next Subcol (→)")
        self.app._on_vocab_click("pen", TokenType.ITEM)

        # Recalculate: error is cleared and result computes successfully!
        res = self.app.calculate()
        self.assertIsNotNone(res)
        self.assertEqual(self.app.result_var.get(), "1")
        self.assertEqual(self.app.result_word_var.get(), "1 pen")




class TestMathematicalTemplateArchitecture(unittest.TestCase):
    """
    Tests for Mathematical Templates architecture:
    - Immutable MathTemplate with named, typed placeholder slots (TemplateSlot).
    - Separation of template structure from runtime values.
    - Deterministic TemplateValidator enforcing addition (+) and parentheses only.
    - Rejection of invalid operators, unclosed parens, empty groups, and unsupported symbols.
    """

    def test_immutable_template_and_slot_metadata(self):
        tpl = MathTemplate(template_id="t1", pattern="(□ + □) + □", name="Group plus term")
        self.assertEqual(tpl.slot_count, 3)
        self.assertEqual(tpl.slots_meta[0].name, "term_1")
        self.assertEqual(tpl.slots_meta[0].expected_type, "NUMBER")
        self.assertEqual(tpl.slots_meta[1].name, "term_2")
        self.assertEqual(tpl.slots_meta[2].name, "term_3")

        # Creating an instance produces distinct TemplateSlots
        inst = tpl.create_instance(initial_values=["10", "20", "30"])
        self.assertEqual(len(inst.slots), 3)
        self.assertEqual(inst.slots[0].value, "10")
        self.assertEqual(inst.slots[1].value, "20")
        self.assertEqual(inst.slots[2].value, "30")
        self.assertTrue(all(s.is_filled for s in inst.slots))

    def test_template_validator_valid_patterns(self):
        valid_patterns = [
            "□ + □",
            "(□ + □)",
            "□ + □ + □",
            "(□ + □) + □",
            "(□ + (□ + □))",
            "((□ + □) + (□ + □))",
        ]
        for pat in valid_patterns:
            TemplateValidator.validate_addition_pattern(pat)

    def test_template_validator_rejects_subtraction_and_algebra_symbols(self):
        invalid_patterns = [
            "□ - □",        # Subtraction rejected in this stage
            "□ * □",        # Multiplication rejected
            "□ / □",        # Division rejected
            "x + y",        # Unstructured algebra variables rejected
            "□ + ",         # Trailing operator
            "+ □",          # Leading operator
            "□ + + □",      # Consecutive operators
            "(□ + □",       # Unmatched open paren
            "□ + □)",       # Unmatched close paren
            "()",           # Empty group
            "",             # Empty pattern
        ]
        for pat in invalid_patterns:
            with self.assertRaises(ValueError):
                TemplateValidator.validate_addition_pattern(pat)


class TestExpressionTemplateParserAndManager(unittest.TestCase):
    """
    Tests for ExpressionTemplateParser and MathTemplateManager:
    - Parsing pasted addition expressions into MathTemplate and initial slot values.
    - Preview without mandatory saving.
    - Optional template saving persisted to custom_templates.json.
    """

    def test_parse_pasted_numerical_expression(self):
        expr = "(15.5 + 4.25) + 8.0"
        tpl, initial_vals = ExpressionTemplateParser.parse_pasted_expression(expr)
        self.assertEqual(tpl.pattern, "( □ + □ ) + □")
        self.assertEqual(initial_vals, ["15.5", "4.25", "8.0"])
        self.assertEqual(tpl.slot_count, 3)

    def test_parse_pasted_placeholder_expression(self):
        expr = "(□ + □) + □"
        tpl, initial_vals = ExpressionTemplateParser.parse_pasted_expression(expr)
        self.assertEqual(tpl.pattern, "( □ + □ ) + □")
        self.assertEqual(initial_vals, ["", "", ""])

    def test_parse_pasted_expression_rejects_unsupported_operators(self):
        with self.assertRaises(ValueError) as ctx:
            ExpressionTemplateParser.parse_pasted_expression("(15.5 - 4.25) + 8.0")
        self.assertIn("Unsupported token", str(ctx.exception))

    def test_template_manager_builtin_and_custom_saving(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_json = Path(tmp_dir) / "test_custom_templates.json"
            mgr = MathTemplateManager(storage_file=tmp_json)

            # Builtins should be available
            patterns = [t.pattern for t in mgr.templates]
            self.assertIn("□ + □", patterns)
            self.assertIn("(□ + □)", patterns)
            self.assertIn("(□ + □) + □", patterns)

            # Save a custom template
            custom_tpl = MathTemplate(template_id="custom_test", pattern="□ + □ + □ + □", name="Four terms", is_custom=True)
            mgr.save_custom_template(custom_tpl)
            self.assertIn("□ + □ + □ + □", [t.pattern for t in mgr.templates])
            self.assertTrue(tmp_json.exists())

            # Load new manager from same file
            mgr2 = MathTemplateManager(storage_file=tmp_json)
            self.assertIn("□ + □ + □ + □", [t.pattern for t in mgr2.templates])


class TestTemplateDrivenCalculatorGUI(unittest.TestCase):
    """
    Tests for GUI integration with templates:
    - Applying a template populates Column 1 with clickable slots.
    - Keypad inputs fill active slot.
    - Pasted expression preview in Column 1.
    - Optional template saving.
    - Row type selection (Addend row vs Label row vs rejected Algebra step).
    - Unfilled slot and unlabeled quantity error boundaries.
    """

    @classmethod
    def setUpClass(cls):
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
            cls.gui_available = True
        except Exception:
            cls.gui_available = False

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, "gui_available", False) and hasattr(cls, "root"):
            try:
                cls.root.destroy()
            except Exception:
                pass

    def setUp(self):
        if not self.gui_available:
            self.skipTest("Tkinter display not available")
        self.app = AdditionTokenCalculator(root=self.root)

    def tearDown(self):
        self.app.clear()

    def test_pasted_expression_preview_and_calculate(self):
        # Enter pasted expression into preview input
        self.app.pasted_expr_var.set("(10 + 20) + 30")
        self.app._on_preview_pasted_expression()

        # Check Column 1 template and slot values
        row = self.app.template_grid_model.rows[0]
        self.assertIsNotNone(row.template_instance)
        self.assertEqual(row.template_instance.template.pattern, "( □ + □ ) + □")
        self.assertEqual([s.value for s in row.template_instance.slots], ["10", "20", "30"])

        # Save button should be enabled during preview
        self.assertEqual(str(self.app.save_tpl_btn["state"]), "normal")

        # Fill description columns: Col 2 = 'pens', Col 3 = 'in the drawer'
        self.app.template_grid_model.cursor_col = 2
        self.app._on_vocab_click("pens", TokenType.ITEM)
        self.app.template_grid_model.cursor_col = 3
        self.app._on_vocab_click("in the drawer", TokenType.CONTEXT)

        # Calculate result
        res = self.app.calculate()
        self.assertIsNotNone(res)
        self.assertEqual(self.app.result_var.get(), "60")
        self.assertEqual(self.app.result_word_var.get(), "60 pens in the drawer")

    def test_pasted_preview_receives_number_pad_input_and_parentheses(self):
        # 1. Select pasted preview as the active destination
        self.app.select_pasted_preview()
        self.assertEqual(self.app.active_input_target, "pasted_preview")

        # 2. Enter '(1 + 2) + 5' using the number pad on the bottom left
        self.app._on_keypad_press("(")
        self.assertEqual(self.app.pasted_expr_var.get(), "(")

        self.app._on_keypad_press("1")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1")

        self.app._on_keypad_press("+")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1 + ")

        self.app._on_keypad_press("2")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1 + 2")

        self.app._on_keypad_press(")")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1 + 2)")

        self.app._on_keypad_press("+")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1 + 2) + ")

        self.app._on_keypad_press("3")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1 + 2) + 3")

        # 3. Test Backspace via keypad
        self.app._on_keypad_press("Backspace")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1 + 2) + ")

        self.app._on_keypad_press("5")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1 + 2) + 5")

        # 4. Press '=' on keypad -> triggers Preview Pasted
        self.app._on_keypad_press("=")

        # Assert template is loaded into Row 1 Column 1
        row = self.app.template_grid_model.rows[0]
        self.assertIsNotNone(row.template_instance)
        self.assertEqual(row.template_instance.template.pattern, "( □ + □ ) + □")
        self.assertEqual([s.value for s in row.template_instance.slots], ["1", "2", "5"])
        self.assertEqual(self.app.active_input_target, "grid")

        # 5. Add unit label and calculate
        self.app.template_grid_model.rows[0].description_columns[0] = "notebooks"
        self.app.calculate()
        self.assertEqual(self.app.result_var.get(), "8")
        self.assertEqual(self.app.result_word_var.get(), "8 notebooks")

        # 6. Test Clear (C) in pasted preview mode
        self.app.select_pasted_preview()
        self.app._on_keypad_press("7")
        self.assertEqual(self.app.pasted_expr_var.get(), "(1 + 2) + 57")
        self.app._on_keypad_press("C")
        self.assertEqual(self.app.pasted_expr_var.get(), "")

    def test_save_template_clickable_and_saves_directly_when_entering_via_keypad(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.app.template_manager.storage_file = Path(tmp_dir) / "custom_templates.json"

            # 1. Initially Save Template button is disabled
            self.assertEqual(str(self.app.save_tpl_btn["state"]), "disabled")

            # 2. Select pasted preview entry and enter expression using number pad
            self.app.select_pasted_preview()
            self.app._on_keypad_press("(")
            # Button should immediately become normal (clickable)
            self.assertEqual(str(self.app.save_tpl_btn["state"]), "normal")

            self.app._on_keypad_press("3")
            self.app._on_keypad_press("+")
            self.app._on_keypad_press("4")
            self.app._on_keypad_press(")")
            self.assertEqual(self.app.pasted_expr_var.get(), "(3 + 4)")
            self.assertEqual(str(self.app.save_tpl_btn["state"]), "normal")

            # 3. User clicks Save Template button directly with mouse (simulated via invoke)
            self.app.save_tpl_btn.invoke()

            # 4. Verify template is saved to registry and dropdown
            saved = next((t for t in self.app.template_manager.templates if t.pattern == "( □ + □ )"), None)
            self.assertIsNotNone(saved)
            self.assertEqual(self.app.selected_template_var.get(), "( □ + □ )")

            # 5. Row 1 Column 1 has clean empty placeholders ready for numbers
            row = self.app.template_grid_model.rows[0]
            self.assertIsNotNone(row.template_instance)
            self.assertEqual(row.template_instance.template.pattern, "( □ + □ )")
            self.assertEqual([s.value for s in row.template_instance.slots], ["", ""])
            self.assertFalse(row.template_instance.slots[0].is_filled)

            # 6. Active input target is back to grid, so keypad enters into slot 0
            self.assertEqual(self.app.active_input_target, "grid")
            self.app._on_keypad_press("9")
            self.assertEqual(row.template_instance.slots[0].value, "9")

    def test_unfilled_template_slot_shows_safe_error_boundary(self):
        # Set template but leave second slot empty
        tpl = MathTemplate(template_id="t_two", pattern="□ + □")
        self.app.template_grid_model.apply_template_to_row(0, tpl)
        self.app.template_grid_model.rows[0].template_instance.slots[0].value = "5"
        self.app.template_grid_model.rows[0].description_columns[0] = "pens"

        res = self.app.calculate()
        self.assertIsNone(res)
        self.assertEqual(self.app.result_var.get(), "Error")
        self.assertIn("empty (□)", self.app.result_word_var.get())

        # Inspector contains actionable recovery steps and user slots remain intact
        inspector_text = self.app.inspector_text.get("1.0", "end")
        self.assertIn("Validation Error", inspector_text)
        self.assertIn("All existing cell values remain intact", inspector_text)
        self.assertEqual(self.app.template_grid_model.rows[0].template_instance.slots[0].value, "5")

    def test_next_row_dialog_and_algebra_step_rejection(self):
        # Create an ADDEND row
        idx1 = self.app.template_grid_model.add_row(RowType.ADDEND)
        self.assertEqual(idx1, 1)
        self.assertEqual(self.app.template_grid_model.rows[1].row_type, RowType.ADDEND)

        # Create a LABEL row
        idx2 = self.app.template_grid_model.add_row(RowType.LABEL, explanation="Subtotal of pencils")
        self.assertEqual(idx2, 2)
        self.assertEqual(self.app.template_grid_model.rows[2].row_type, RowType.LABEL)
        self.assertEqual(self.app.template_grid_model.rows[2].explanation_text, "Subtotal of pencils")

        # Future ALGEBRA_STEP row is rejected deterministically in this stage
        with self.assertRaises(ValueError) as ctx:
            self.app.template_grid_model.add_row(RowType.ALGEBRA_STEP)
        self.assertIn("Algebra steps are reserved for a future development stage", str(ctx.exception))



class TestSingleSlotTemplateLifecycle(unittest.TestCase):
    """
    Regression tests for single-slot template lifecycle:
    - Previewing '1' generates a reusable single-slot template '□'.
    - Preview retains '1' as current editable value.
    - Saving template preserves reusable placeholder '□' (not permanently storing '1').
    - Saving resets mathematical column to show empty editable placeholder '□'.
    - Entering another number using central keypad fills that placeholder.
    - Selecting saved template for a new calculation shows empty editable placeholder.
    - Saving and loading templates keeps structure separate from runtime values.
    - Existing calculations and labels remain unchanged.
    """

    @classmethod
    def setUpClass(cls):
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
            cls.gui_available = True
        except Exception:
            cls.gui_available = False

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, "gui_available", False) and hasattr(cls, "root"):
            try:
                cls.root.destroy()
            except Exception:
                pass

    def setUp(self):
        if not self.gui_available:
            self.skipTest("Tkinter display not available")
        self.app = AdditionTokenCalculator(root=self.root)

    def tearDown(self):
        self.app.clear()

    def test_single_slot_preview_retains_value_but_saving_preserves_empty_placeholder(self):
        # 1. Previewing '1' generates a reusable single-slot template '□'
        self.app.pasted_expr_var.set("1")
        self.app._on_preview_pasted_expression()

        row = self.app.template_grid_model.rows[0]
        self.assertIsNotNone(row.template_instance)
        # Template pattern is strictly the placeholder '□'
        self.assertEqual(row.template_instance.template.pattern, "□")
        self.assertEqual(row.template_instance.template.slot_count, 1)

        # 2. Preview retains '1' as current editable value
        self.assertEqual(row.template_instance.slots[0].value, "1")
        self.assertEqual(str(self.app.save_tpl_btn["state"]), "normal")

        # 3. Saving template must preserve reusable placeholder '□', not '1'
        self.app._on_save_custom_template()

        # The saved template pattern in manager is '□'
        saved_tpl = next((t for t in self.app.template_manager.templates if t.pattern == "□"), None)
        self.assertIsNotNone(saved_tpl)
        self.assertEqual(saved_tpl.pattern, "□")
        self.assertEqual(saved_tpl.slot_count, 1)

        # Mathematical column in the grid now shows the clean empty placeholder '□'
        self.assertEqual(row.template_instance.slots[0].value, "")
        self.assertFalse(row.template_instance.slots[0].is_filled)

        # 4. Entering another number using central keypad fills that placeholder
        self.app._on_keypad_press("4")
        self.app._on_keypad_press("2")
        self.assertEqual(row.template_instance.slots[0].value, "42")

    def test_select_saved_single_slot_template_for_new_calculation(self):
        # Ensure single-slot template '□' is in manager
        single_tpl = MathTemplate(template_id="custom_single", pattern="□", name="Single term", is_custom=True)
        self.app.template_manager.save_custom_template(single_tpl)

        # Row 1: Set a calculation with labels
        row1 = self.app.template_grid_model.rows[0]
        row1.description_columns[0] = "pens"
        row1.description_columns[1] = "in the drawer"

        # Apply saved single-slot template '□'
        self.app.selected_template_var.set("□")
        self.app._on_apply_selected_template()

        # Must show empty editable placeholder
        self.assertEqual(row1.template_instance.slots[0].value, "")
        self.assertFalse(row1.template_instance.slots[0].is_filled)

        # Labels on the row must remain unchanged
        self.assertEqual(row1.description_columns[0], "pens")
        self.assertEqual(row1.description_columns[1], "in the drawer")

        # Fill placeholder with keypad
        self.app._on_keypad_press("5")
        self.assertEqual(row1.template_instance.slots[0].value, "5")

        # Calculate result
        res = self.app.calculate()
        self.assertIsNotNone(res)
        self.assertEqual(self.app.result_var.get(), "5")
        self.assertEqual(self.app.result_word_var.get(), "5 pens in the drawer")

    def test_combobox_selection_applies_empty_placeholder_immediately(self):
        # Ensure single-slot template '□' is available
        single_tpl = MathTemplate(template_id="custom_single_combo", pattern="□", name="Single term", is_custom=True)
        self.app.template_manager.save_custom_template(single_tpl)

        # Put a dummy value into slot
        self.app.template_grid_model.rows[0].template_instance.slots[0].value = "99"

        # Change dropdown selection and fire event
        self.app.selected_template_var.set("□")
        self.app._on_apply_selected_template()

        # Slot is reset to clean empty placeholder
        self.assertEqual(self.app.template_grid_model.rows[0].template_instance.slots[0].value, "")

    def test_saving_and_loading_keeps_structure_separate_from_runtime_values(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_json = Path(tmp_dir) / "custom_templates.json"
            mgr1 = MathTemplateManager(storage_file=tmp_json)

            # Parse expression with runtime value '1'
            tpl, initial_vals = ExpressionTemplateParser.parse_pasted_expression("1")
            self.assertEqual(tpl.pattern, "□")
            self.assertEqual(initial_vals, ["1"])

            # Save clean template to manager
            mgr1.save_custom_template(tpl)

            # Verify persisted JSON has pattern '□' and NO numbers
            raw_json = tmp_json.read_text(encoding="utf-8")
            self.assertIn('"pattern": "□"', raw_json)
            self.assertNotIn('"1"', raw_json)

            # Load new manager from disk
            mgr2 = MathTemplateManager(storage_file=tmp_json)
            loaded_tpl = next((t for t in mgr2.templates if t.pattern == "□"), None)
            self.assertIsNotNone(loaded_tpl)
            self.assertEqual(loaded_tpl.pattern, "□")

            # Instantiating creates empty placeholder
            new_inst = loaded_tpl.create_instance()
            self.assertEqual(new_inst.slots[0].value, "")



class TestSlotInputValidationAndGridAlignment(unittest.TestCase):
    """
    Regression tests for:
    - Slot input validation: rejecting parentheses '(', ')' inside numeric slots.
    - Preventing unbalanced parentheses corruption in numeric slots.
    - Decimal point entered only once per slot.
    - Keypad '+' in template mode advancing to the next slot.
    - Grid-column alignment: Column 2 (Item) and Column 3 (Context) aligned directly below each other
      across different rows regardless of varying Column 1 template sizes.
    - Clean KeyboardInterrupt handling on program termination.
    """

    @classmethod
    def setUpClass(cls):
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
            cls.gui_available = True
        except Exception:
            cls.gui_available = False

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, "gui_available", False) and hasattr(cls, "root"):
            try:
                cls.root.destroy()
            except Exception:
                pass

    def setUp(self):
        if not self.gui_available:
            self.skipTest("Tkinter display not available")
        self.app = AdditionTokenCalculator(root=self.root)

    def tearDown(self):
        self.app.clear()

    def test_numeric_slot_rejects_parentheses_and_unbalanced_syntax(self):
        # Default template: □ + □
        # 1. Give Slot 1 value '5'
        self.app._on_keypad_press("5")
        slot0 = self.app.template_grid_model.rows[0].template_instance.slots[0]
        self.assertEqual(slot0.value, "5")

        # 2. Click the box / select slot 0 again
        self.app.select_cell(0, "addend", 0, 0)
        self.assertEqual(self.app.template_grid_model.cursor_slot, 0)

        # 3. Press '(' on keypad
        self.app._on_keypad_press("(")

        # Value must remain '5' and NOT become '5(' or '('
        self.assertEqual(slot0.value, "5")

        # Press ')' on keypad
        self.app._on_keypad_press(")")
        self.assertEqual(slot0.value, "5")

        # Inspector provides clear feedback explaining that parentheses define template structure
        inspector_content = self.app.inspector_text.get("1.0", "end")
        self.assertIn("Parentheses", inspector_content)
        self.assertIn("template structure", inspector_content)

    def test_decimal_point_entered_only_once_per_slot(self):
        # Empty slot: press '.' -> becomes '0.'
        self.app._on_keypad_press(".")
        slot0 = self.app.template_grid_model.rows[0].template_instance.slots[0]
        self.assertEqual(slot0.value, "0.")

        # Press '5' -> '0.5'
        self.app._on_keypad_press("5")
        self.assertEqual(slot0.value, "0.5")

        # Press '.' again -> must still be '0.5', NOT '0.5.'
        self.app._on_keypad_press(".")
        self.assertEqual(slot0.value, "0.5")

    def test_keypad_plus_skips_to_next_slot_on_right_of_plus_sign(self):
        # In template □ + □:
        # Enter '5' into first square (slot 0)
        self.app._on_keypad_press("5")
        self.assertEqual(self.app.template_grid_model.cursor_slot, 0)
        self.assertEqual(self.app.template_grid_model.cursor_col, 1)
        slot0 = self.app.template_grid_model.rows[0].template_instance.slots[0]
        self.assertEqual(slot0.value, "5")

        # Press '+' -> skips to the square box on the right side of the '+' sign (slot 1)
        self.app._on_keypad_press("+")
        self.assertEqual(self.app.template_grid_model.cursor_slot, 1)
        self.assertEqual(self.app.template_grid_model.cursor_col, 1)
        # Value in slot 0 remains intact (preserved)
        self.assertEqual(slot0.value, "5")

        # Enter '3' into slot 1
        self.app._on_keypad_press("3")
        slot1 = self.app.template_grid_model.rows[0].template_instance.slots[1]
        self.assertEqual(slot1.value, "3")

        # Press '+' while on the last slot -> does NOT advance to Col 2, stays on slot 1
        self.app._on_keypad_press("+")
        self.assertEqual(self.app.template_grid_model.cursor_slot, 1)
        self.assertEqual(self.app.template_grid_model.cursor_col, 1)
        inspector_content = self.app.inspector_text.get("1.0", "end")
        self.assertIn("All placeholder boxes (□) in this mathematical template have been reached", inspector_content)

        # Explicit navigation into Column 2 via Next Col (⇒)
        self.app._on_keypad_press("Next Col (⇒)")
        self.assertEqual(self.app.template_grid_model.cursor_col, 2)
        self.app.template_grid_model.rows[0].description_columns[0] = "pens"

        # Calculate result
        self.app.calculate()
        self.assertEqual(self.app.result_var.get(), "8")
        self.assertEqual(self.app.result_word_var.get(), "8 pens")

    def test_grid_columns_align_across_different_template_sizes(self):
        # Row 1: Single slot template '□'
        tpl1 = MathTemplate(template_id="t_single", pattern="□", name="Single term")
        self.app.template_grid_model.apply_template_to_row(0, tpl1)
        self.app.template_grid_model.rows[0].description_columns[0] = "pens"
        self.app.template_grid_model.rows[0].description_columns[1] = "in the drawer"

        # Row 2: Three slot template '□ + □ + □' (wider than Row 1)
        tpl2 = MathTemplate(template_id="t_three", pattern="□ + □ + □", name="Three terms")
        row2_idx = self.app.template_grid_model.add_row(RowType.ADDEND)
        self.app.template_grid_model.apply_template_to_row(row2_idx, tpl2)
        self.app.template_grid_model.rows[row2_idx].description_columns[0] = "apples"
        self.app.template_grid_model.rows[row2_idx].description_columns[1] = "in the basket"

        self.app.render_grid()
        self.root.update_idletasks()

        # Check grid configuration of row cards and header bar
        cards = [child for child in self.app.grid_frame.winfo_children() if isinstance(child, tk.Frame)]
        header_bar = cards[0]
        row_cards = cards[1:]
        self.assertEqual(len(row_cards), 2)

        card1 = row_cards[0]
        card2 = row_cards[1]

        # Verify header bar and row cards have identical column minsize configurations
        self.assertEqual(header_bar.columnconfigure(1)["minsize"], 320)
        self.assertEqual(card1.columnconfigure(1)["minsize"], 320)
        self.assertEqual(card2.columnconfigure(1)["minsize"], 320)

        self.assertEqual(header_bar.columnconfigure(2)["minsize"], 140)
        self.assertEqual(card1.columnconfigure(2)["minsize"], 140)
        self.assertEqual(card2.columnconfigure(2)["minsize"], 140)

        self.assertEqual(header_bar.columnconfigure(3)["minsize"], 180)
        self.assertEqual(card1.columnconfigure(3)["minsize"], 180)
        self.assertEqual(card2.columnconfigure(3)["minsize"], 180)

    def test_synchronized_alignment_with_long_mathematical_expressions_and_labels(self):
        # Row 1: Short single-slot template '□'
        tpl1 = MathTemplate(template_id="t_single", pattern="□", name="Single term")
        self.app.template_grid_model.apply_template_to_row(0, tpl1)
        self.app.template_grid_model.rows[0].description_columns[0] = "pens"
        self.app.template_grid_model.rows[0].description_columns[1] = "desk"

        # Row 2: Long nested expression template: ((□ + □) + (□ + □)) + ((□ + □) + (□ + □))
        long_pattern = "((□ + □) + (□ + □)) + ((□ + □) + (□ + □))"
        tpl_long = MathTemplate(template_id="t_long", pattern=long_pattern, name="Long expression")
        row2_idx = self.app.template_grid_model.add_row(RowType.ADDEND)
        self.app.template_grid_model.apply_template_to_row(row2_idx, tpl_long)

        # Long descriptive labels in Row 2
        long_item = "extraordinary long chemical pharmaceutical reagent grade substance"
        long_context = "stored inside pressurized temperature-regulated cleanroom facility cabinet"
        self.app.template_grid_model.rows[row2_idx].description_columns[0] = long_item
        self.app.template_grid_model.rows[row2_idx].description_columns[1] = long_context

        self.app.render_grid()
        self.root.update_idletasks()

        cards = [child for child in self.app.grid_frame.winfo_children() if isinstance(child, tk.Frame)]
        header_bar = cards[0]
        card1 = cards[1]
        card2 = cards[2]

        # Column 1 minsize must dynamically expand to accommodate long expression (well over 320)
        sync_col1 = card1.columnconfigure(1)["minsize"]
        self.assertGreater(sync_col1, 320)
        self.assertEqual(card2.columnconfigure(1)["minsize"], sync_col1)
        self.assertEqual(header_bar.columnconfigure(1)["minsize"], sync_col1)

        # Column 2 minsize must dynamically expand to accommodate long item label (well over 140)
        sync_col2 = card1.columnconfigure(2)["minsize"]
        self.assertGreater(sync_col2, 140)
        self.assertEqual(card2.columnconfigure(2)["minsize"], sync_col2)
        self.assertEqual(header_bar.columnconfigure(2)["minsize"], sync_col2)

        # Column 3 minsize must dynamically expand to accommodate long context label (well over 180)
        sync_col3 = card1.columnconfigure(3)["minsize"]
        self.assertGreater(sync_col3, 180)
        self.assertEqual(card2.columnconfigure(3)["minsize"], sync_col3)
        self.assertEqual(header_bar.columnconfigure(3)["minsize"], sync_col3)

    def test_horizontal_scrolling_and_narrow_window_support(self):
        # Verify horizontal scrollbar exists and is wired to canvas xview
        self.assertTrue(hasattr(self.app, "scrollbar_x"))
        self.assertIsInstance(self.app.scrollbar_x, tk.Scrollbar)

        # Verify total_grid_content_width is calculated and positive
        self.assertGreater(self.app.total_grid_content_width, 0)

        # Verify canvas configure callback preserves minimum content width on narrow resizing
        dummy_event = tk.Event()
        dummy_event.width = 400  # Narrow window width below grid content width
        self.app._on_canvas_configure(dummy_event)
        canvas_win_w = self.app.canvas.itemcget(self.app.canvas_window_id, "width")
        self.assertGreaterEqual(float(canvas_win_w), self.app.total_grid_content_width)

    def test_graceful_exit_on_keyboard_interrupt(self):
        from unittest.mock import patch
        from addition_tokens.addition import main, AdditionTokenCalculator

        # Create isolated root for the shutdown test so class root is not destroyed
        isolated_root = tk.Tk()
        isolated_root.withdraw()
        app = AdditionTokenCalculator(root=isolated_root)
        app._owns_root = True

        # Simulate KeyboardInterrupt on mainloop
        with patch.object(app.root, "mainloop", side_effect=KeyboardInterrupt):
            # run() should catch KeyboardInterrupt without re-raising and cleanly destroy isolated_root
            app.run()

        with patch("addition_tokens.addition.AdditionTokenCalculator") as mock_calc:
            mock_inst = mock_calc.return_value
            mock_inst.run.side_effect = KeyboardInterrupt
            # main() should catch KeyboardInterrupt without re-raising
            main()

        # Non-KeyboardInterrupt exceptions (like ValueError) must NOT be masked and should propagate
        isolated_root2 = tk.Tk()
        isolated_root2.withdraw()
        try:
            app2 = AdditionTokenCalculator(root=isolated_root2)
            app2._owns_root = True
            with patch.object(app2.root, "mainloop", side_effect=ValueError("test unmasked error")):
                with self.assertRaises(ValueError):
                    app2.run()
        finally:
            try:
                isolated_root2.destroy()
            except Exception:
                pass


class TestResultsWindowAndScrolling(unittest.TestCase):
    """
    Comprehensive regression tests for the dedicated Results Window:
    1. Results longer than the application window.
    2. Multiline descriptive results.
    3. Vertical scrolling.
    4. Horizontal scrolling with wrapping disabled.
    5. Text wrapping enabled.
    6. Increasing and decreasing the result font size.
    7. Resizing the result area.
    8. Copying complete results.
    9. Long numerical results with exact Decimal formatting.
    10. Keeping the keypad visible while resizing.
    11. Long error messages.
    12. Existing mathematical calculations remaining unchanged.
    """

    @classmethod
    def setUpClass(cls):
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
            cls.gui_available = True
        except Exception:
            cls.gui_available = False

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, "gui_available", False) and hasattr(cls, "root"):
            try:
                cls.root.destroy()
            except Exception:
                pass

    def setUp(self):
        if not self.gui_available:
            self.skipTest("Tkinter display not available")
        self.app = AdditionTokenCalculator(root=self.root)

    def tearDown(self):
        self.app.clear()

    def test_multiline_descriptive_results_and_layout(self):
        # Calculate standard expression
        self.app._on_keypad_press("5")
        self.app._on_keypad_press("Next Slot (→)")
        self.app._on_keypad_press("3")
        self.app.template_grid_model.rows[0].description_columns[0] = "pens"
        self.app.calculate()

        # Multiline text widget contains formatted numerical total and sentence result
        text_content = self.app.results_text.get("1.0", "end")
        self.assertIn("NUMERICAL TOTAL:    8", text_content)
        self.assertIn("DESCRIPTIVE RESULT: 8 pens", text_content)
        self.assertIn("MATHEMATICAL ADDEND BREAKDOWN", text_content)
        self.assertIn("Quantity: 5 pens", text_content)
        self.assertIn("Quantity: 3 pens", text_content)

    def test_results_longer_than_window_and_vertical_scrolling(self):
        # Fill Row 0
        self.app.template_grid_model.rows[0].template_instance.slots[0].value = "10"
        self.app.template_grid_model.rows[0].template_instance.slots[1].value = "5"
        self.app.template_grid_model.rows[0].description_columns[0] = "scientific_component_0"
        self.app.template_grid_model.rows[0].description_columns[1] = "laboratory_bay_0"

        # Create additional rows with detailed terms
        for i in range(1, 12):
            r_idx = self.app.add_addend_row()
            self.app.template_grid_model.apply_template_to_row(r_idx, self.app.template_manager.templates[0])
            self.app.template_grid_model.rows[r_idx].template_instance.slots[0].value = str(10 + i)
            self.app.template_grid_model.rows[r_idx].template_instance.slots[1].value = "5"
            self.app.template_grid_model.rows[r_idx].description_columns[0] = f"scientific_component_{i}"
            self.app.template_grid_model.rows[r_idx].description_columns[1] = f"laboratory_bay_{i}"

        self.app.calculate()
        text_content = self.app.results_text.get("1.0", "end")
        self.assertGreater(len(text_content.splitlines()), 25)

        # Vertical scrollbar is active and wired to results text
        self.assertTrue(hasattr(self.app, "results_scroll_y"))
        y_view_before = self.app.results_text.yview()
        self.app.results_text.yview_scroll(5, "units")
        y_view_after = self.app.results_text.yview()
        self.assertIsNotNone(y_view_after)

    def test_horizontal_scrolling_with_wrapping_disabled(self):
        # Default is wrap word (Wrap: ON)
        self.assertTrue(self.app.results_wrap_mode)
        self.assertEqual(self.app.results_text.cget("wrap"), "word")

        # Toggle to Wrap: OFF
        self.app.toggle_results_wrap()
        self.assertFalse(self.app.results_wrap_mode)
        self.assertEqual(self.app.results_text.cget("wrap"), "none")
        self.assertEqual(self.app.wrap_btn.cget("text"), "Wrap: OFF")

        # Horizontal scrollbar is wired to results text xview
        self.assertTrue(hasattr(self.app, "results_scroll_x"))
        self.app.results_text.xview_scroll(2, "units")

        # Toggle back to Wrap: ON
        self.app.toggle_results_wrap()
        self.assertTrue(self.app.results_wrap_mode)
        self.assertEqual(self.app.results_text.cget("wrap"), "word")
        self.assertEqual(self.app.wrap_btn.cget("text"), "Wrap: ON")

    def test_increasing_decreasing_and_resetting_result_font_size(self):
        initial_font_size = self.app.results_font_size

        # Increase font size
        self.app.increase_results_font()
        self.assertEqual(self.app.results_font_size, initial_font_size + 1)
        font_tuple = self.app.results_text.cget("font")
        self.assertIn(str(initial_font_size + 1), str(font_tuple))

        # Decrease font size twice
        self.app.decrease_results_font()
        self.app.decrease_results_font()
        self.assertEqual(self.app.results_font_size, initial_font_size - 1)

        # Reset font size
        self.app.reset_results_font()
        self.assertEqual(self.app.results_font_size, 10)

        # Font changes must NOT alter mathematical values
        self.app._on_keypad_press("12")
        self.app._on_keypad_press("Next Slot (→)")
        self.app._on_keypad_press("8")
        self.app.template_grid_model.rows[0].description_columns[0] = "meters"
        self.app.calculate()
        self.assertEqual(self.app.result_var.get(), "20")

    def test_resizing_result_area_and_expand_toggle(self):
        # Verify ttk.PanedWindow houses scroll_container and result_frame
        self.assertTrue(hasattr(self.app, "main_paned"))
        panes = self.app.main_paned.panes()
        self.assertEqual(len(panes), 2)

        # Toggle expand
        self.assertFalse(self.app.results_expanded)
        self.app.toggle_expand_results()
        self.assertTrue(self.app.results_expanded)
        self.assertIn("Collapse", self.app.expand_btn.cget("text"))

        # Toggle collapse
        self.app.toggle_expand_results()
        self.assertFalse(self.app.results_expanded)
        self.assertIn("Expand", self.app.expand_btn.cget("text"))

    def test_copying_complete_results(self):
        self.app._on_keypad_press("100")
        self.app._on_keypad_press("Next Slot (→)")
        self.app._on_keypad_press("50")
        self.app.template_grid_model.rows[0].description_columns[0] = "volts"
        self.app.calculate()

        copied = self.app.copy_results_to_clipboard()
        self.assertIn("NUMERICAL TOTAL:    150", copied)
        self.assertIn("DESCRIPTIVE RESULT: 150 volts", copied)
        self.assertIn("Quantity: 100 volts", copied)

    def test_long_numerical_results_with_exact_decimal_formatting(self):
        # Very high precision Decimal values without floating point conversion
        d1 = "12345678901234567890.12345678901234567890"
        d2 = "98765432109876543210.98765432109876543210"
        expected_sum = "111111111011111111101.111111110111111111"

        self.app._on_keypad_press(d1)
        self.app._on_keypad_press("Next Slot (→)")
        self.app._on_keypad_press(d2)
        self.app.template_grid_model.rows[0].description_columns[0] = "nanometers"
        self.app.calculate()

        self.assertEqual(self.app.result_var.get(), expected_sum)
        text_content = self.app.results_text.get("1.0", "end")
        self.assertIn(expected_sum, text_content)

    def test_keypad_visibility_and_anchor_during_resizing(self):
        # Keypad is in bottom_container, which is packed to bottom outside the paned window
        self.assertEqual(self.app.bottom_container.master, self.app.root)
        self.assertIn("0", self.app.keypad_buttons)
        btn_0 = self.app.keypad_buttons["0"]

        # Grid coordinate anchor for button 0 must remain at row 4, column 0
        info_0 = btn_0.grid_info()
        self.assertEqual(info_0["row"], 4)
        self.assertEqual(info_0["column"], 0)

        # Trigger expand and collapse
        self.app.toggle_expand_results()
        info_0_expanded = btn_0.grid_info()
        self.assertEqual(info_0_expanded["row"], 4)
        self.assertEqual(info_0_expanded["column"], 0)

        self.app.toggle_expand_results()
        info_0_restored = btn_0.grid_info()
        self.assertEqual(info_0_restored["row"], 4)
        self.assertEqual(info_0_restored["column"], 0)

    def test_long_error_messages_displayed_in_results_window(self):
        # Unfilled slot error with descriptive text
        self.app._on_keypad_press("42")
        # Slot 1 is left unfilled
        self.app.template_grid_model.rows[0].description_columns[0] = "widgets"
        self.app.calculate()

        self.assertEqual(self.app.result_var.get(), "Error")
        text_content = self.app.results_text.get("1.0", "end")
        self.assertIn("VALIDATION NOTICE", text_content)
        self.assertIn("empty (□)", text_content)
        self.assertIn("Note: All current cell inputs and templates remain intact", text_content)

        # Current inputs are not destroyed
        slot0 = self.app.template_grid_model.rows[0].template_instance.slots[0]
        self.assertEqual(slot0.value, "42")

    def test_existing_mathematical_calculations_remain_unchanged(self):
        # Simple addition
        self.app._on_keypad_press("25")
        self.app._on_keypad_press("Next Slot (→)")
        self.app._on_keypad_press("75")
        self.app.template_grid_model.rows[0].description_columns[0] = "dollars"
        self.app.calculate()

        self.assertEqual(self.app.result_var.get(), "100")
        self.assertEqual(self.app.result_word_var.get(), "100 dollars")

    def test_future_annotations_present_in_token_model(self):
        token_model_path = _PROJECT_ROOT / "addition_tokens" / "token_model.py"
        with open(token_model_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Find module docstring end
        doc_end_idx = None
        for i, line in enumerate(lines):
            if '"""' in line and i > 0:
                doc_end_idx = i
                break
        self.assertIsNotNone(doc_end_idx, "Module docstring closing not found")
        # Ensure 'from __future__ import annotations' appears directly after docstring
        subsequent_code = "".join(lines[doc_end_idx + 1:doc_end_idx + 10])
        self.assertIn("from __future__ import annotations", subsequent_code)

    def test_physical_enter_key_respects_active_input_target(self):
        # 1. When Pasted Preview is selected, physical Enter previews expression (does NOT calculate grid)
        self.app.select_pasted_preview()
        self.assertEqual(self.app.active_input_target, "pasted_preview")
        self.app.pasted_expr_var.set("(10 + 20) + 30")

        # Simulate physical Enter key press
        res = self.app._on_enter_key()
        self.assertEqual(res, "break")

        # Expression is previewed in Row 1 Column 1
        row = self.app.template_grid_model.rows[0]
        self.assertIsNotNone(row.template_instance)
        self.assertEqual(row.template_instance.template.pattern, "( □ + □ ) + □")
        self.assertEqual([s.value for s in row.template_instance.slots], ["10", "20", "30"])

        # Input target automatically transitioned to grid
        self.assertEqual(self.app.active_input_target, "grid")
        # Grid has NOT been calculated yet
        self.assertEqual(self.app.result_var.get(), "")

        # 2. When grid is selected, physical Enter calculates normally
        row.description_columns[0] = "apples"
        res_calc = self.app._on_enter_key()
        self.assertEqual(res_calc, "break")
        self.assertEqual(self.app.result_var.get(), "60")
        self.assertEqual(self.app.result_word_var.get(), "60 apples")

    def test_save_duplicate_of_builtin_template_does_not_convert_to_custom(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_storage = Path(tmp_dir) / "custom_templates.json"
            mgr = MathTemplateManager(storage_file=tmp_storage)

            # Built-in template '□ + □' exists with is_custom=False
            builtin = next(t for t in mgr.templates if t.pattern == "□ + □")
            self.assertFalse(builtin.is_custom)
            initial_count = len(mgr.templates)

            # Attempt to save a duplicate of the built-in template
            duplicate = MathTemplate(
                template_id="custom_duplicate",
                pattern="□ + □",
                name="Duplicate Two terms",
                is_custom=True,
            )
            mgr.save_custom_template(duplicate)

            # Built-in template definition is retained and NOT converted to custom
            self.assertFalse(builtin.is_custom)
            self.assertEqual(len(mgr.templates), initial_count)

            # JSON storage file does not persist the built-in template
            if tmp_storage.exists():
                with open(tmp_storage, "r", encoding="utf-8") as f:
                    stored_data = json.load(f)
                self.assertFalse(any(item["pattern"] == "□ + □" for item in stored_data))

            # Test through GUI: saving '1 + 2' reuses built-in '□ + □' without converting
            self.app.template_manager = mgr
            self.app.pasted_expr_var.set("1 + 2")
            self.app._on_save_custom_template()

            applied_template = self.app.template_grid_model.rows[0].template_instance.template
            self.assertEqual(applied_template.pattern, "□ + □")
            self.assertFalse(applied_template.is_custom)
            inspector_msg = self.app.inspector_text.get("1.0", "end")
            self.assertIn("existing built-in template", inspector_msg)



class TestDualModelCleanupAndEditingProjection(unittest.TestCase):
    """
    Verification tests for single source of truth (TemplateGridModel)
    and non-validating editing projections vs strict evaluation:
    1. to_editing_token_stream non-validating projection preserves incomplete [5] + [□].
    2. to_token_stream strict validation raises ValueError on empty [□].
    3. Mathematical keypad inputs (0-9, .) do not mutate TokenGridModel in template mode.
    4. Keypad '+' button in Column 1 advances to the next slot without appending '+' to TokenGridModel.
    5. Keypad '+' button at the last slot does not advance into Column 2 and does not mutate slot.
    6. Keypad parentheses in Column 1 display informational notice and do not mutate TokenGridModel.
    7. rows_tokens in template mode returns non-validating editing tokens from TemplateGridModel.
    8. delete_selected_column in template mode resets slot value back to empty □ without deleting row.
    9. Non-validating editing projection in inspector view works on incomplete templates without crashing.
    10. Strict validation in calculate() properly rejects incomplete templates with a clear error message.
    """
    @classmethod
    def setUpClass(cls):
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
            cls.gui_available = True
        except Exception:
            cls.gui_available = False

    @classmethod
    def tearDownClass(cls):
        if getattr(cls, "gui_available", False) and hasattr(cls, "root"):
            try:
                cls.root.destroy()
            except Exception:
                pass

    def setUp(self):
        if not self.gui_available:
            self.skipTest("Tkinter display not available")
        import tempfile
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.app = AdditionTokenCalculator(root=self.root, mode="template")
        self.app.template_manager.storage_file = Path(self.tmp_dir.name) / "custom_templates.json"

    def tearDown(self):
        self.app.clear()
        if hasattr(self, "tmp_dir"):
            self.tmp_dir.cleanup()

    def test_1_to_editing_token_stream_preserves_incomplete_template(self):
        tpl = MathTemplate(template_id="t1", pattern="□ + □", name="Two terms")
        inst = tpl.create_instance()
        inst.slots[0].value = "5"
        # Slot 1 is unfilled ("")
        editing_tokens = inst.to_editing_token_stream(["apples", "on the desk"])
        vals = [t.value for t in editing_tokens]
        self.assertEqual(vals, ["5", "apples", "on the desk", "+", "□", "apples", "on the desk"])
        self.assertEqual(editing_tokens[0].token_type, TokenType.NUMBER)
        self.assertEqual(editing_tokens[4].token_type, TokenType.UNKNOWN)
        self.assertEqual(editing_tokens[4].value, "□")
        self.assertEqual(editing_tokens[4].slot_id, inst.slots[1].slot_id)

    def test_2_to_token_stream_strictly_validates_unfilled_slots(self):
        tpl = MathTemplate(template_id="t1", pattern="□ + □", name="Two terms")
        inst = tpl.create_instance()
        inst.slots[0].value = "5"
        with self.assertRaises(ValueError) as ctx:
            inst.to_token_stream(["apples"])
        self.assertIn("is empty (□)", str(ctx.exception))

    def test_3_numeric_keypad_does_not_mutate_legacy_model(self):
        # Default row is template □ + □
        self.assertEqual(len(self.app.grid_model.rows[0].addend_columns[0].ordered_subcolumns), 0)
        self.app._on_keypad_press("5")
        self.app._on_keypad_press("7")
        # TemplateGridModel slot 0 has "57"
        row = self.app.template_grid_model.rows[0]
        self.assertEqual(row.template_instance.slots[0].value, "57")
        # TokenGridModel has NO tokens (0)
        self.assertEqual(len(self.app.grid_model.rows[0].addend_columns[0].ordered_subcolumns), 0)

    def test_4_keypad_plus_advances_slot_without_mutating_legacy_model(self):
        self.app._on_keypad_press("5")
        self.assertEqual(self.app.template_grid_model.cursor_slot, 0)
        self.app._on_keypad_press("+")
        # Cursor advanced to slot 1
        self.assertEqual(self.app.template_grid_model.cursor_slot, 1)
        # TokenGridModel has NOT received '+' or '5'
        self.assertEqual(len(self.app.grid_model.rows[0].addend_columns[0].ordered_subcolumns), 0)

    def test_5_keypad_plus_at_last_slot_does_not_advance_to_col2(self):
        self.app._on_keypad_press("5")
        self.app._on_keypad_press("+")
        self.app._on_keypad_press("9")
        self.assertEqual(self.app.template_grid_model.cursor_slot, 1)
        # Press '+' again when already on last slot
        self.app._on_keypad_press("+")
        # Still in Column 1 and slot 1
        self.assertEqual(self.app.template_grid_model.cursor_col, 1)
        self.assertEqual(self.app.template_grid_model.cursor_slot, 1)
        self.assertIn("All placeholder boxes (□) in this mathematical template have been reached",
                      self.app.inspector_text.get("1.0", "end"))

    def test_6_keypad_parentheses_show_notice_and_do_not_mutate_legacy(self):
        self.app._on_keypad_press("(")
        self.assertIn("Parentheses '(' define mathematical template structure",
                      self.app.inspector_text.get("1.0", "end"))
        self.assertEqual(len(self.app.grid_model.rows[0].addend_columns[0].ordered_subcolumns), 0)

    def test_7_rows_tokens_returns_non_validating_editing_tokens(self):
        self.app._on_keypad_press("5")
        # Slot 0 has "5", slot 1 has ""
        toks = self.app.rows_tokens
        self.assertEqual(len(toks), 1)
        tok_vals = [t.value for t in toks[0]]
        self.assertEqual(tok_vals, ["5", "+", "□"])

    def test_8_delete_selected_column_resets_slot_to_placeholder(self):
        self.app._on_keypad_press("5")
        self.app._on_keypad_press("+")
        self.app._on_keypad_press("9")
        self.assertEqual(self.app.template_grid_model.rows[0].template_instance.slots[1].value, "9")
        # Delete selected column (slot 1)
        self.app.delete_selected_column()
        self.assertEqual(self.app.template_grid_model.rows[0].template_instance.slots[1].value, "")
        self.assertEqual(self.app.template_grid_model.rows[0].template_instance.slots[0].value, "5")
        # The row remains intact
        self.assertEqual(len(self.app.template_grid_model.rows), 1)

    def test_9_inspector_view_projects_incomplete_templates_without_crashing(self):
        self.app._on_keypad_press("8")
        # Only slot 0 filled, slot 1 empty
        self.app.render_inspector(None)
        txt = self.app.inspector_text.get("1.0", "end")
        self.assertIn("Rep 1 (Ordered Subcolumns): ['8' | '+' | '□']", txt)
        self.assertIn("(No parsed terms)", txt)

    def test_10_calculate_strictly_validates_and_reports_error(self):
        self.app._on_keypad_press("8")
        # Attempt calculation with slot 1 unfilled
        res = self.app.calculate()
        self.assertIsNone(res)
        self.assertEqual(self.app.result_var.get(), "Error")
        self.assertIn("VALIDATION NOTICE: Calculation Not Completed", self.app.results_text.get("1.0", "end"))


if __name__ == "__main__":
    unittest.main()

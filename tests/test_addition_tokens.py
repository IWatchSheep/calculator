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
        self.app = AdditionTokenCalculator(root=self.root)

    def tearDown(self):
        self.app.clear()

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
        self.app = AdditionTokenCalculator(root=self.root)

    def tearDown(self):
        self.app.clear()

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


if __name__ == "__main__":
    unittest.main()

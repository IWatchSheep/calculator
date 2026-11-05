# Python Calculator

A desktop calculator project written in **Python** using **Tkinter**. Development is incremental: **numeric addition is complete**, and a separate **experimental word-enabled addition calculator** supports quantities, items, and descriptive context. **Subtraction is the next planned operation**; the other mathematics features below are not implemented yet.

## Project status

### Completed: Numeric addition calculator

**File:** `addition/addition.py`

- Adds two or more integers or decimal values.
- Supports parentheses `(` and `)` on the keypad and via physical keyboard.
- Connected to the shared expression evaluator `calculator_core/expression.py`.
- Supports additional input rows in a scrollable area while keeping the keypad anchored at the bottom.
- Supports keypad and keyboard input, Backspace, Clear, and continuing a calculation after a result.
- Uses Python's `decimal.Decimal` and operation-specific precision for finite-decimal addition.
- Displays small values in ordinary decimal notation rather than scientific notation.

### Completed: Expression evaluator & CLI

**File:** `calculator_core/expression.py`

- Evaluates addition expressions with arbitrary nested parentheses and dynamic finite-decimal precision.
- Command-line interface:
  ```powershell
  python -m calculator_core.expression "2 + (3 + 4)"
  ```
- Exits with status `0` on success and prints the result.
- Exits with status `1` on invalid expressions and writes an error message to `stderr`.

### Implemented (experimental): Word-enabled addition calculator

**File:** `addition_chat/addition.py`

This is a **separate Tkinter application** that combines numbers with item words and descriptions. Each addend row starts with **three columns**:

| Column | Purpose | Example |
| --- | --- | --- |
| 1 — Quantity | The number to add | `2` |
| 2 — Item | Choose an item from the dropdown or enter a custom word | `pens` |
| 3 — Description / Context | Choose or type where or how the item is described | `in the drawer` |

For example:

| Row | Quantity | Item | Description / Context |
| --- | ---: | --- | --- |
| 1 | 2 | pens | in the drawer |
| 2 | 3 | pens | in the drawer |

**Result:** `5 pens in the drawer`

The experimental app also includes:

- An editable **Item** dropdown with starter words and **+ Add to List** for custom items.
- An editable **Description / Context** dropdown with common phrases (such as `on the desk` and `in the drawer`) and **+ Add to List** for custom phrases.
- A **+ Column** button that creates another descriptive column in all existing addend rows and any rows added later.
- Summaries that take descriptions into account. For example:
  - `2 pens in the drawer + 3 pens on the desk` produces `5 pens (2 in the drawer, 3 on the desk)`.
  - `2 apples in the fridge + 3 oranges on the counter` produces `5 fruits (2 apples in the fridge, 3 oranges on the counter)` using the built-in category rules.
- A scrollable input area, a bottom-anchored keypad, typewriter-style text input, Clear, Backspace, and continuing addition after a result.

**Limitations:** The word-enabled application is an **offline, rule-based helper**, not a general-purpose AI chatbot. It only recognizes certain built-in word categories and cannot interpret arbitrary word problems or automatically convert between units (such as cents and dollars). Custom dropdown entries are maintained in the current running application and are not a permanent database.

### Planned next: Subtraction

**Subtraction is the next development goal.** It is **not implemented** in the current applications. The existing addition calculators and their tests should be preserved while subtraction is developed.

### Other planned mathematics

These are **future goals**, not completed features:

- Multiplication and division.
- Fractions: simplification, common denominators, and arithmetic operations.
- Additional decimal operations and place-value exercises.
- Percentages, ratios, and proportions.
- Pre-algebra 1 and 2; algebra 1 and 2, including word problems.
- Geometry.
- Potentially, more advanced text interpretation for word problems or an AI-powered chatbot (separate from the current rule-based feature).

## Requirements

- Python 3 with Tkinter available.
- A desktop environment or virtual display (such as `Xvfb` on headless Linux) that supports opening Tkinter windows.

The current applications use only Python's standard library; no additional Python packages are required.

## Run the calculators

Open a terminal in the project root (the folder containing `addition/`, `addition_chat/`, and `tests/`).

**Numeric addition calculator:**

```powershell
python addition/addition.py
```

**Experimental word-enabled addition calculator:**

```powershell
python addition_chat/addition.py
```

**Expression evaluator (command line):**

```powershell
python -m calculator_core.expression "2 + (3 + 4)"
```

## Run automated tests

The `tests/` folder contains **78 automated tests** across three test modules:

- `tests/test_calculator.py` — **36** tests for numeric addition, parentheses, dynamic decimal precision, automated GUI button clicks, physical keyboard event input, and keypad stability.
- `tests/test_expression.py` — **21** tests for the expression evaluation core, nested parentheses, precision, syntax errors, and the command-line interface.
- `tests/test_addition_chat.py` — **21** tests for word-enabled addition, context descriptions, extra columns, custom dropdown entries, and related input behavior.

### Run all tests from the project root

**Standard desktop session (Windows, macOS, or Linux with desktop):**

```powershell
python -m unittest discover -s tests -v
```

**Headless Linux / virtual desktop / CI environments:**

On systems with Xvfb installed, tests can be run using `xvfb-run`:

```bash
xvfb-run -a python -m unittest discover -s tests -v
```

Additionally, `tests/__init__.py` and `tests/test_calculator.py` include automatic virtual display startup (`pyvirtualdisplay` or `Xvfb`) if executed on a POSIX system without an active `$DISPLAY`.

A passing run ends with `OK`.

## Development approach

Make changes incrementally, starting from the current working code. Keep the original addition calculator intact while adding new operations. Preserve decimal precision, fixed-point output, bottom-anchored keypad behavior, and existing word/context features. Run the regression tests after every change, and add new tests for new functionality.

# Python Calculator

A desktop calculator project built with Python and Tkinter. The project is being developed incrementally: **addition is implemented**, including a separate experimental version that associates words with numbers. Other mathematical operations remain planned features.

## Project status

### Completed: Numeric addition calculator

**File:** `addition/addition.py`

- Adds two or more whole numbers and decimals.
- Adds input rows as needed, with a scrollable entry area and a bottom-anchored keypad.
- Supports mouse and keyboard input, Backspace, Clear, and continuing a calculation after a result.
- Uses `decimal.Decimal` with dynamically selected precision for finite-decimal addition.
- Displays small decimal answers in ordinary decimal notation instead of scientific notation.

### Implemented (experimental): Word-enabled addition calculator

**File:** `addition_chat/addition.py`

This is a **separate Tkinter app** that extends addition with optional word descriptions:

- Attach words to numbers using a dropdown list or custom typed words.
- Add custom words to the application's selectable options.
- Combine quantities of the same item, such as **3 apples + 2 apples = 5 apples**.
- Recognize certain related words using a built-in category list, such as **2 apples + 3 oranges = 5 fruits (2 apples, 3 oranges)**.
- Display a descriptive summary for different, unrelated items.

**Limitations:** This is an offline, rule-based word helper, **not a general-purpose AI chatbot**. It recognizes a limited set of categories, does not understand arbitrary word problems, and does not automatically convert between units (for example, cents and dollars). Custom word options are maintained in the running application; they are not a persistent word database.

### Not yet implemented: Other mathematics

The following are **development goals**, not features currently available in these apps.

#### Basic arithmetic and number skills

- Subtraction, multiplication, and division.
- Fractions: simplification, common denominators, addition, subtraction, multiplication, and division.
- More decimal operations and decimal place-value exercises.
- Percentages.
- Ratios, proportions, and related word problems.

#### More advanced mathematics

- Pre-algebra 1 and 2.
- Algebra 1 and 2, including word problems.
- Geometry.

#### Possible future text assistance

- More advanced text input and interpretation of mathematical word problems, potentially using an AI chatbot. This is a future idea, separate from the existing rule-based word-enabled addition app.

## Requirements

- Python 3 with Tkinter support.
- A desktop environment that can display Tkinter windows (such as Windows with PyCharm).

Both applications currently use the Python standard library; no extra Python packages are required.

## Run either calculator

Open a terminal in the project's main folder.

**Numeric addition calculator:**

```powershell
python addition/addition.py
```

**Experimental word-enabled addition calculator:**

```powershell
python addition_chat/addition.py
```

## Run automated tests

The `tests/` folder contains regression tests for both calculators:

- `tests/test_calculator.py` — numeric addition, decimal precision, input behavior, and keypad layout.
- `tests/test_addition_chat.py` — word-enabled addition, categories, and related interface behavior.

From the project root, run:

```powershell
python -m unittest discover -s tests -v
```

These tests create Tkinter windows, so they require a working graphical desktop. The current test suite contains **27 tests** (16 numeric calculator tests and 11 word-enabled calculator tests).

## Development approach

New capabilities should be added incrementally without undoing completed functionality. Run the existing tests after each change, and preserve the precision, formatting, and keypad-layout corrections in both applications.

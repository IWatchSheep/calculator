# Python Calculator

A Python calculator project built with Tkinter. The goal is to develop the calculator gradually, starting with addition and expanding to other areas of mathematics.

## Project status

**Completed: Addition calculator**

The addition calculator is implemented in `addition/addition.py`. It currently supports:

- Adding two or more numbers, including whole numbers and decimals.
- Adding more input fields as needed.
- A graphical keypad and keyboard input.
- Editing entries with Backspace and clearing the calculator.
- Continuing a calculation after displaying a result.
- Accurate finite-decimal addition using Python's `decimal.Decimal` with precision chosen for the inputs.
- Displaying small decimal results in standard decimal notation rather than scientific notation.
- A scrollable input area with the keypad anchored at the bottom when more addends are added.
- nlp to add words to addition calculator

**Not yet implemented:** The other arithmetic operations and mathematics topics below are future goals, not features of the current application.

## Planned features

### Basic arithmetic and number skills

- Subtraction, multiplication, and division.
- Fractions: simplification, common denominators, addition, subtraction, multiplication, and division.
- Decimal place value, along with subtraction, multiplication, and division of decimals.
- Percentages.
- Ratios and proportions, including word problems.

### More advanced mathematics

- Pre-algebra 1 and 2.
- Algebra 1.
- Geometry.
- Algebra 2.
- Algebra word problems.

### Possible future text-based assistance

- Explore adding a chatbot or text-input helper to interpret word problems, including ratio and proportion problems. This is a **future idea** and is not part of the current calculator.

## Requirements

- Python 3 with Tkinter support.
- A desktop environment capable of opening Tkinter windows.

The application uses Python's standard library and does not require additional Python packages.

## Run the addition calculator

From the project root, open a terminal and run:

```powershell
python addition/addition.py
```

## Run the regression tests

The project includes tests in `tests/test_calculator.py` for addition, decimal precision, input behavior, and keypad layout.

From the project root, run:

```powershell
python -m unittest discover -s tests -v
```

The tests require a graphical desktop because they create Tkinter windows.

## Development approach

New features will be added incrementally. Changes should preserve working addition functionality and keep the existing regression tests passing.

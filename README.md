# Calculator

A Python calculator with a graphical interface, mathematical operators, formulas, and operator pictures.

## Requirements

- Python 3
- Pillow

## Download and Run

1. Download the project from GitHub using Code > Download ZIP.
2. Extract the ZIP file.
3. Open the extracted folder in PyCharm.
4. Open the PyCharm terminal.
5. Install the required package:

   python -m pip install -r requirements.txt

6. Start the calculator:

   python main.py

## Project Files

- main.py - Main calculator application
- gui_style.py - GUI styling
- operator_links.py - Operator button connections
- operator_row_math/ - Operator row logic
- operators_one_operator_per_file/ - Mathematical operators and pictures
- picture_of_gui/ - GUI images

## Testing

Run the automated test suite (standard library only):

   python tests/test_operators.py

It checks all 507 operators: 446 working operators against hand-calculated answers, plus structure, error handling, input parsing, and the real calculator window for the newer physics operators (magnetism, fluid dynamics, quantum mechanics, optics, relativity). See TESTING_GUIDE.md for how to verify the calculator independently, including a manual GUI checklist.

Numerical results are checked to about 1e-6 and the GUI is only smoke-tested automatically, so independent verification is still welcome.

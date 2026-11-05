"""Addition expressions with parentheses and exact finite decimal results.

This is the initial shared arithmetic core. Subtraction is intentionally not
implemented yet. Existing Tkinter calculators are not changed.
"""

from decimal import Decimal, localcontext
import re
import sys

_TOKEN = re.compile(r"\s*(?:(\d+(?:\.\d*)?|\.\d+)|([()+]))")


def _tokens(expression: str) -> list[str]:
    if not isinstance(expression, str):
        raise TypeError("Expression must be a string")
    tokens = []
    index = 0
    while index < len(expression):
        if expression[index:].isspace():
            break
        match = _TOKEN.match(expression, index)
        if match is None:
            raise ValueError(f"Invalid character or number at position {index + 1}")
        tokens.append(match.group(1) or match.group(2))
        index = match.end()
    if not tokens:
        raise ValueError("Expression is empty")
    return tokens


def evaluate_addition(expression: str) -> str:
    """Evaluate addition and nested parentheses; return a plain decimal string.

    Examples: '2 + (3 + 4)' -> '9'; '0.1 + 0.2' -> '0.3'.
    Raises ValueError for invalid expressions. Minus is deliberately unsupported.
    """
    tokens = _tokens(expression)
    position = 0
    numbers = []

    def parse_term() -> Decimal:
        nonlocal position
        if position >= len(tokens):
            raise ValueError("Expected a number or opening parenthesis")
        token = tokens[position]
        position += 1
        if token == '(':
            value = parse_expression()
            if position >= len(tokens) or tokens[position] != ')':
                raise ValueError("Missing closing parenthesis")
            position += 1
            return value
        if token in ('+', ')'):
            raise ValueError("Expected a number or opening parenthesis")
        value = Decimal(token)
        numbers.append(value)
        return value

    def parse_expression() -> Decimal:
        nonlocal position
        value = parse_term()
        while position < len(tokens) and tokens[position] == '+':
            position += 1
            value += parse_term()
        return value

    # Parse syntax and capture values, then re-evaluate with enough precision.
    # This first pass is only for syntax checking: arithmetic happens after the
    # decimal context is sized, so it cannot silently round long numbers.
    # Using a nested function avoids maintaining a second tokenizer/parser.
    # To avoid rounding even during the first pass, set sufficient context from
    # numeric tokens before parsing.
    numeric_values = [Decimal(t) for t in tokens if t not in ('(', ')', '+')]
    if numeric_values:
        highest = max(v.adjusted() for v in numeric_values)
        lowest = min(v.as_tuple().exponent for v in numeric_values)
        precision = max(1, highest - lowest + len(numeric_values) + 2)
    else:
        precision = 1
    with localcontext() as context:
        context.prec = precision
        total = parse_expression()
        if position != len(tokens):
            raise ValueError("Unexpected token or unmatched closing parenthesis")
        result = format(total, 'f')
    if '.' in result:
        result = result.rstrip('0').rstrip('.')
    return '0' if result in ('', '-0') else result


def main(argv: list[str] | None = None) -> int:
    """Command-line interface to evaluate addition expressions with parentheses.

    Accepts an expression as command-line arguments, prints the result to
    standard output, and returns exit code 0. For invalid expressions, writes
    an error message to standard error and returns a non-zero exit code (1).
    """
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        sys.stderr.write("Usage: python -m calculator_core.expression \"<expression>\"\n")
        return 1
    expression = " ".join(argv).strip()
    try:
        result = evaluate_addition(expression)
        sys.stdout.write(f"{result}\n")
        return 0
    except Exception as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())

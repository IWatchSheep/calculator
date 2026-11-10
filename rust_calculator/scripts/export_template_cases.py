import json, sys
sys.path.insert(0, '.')
from operator_row_math import template_math as T
cases = ["(□ + 3) × 2", "(? + 3) * 2", "sqrt(16) + abs(-3)", "sqrt(x) + 4", "Time dilation(1, x)", "sin(pi / 2)", "2^3^2", "-5 + 2", "-x", "-2^2",
         "3 + 4 * 5", "(1 + 2", "1 +", "", "2 3", "foo(1)", "sqrt(1, 2)", "ln(e)", "min(1, 2) + max(3, 4)", "10 % 3", "2 × (3 + 4) ÷ 7", "x + y", "5", "pi",
         "Square root(9)", "square_root(9)", "1.5e-3 + .5", "log(100) - ln(10)", "factorial(5) / 2", "((1 + 2) × (3 + 4))", "1 $ 2", "a b c", "sqrt 9",
         "determinant(x)", "gcd(12, 18)", "floor(2.5) + ceil(2.5)"]
out = []
for c in cases:
    try:
        n = T.parse_math(c)
        out.append({"text": c, "ok": True, "describe": T.describe(n), "empty": T.empty_boxes(n)})
    except T.IncompleteMath as e:
        out.append({"text": c, "ok": False, "incomplete": True, "message": str(e)})
    except ValueError as e:
        out.append({"text": c, "ok": False, "incomplete": False, "message": str(e)})
json.dump(out, open('rust_calculator/tests/template_cases.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), sum(1 for o in out if o["ok"]))

"""The algebra word problems, one per wording, as a list the calculator can show.

Read from operators_one_algebra_word_problem_per_file/INDEX.md. Each item is one problem:
its category, id, text, Ready or Reference status, and the folder key (for example "savings/0848").
The diagram is <key>/<id>.jpg next to the problem file.
"""
import os


def load_catalog(index_path):
    """Every problem in INDEX.md, in file order. Empty if the index is not there."""
    if not os.path.exists(index_path):
        return []
    items = []
    category = ""
    with open(index_path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("## "):
                category = line[3:].strip()
                continue
            if not line.startswith("|"):
                continue
            parts = [p.strip() for p in line.strip().strip("|").split("|")]
            if len(parts) != 6 or not (len(parts[0]) == 4 and parts[0].isdigit()):
                continue
            folder = parts[5].strip("`").strip("/")
            items.append({
                "category": category,
                "id": parts[0],
                "problem": parts[1],
                "status": parts[3],
                "key": folder,
            })
    return items


def diagram_path(library_root, item):
    """The jpg drawn for this problem."""
    return os.path.join(library_root, item["key"], item["id"] + ".jpg")
"""Fail CI on unresolved citations/references even if LaTeX produced a PDF."""
from pathlib import Path
import argparse
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("document", nargs="?", default="main",
                    choices=("main", "proposal", "presentation"))
document = parser.parse_args().document
pdf = Path(f"{document}.pdf")
if not pdf.is_file() or pdf.stat().st_size == 0:
    raise SystemExit(f"{pdf} was not produced.")
patterns = (
    r"(?:Citation|Reference)\b[^\n]*\bundefined",
    r"There were undefined (?:references|citations)",
    r"Please \(re\)run Biber",
    r"Rerun to get cross-references right",
    r"Please rerun LaTeX",
    r"I didn't find a database entry",
    r"^.*\bERROR\s*-",
)
errors = []
for filename in (f"{document}.log", f"{document}.blg"):
    path = Path(filename)
    if not path.is_file():
        errors.append(f"Missing build log: {filename}")
        continue
    content = path.read_text(encoding="utf-8", errors="replace")
    for pattern in patterns:
        errors.extend(f"{filename}: {match.group(0)}" for match in
                      re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE))
if errors:
    raise SystemExit("\n".join(errors))
print(f"{pdf}: built; citations and cross-references resolved.")

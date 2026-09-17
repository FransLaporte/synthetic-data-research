"""Fail CI on unresolved citations/references even if LaTeX produced a PDF."""
from pathlib import Path
import re

pdf = Path("main.pdf")
if not pdf.is_file() or pdf.stat().st_size == 0:
    raise SystemExit("main.pdf was not produced.")
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
for filename in ("main.log", "main.blg"):
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
print("PDF built; citations and cross-references resolved.")

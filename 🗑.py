import csv
import json
from pathlib import Path

_M = Path.cwd().resolve()
TRASH = "🗑"
IDCSV = "ids.csv"
j = _M / "🗑.json"


def _O():
    a: list[int] = []
    b: list[int] = []
    c = _M / IDCSV
    with c.open(encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        for f in reader:
            if f[1] == TRASH:
                b.append(int(f[0]))
            else:
                a.append(int(f[0]))
    return a, b


def main():
    a: list[int] = json.loads(j.read_text("utf-8"))
    b, c = _O()
    for d in c:
        a.append(d)
    j.write_text(json.dumps(sorted(set(a)), indent="\t"))


if __name__ == "__main__":
    main()

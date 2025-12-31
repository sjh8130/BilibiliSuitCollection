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
    f = j.read_text("utf-8")
    a: list[int] = json.loads(f)
    b, c = _O()
    a.extend(c)
    g = json.dumps(sorted(set(a)), indent="\t")
    if g == f:
        return
    j.write_text(g)


if __name__ == "__main__":
    main()

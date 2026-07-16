import json
import sys
from pathlib import Path

import tqdm


def _main(path: Path) -> None:
    with path.open(encoding="utf-8") as fp:
        item: dict = json.load(fp)

    with path.open("w", encoding="utf-8") as fp:
        json.dump(item, fp, ensure_ascii=False, separators=(",", ":"), indent="\t")


if __name__ == "__main__":
    files = sys.argv[1:]
    try:
        for file in tqdm.tqdm(files):
            p = Path(file)
            if p.is_dir():
                for pp in p.iterdir():
                    _main(pp)
            else:
                _main(p)
    except Exception as e:  # ruff:ignore[blind-except]
        import time

        print(e)
        time.sleep(10)

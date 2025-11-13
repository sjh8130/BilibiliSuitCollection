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
    try:
        files = sys.argv[1:]
        for file in tqdm.tqdm(files):
            _main(Path(file))
    except Exception as e:  # noqa: BLE001
        import time

        print(e)
        time.sleep(10)
    finally:
        pass

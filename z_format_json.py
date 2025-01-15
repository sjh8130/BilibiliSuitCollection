import json
import sys


def _main(path: str):
    with open(path, "r", encoding="utf-8") as fp:
        item: dict = json.load(fp)

    with open(path, "w", encoding="utf-8") as fp:
        json.dump(item, fp, ensure_ascii=False, separators=(",", ":"), indent="\t")


if __name__ == "__main__":
    try:
        files = sys.argv[1:]
        for file in files:
            _main(file)
    except Exception:
        import time

        time.sleep(10)
    finally:
        pass

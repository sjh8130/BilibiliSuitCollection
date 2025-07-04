import json
import sys
from collections.abc import Iterable
from pathlib import Path

from loguru import logger
from tqdm import tqdm

from a import OPR, del_keys, replace_str, sort_list_dict

log = logger.bind(user="S.ei")


def _p_main(item: dict) -> None:
    # print(item["id"])
    del_keys(item, "suggest", [""])
    del_keys(item, "flags", {})
    del_keys(item, "flags", {"no_access": True, "unlocked": False})
    del_keys(item, "flags", {"no_access": True})
    del_keys(item, "activity", None, OPR.ANY)
    del_keys(item, "sale_promo", None, OPR.ANY)
    del_keys(item, "label", None)
    del_keys(item, "attr", 0)
    del_keys(item, "package_sub_title", "")
    del_keys(item, "ref_mid", 0)
    del_keys(item, "resource_type", 0)
    if "emote" in item:
        sort_list_dict(item["emote"], "id", "text")
    replace_str(item, "http://", "https://")
    replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "fasle", "false")


def _main(path: Path) -> None:
    src = path.read_text("utf-8")
    item: dict = json.loads(src)
    _p_main(item)
    target = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if src == target:
        return
        print(f"EQ:{path}")
    path.write_text(target, encoding="utf-8")


def _N(path: Path) -> Iterable[Path]:
    return path.glob("*.json")


if __name__ == "__main__":
    try:
        for file in tqdm(_N(Path.cwd() / "emoji") if len(sys.argv) <= 1 else [Path(x) for x in sys.argv[1:]]):
            _main(file)
    except Exception as e:
        log.exception(str(file))  # type: ignore
        log.exception(e)
    finally:
        pass

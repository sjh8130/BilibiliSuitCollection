import json
import sys
from enum import StrEnum, auto

from loguru import logger

log = logger.bind(user="S.e")


def sort_list_dict(old_list: list[dict]) -> list[dict]:
    return sorted(old_list, key=lambda x: x["id"])


class OPR(StrEnum):
    EQ = auto()
    NEQ = auto()
    GT = auto()
    LT = auto()
    GEQ = auto()
    LEQ = auto()
    ANY = auto()
    IN = auto()
    INEQ = auto()
    NIN = auto()
    IS = auto()
    NIS = auto()


def _del_keys(d: dict, k: str, v, operator: OPR = OPR.EQ, recursive=True):
    if k in d and d.get(k) == v:
        d.pop(k)
    if not recursive:
        return
    for key in d:
        if isinstance(d[key], dict):
            _del_keys(d[key], k, v)
        if isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    _del_keys(item, k, v)


def _main(path):
    with open(path, encoding="utf-8") as fp:
        src = fp.read()
        item: dict = json.loads(src)
    print(item["id"])
    _del_keys(item, "suggest", [""])
    _del_keys(item, "flags", {})
    _del_keys(item, "flags", {"no_access": True, "unlocked": False})
    _del_keys(item, "flags", {"no_access": True})
    _del_keys(item, "activity", None)
    _del_keys(item, "label", None)
    _del_keys(item, "attr", 0)
    _del_keys(item, "package_sub_title", "")
    _del_keys(item, "ref_mid", 0)
    _del_keys(item, "resource_type", 0)
    if "emote" in item:
        item["emote"] = sort_list_dict(item["emote"])
    target = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if src == target:
        return
        print(f"EQ:{path}")
    else:
        pass
        print(f"NEQ:{path}")
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(target)


if __name__ == "__main__":
    try:
        files = sys.argv[1:]
        for file in files:
            _main(file)
    except Exception as e:
        log.exception(e)
        import time

        time.sleep(20)

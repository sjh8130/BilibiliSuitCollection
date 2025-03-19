import json
import os
import sys

from loguru import logger
from tqdm import tqdm

from a import OPR, del_keys, sort_list_dict

log = logger.bind(user="S.ei")


def _p_main(item: dict):
    print(item["id"])
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
        sort_list_dict(item["emote"])


def _main(path: str):
    with open(path, encoding="utf-8") as fp:
        src = fp.read()
        item: dict = json.loads(src)
    _p_main(item)
    target = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if src == target:
        return
        print(f"EQ:{path}")
    else:
        ...
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(target)


def walk_dir(path):
    walk_result = os.walk(os.path.join(base_path, path))
    ret_list = []
    for r in walk_result:
        for p in r[2]:
            if p == "ids.csv":
                continue
            ret_list.append(os.path.join(base_path, path, p))
    return ret_list


if __name__ == "__main__":
    base_path = os.path.abspath(".")
    t_list: list[str] = walk_dir("emoji") if len(sys.argv) <= 1 else sys.argv[1:]
    try:
        for file in tqdm(t_list):
            _main(file)
    except Exception as e:
        log.exception(e)

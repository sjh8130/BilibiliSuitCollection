import glob
import json
import os
import sys

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


def _main(path: str) -> None:
    with open(path, encoding="utf-8") as fp:
        src = fp.read()
        item: dict = json.loads(src)
    _p_main(item)
    target = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if src == target:
        return
        print(f"EQ:{path}")
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(target)


def _N(path: str) -> list[str]:
    ret_list = []
    for r in glob.glob("*.json", root_dir=os.path.join(base_path, path)):
        ret_list.append(os.path.join(base_path, path, r))
    return ret_list


if __name__ == "__main__":
    base_path = os.path.abspath(".")
    t_list: list[str] = _N("emoji") if len(sys.argv) <= 1 else sys.argv[1:]
    try:
        for file in tqdm(t_list):
            _main(file)
    except Exception as e:
        log.exception(file)
        log.exception(e)
    finally:
        pass

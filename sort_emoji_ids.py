import json
import sys

from loguru import logger

log = logger.bind(user="S")


def sort_list_dict(old_list: list[dict]) -> list[dict]:
    return sorted(old_list, key=lambda x: x["id"])


def _del_keys_anyway(d: dict, k: str, r=True):
    if k in d:
        d.pop(k)
    for key in d:
        if isinstance(d[key], dict):
            _del_keys_anyway(d[key], k, r)
        elif isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    _del_keys_anyway(item, k, r)


def _del_keys_if_eq_value(d: dict, k: str, v, r=True):
    if k in d and d.get(k) == v:
        d.pop(k)
    if not r:
        return
    for key in d:
        if isinstance(d[key], dict):
            _del_keys_if_eq_value(d[key], k, v)
        if isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    _del_keys_if_eq_value(item, k, v)


def _main(path):
    with open(path, encoding="utf-8") as fp:
        item: dict = json.load(fp)
    print(item["id"])
    _del_keys_if_eq_value(item, "suggest", [""])
    _del_keys_if_eq_value(item, "flags", {})
    _del_keys_if_eq_value(item, "activity", None)
    _del_keys_if_eq_value(item, "label", None)
    _del_keys_if_eq_value(item, "package_sub_title", "")
    if "emote" in item:
        item["emote"] = sort_list_dict(item["emote"])
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(item, fp, ensure_ascii=False, separators=(",", ":"), indent="\t")


if __name__ == "__main__":
    try:
        files = sys.argv[1:]
        for file in files:
            _main(file)
    except Exception as e:
        log.exception(e)
        import time

        time.sleep(20)

import json
import os
import sys
import time
from enum import StrEnum, auto

from loguru import logger
from tqdm import tqdm

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


def _replace_str(d_l: dict | list, k_i: int | str, old_v, new_v, recursive=True):
    if k_i in d_l and isinstance(d_l, dict) and isinstance(d_l[k_i], str):
        d_l[k_i].replace(old_v, new_v)
    elif isinstance(d_l, list) and isinstance(k_i, int) and len(d_l) >= k_i:
        d_l[k_i] = d_l[k_i].replace(old_v, new_v)
        return
    if not recursive:
        return
    for key in d_l:
        if isinstance(d_l[key], dict):
            _replace_str(d_l[key], k_i, old_v, new_v, recursive)
        elif isinstance(d_l[key], list):
            for index, item in enumerate(d_l[key]):
                if isinstance(item, dict):
                    _replace_str(item, k_i, old_v, new_v, recursive)
                elif isinstance(item, str):
                    _replace_str(d_l[key], k_i, old_v, new_v, False)


def _del_keys(d: dict, k: str, v, operator: OPR = OPR.EQ, recursive=True):
    if (
        k in d
        and isinstance(d, dict)
        and (type(d[k]) is type(v) or operator in (OPR.IN, OPR.INEQ, OPR.ANY))
    ):
        match operator:
            case OPR.EQ:
                if d.get(k) == v:
                    d.pop(k)
            case OPR.IN | OPR.INEQ:
                if d.get(k) in v:  # type:ignore[reportOperatorIssue]
                    d.pop(k)
            case OPR.ANY:
                d.pop(k)
            case OPR.GT:
                if d.get(k) > v:  # type: ignore[reportOptionalOperand]
                    d.pop(k)
            case OPR.LT:
                if d.get(k) < v:  # type: ignore[reportOptionalOperand]
                    d.pop(k)
            case OPR.GEQ:
                if d.get(k) >= v:  # type: ignore[reportOptionalOperand]
                    d.pop(k)
            case OPR.LEQ:
                if d.get(k) <= v:  # type: ignore[reportOptionalOperand]
                    d.pop(k)
            case OPR.NEQ:
                if d.get(k) != v:
                    d.pop(k)
            case OPR.NIN:
                if d.get(k) not in v:  # type:ignore[reportOperatorIssue]
                    d.pop(k)
            case OPR.IS:
                if d.get(k) is v:
                    d.pop(k)
            case OPR.NIS:
                if d.get(k) is not v:
                    d.pop(k)
            case _:
                raise "*ToDo"
    if not recursive:
        return
    for key in d:
        if isinstance(d[key], dict):
            _del_keys(d[key], k, v, operator, recursive)
        elif isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    _del_keys(item, k, v, operator, recursive)


def _p_main(item: dict):
    print(item["id"])
    _del_keys(item, "suggest", [""])
    _del_keys(item, "flags", {})
    _del_keys(item, "flags", {"no_access": True, "unlocked": False})
    _del_keys(item, "flags", {"no_access": True})
    _del_keys(item, "activity", None, OPR.ANY)
    _del_keys(item, "sale_promo", None, OPR.ANY)
    _del_keys(item, "label", None)
    _del_keys(item, "attr", 0)
    _del_keys(item, "package_sub_title", "")
    _del_keys(item, "ref_mid", 0)
    _del_keys(item, "resource_type", 0)
    if "emote" in item:
        item["emote"] = sort_list_dict(item["emote"])


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
    time.sleep(20)

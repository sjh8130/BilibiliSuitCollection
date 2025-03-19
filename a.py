import json
from enum import IntEnum, auto


class OPR(IntEnum):
    EQ = auto()
    NEQ = auto()
    GT = auto()
    LT = auto()
    GEQ = auto()
    LEQ = auto()
    ANY = auto()
    IN = auto()
    NIN = auto()
    IS = auto()
    NIS = auto()


def sort_str_list(s: str, /) -> str:
    """example: `'1,3,2,4,5'` -> `'1,2,3,4,5'`"""
    if s.count(",") == 0:
        return s
    a = json.loads(f"[{s}]")
    b = sorted(a)
    return ",".join(str(c) for c in b)


def sort_list_dict(
    ld: list[dict],
    k1: str = "item_id",
    k2: str = "name",
) -> list[dict]:
    items_with_k1 = [item for item in ld if item[k1] not in [0, "0"]]
    items_with_k2 = [item for item in ld if item[k1] in [0, "0"]]
    items_with_k1.sort(key=lambda x: x[k1])
    items_with_k2.sort(key=lambda x: x[k2])
    ld[:] = items_with_k1 + items_with_k2
    return items_with_k1 + items_with_k2


def sort_p6_emoji(ld: list[dict], /) -> list[dict]:
    for i in range(len(ld)):
        if isinstance(ld[i].get("properties"), dict):
            if isinstance(ld[i]["properties"].get("item_ids"), str):
                ld[i]["properties"]["item_ids"] = sort_str_list(ld[i]["properties"]["item_ids"])
        sort_list_dict(ld[i]["items"])
    return ld


def del_keys(d: dict, k: str, v=None, operator: OPR = OPR.EQ, recursive=True):
    if isinstance(d, dict) and k in d and (type(d[k]) is type(v) or operator in (OPR.IN, OPR.ANY)):
        match operator:
            case OPR.EQ:
                if d.get(k) == v:
                    d.pop(k)
            case OPR.IN | OPR.ANY:
                d.pop(k, None)
            case OPR.GT:
                if isinstance(d[k], (int, float)) and d[k] > v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.LT:
                if isinstance(d[k], (int, float)) and d[k] < v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.GEQ:
                if isinstance(d[k], (int, float)) and d[k] >= v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.LEQ:
                if isinstance(d[k], (int, float)) and d[k] <= v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.NEQ:
                if d.get(k) != v:
                    d.pop(k)
            case OPR.NIN:
                if d[k] not in v:
                    d.pop(k)
            case OPR.IS:
                if d.get(k) is v:
                    d.pop(k)
            case OPR.NIS:
                if d.get(k) is not v:
                    d.pop(k)
            case _:
                raise Exception("*ToDo")
    if not recursive:
        return
    for key in d:
        if isinstance(d[key], dict):
            del_keys(d[key], k, v, operator, recursive)
        elif isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    del_keys(item, k, v, operator, recursive)


def replace_value_in_list_dict(
    d_or_l: dict | list,
    k_or_i: int | str,
    old_v,
    new_v,
    recursive=True,
):
    if (k_or_i in d_or_l and isinstance(d_or_l, dict) and isinstance(d_or_l[k_or_i], str)) or (
        isinstance(d_or_l, list) and isinstance(k_or_i, int) and len(d_or_l) >= k_or_i
    ):
        if d_or_l[k_or_i] == old_v:  # type:ignore
            d_or_l[k_or_i] = d_or_l[k_or_i] = new_v  # type:ignore
    if not recursive:
        return
    for key in d_or_l:
        if isinstance(d_or_l[key], dict):
            replace_value_in_list_dict(d_or_l[key], k_or_i, old_v, new_v, recursive)
        elif isinstance(d_or_l[key], list):
            for index, item in enumerate(d_or_l[key]):
                if isinstance(item, dict):
                    replace_value_in_list_dict(item, k_or_i, old_v, new_v, recursive)
                elif isinstance(item, list):
                    replace_value_in_list_dict(d_or_l[key], k_or_i, old_v, new_v, recursive)

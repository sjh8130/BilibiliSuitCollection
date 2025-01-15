from enum import StrEnum
import json
import sys

_EMPTY_FAN_USER = {"mid": 0, "nickname": "", "avatar": ""}
_EMPTY_ACTIVITY_ENTRANCE = {"id": 0, "item_id": 0, "title": "", "image_cover": "", "jump_link": ""}


def _sort_str_list(s: str) -> str:
    """example: '1,3,2,4,5' -> '1,2,3,4,5'"""
    if s.count(",") == 0:
        return s
    a = json.loads(f"[{s}]")
    b = sorted(a)
    return ",".join(str(c) for c in b)


def _sort_list_dict(ld: list[dict], k1: str, k2: str) -> list[dict]:
    items_with_k1 = [item for item in ld if item[k1] not in [0, "0"]]
    items_with_k2 = [item for item in ld if item[k1] in [0, "0"]]
    items_with_k1.sort(key=lambda x: x[k1])
    items_with_k2.sort(key=lambda x: x[k2])
    return items_with_k1 + items_with_k2


def _sort_p6_emoji(ld: list[dict]) -> list[dict]:
    for i in range(len(ld)):
        if isinstance(ld[i].get("properties"), dict):
            if isinstance(ld[i]["properties"].get("item_ids"), str):
                ld[i]["properties"]["item_ids"] = _sort_str_list(ld[i]["properties"]["item_ids"])
        ld[i]["items"] = _sort_list_dict(ld[i]["items"], "item_id", "name")
    return ld


def _del_keys_anyway(d: dict, k: str, r=True):
    if k in d:
        d.pop(k)
    if not r:
        return
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


class OPR(StrEnum):
    EQ = "=="
    NEQ = "!="
    GT = ">"
    LT = "<"
    GEQ = ">="
    LEQ = "<="


def _del_keys_if_int_cmp(d: dict, k: str, v: int, opr: OPR, r=True):
    if k in d and isinstance(d[k], int):
        match opr:
            case OPR.EQ:
                if d.get(k) == v:
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
    if not r:
        return
    for key in d:
        if isinstance(d[key], dict):
            _del_keys_if_int_cmp(d[key], k, v, opr)
        if isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    _del_keys_if_int_cmp(item, k, v, opr)


def _main(path: str):
    with open(path, "r", encoding="utf-8") as fp:
        item: dict = json.load(fp)
    s1 = len(item)
    if item.get("suit_items") is None:
        return
    print(item["item_id"])
    match item["part_id"]:
        case 1:
            ...
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            if isinstance(item.get("properties"), dict):
                if isinstance(item["properties"].get("item_ids"), str):
                    item["properties"]["item_ids"] = _sort_str_list(item["properties"]["item_ids"])
            if isinstance(item.get("suit_items"), dict):
                if isinstance(item["suit_items"].get("emoji"), list):
                    item["suit_items"]["emoji"] = _sort_list_dict(item["suit_items"]["emoji"], "item_id", "name")
        case 6:
            if isinstance(item.get("properties"), dict):
                if isinstance(item["properties"].get("fan_item_ids"), str):
                    item["properties"]["fan_item_ids"] = _sort_str_list(item["properties"]["fan_item_ids"])
            if isinstance(item.get("suit_items"), dict):
                if isinstance(item["suit_items"].get("card"), list):
                    item["suit_items"]["card"] = _sort_list_dict(item["suit_items"]["card"], "item_id", "name")
                if isinstance(item["suit_items"].get("card_bg"), list):
                    item["suit_items"]["card_bg"] = _sort_list_dict(item["suit_items"]["card_bg"], "item_id", "name")
                if isinstance(item["suit_items"].get("loading"), list):
                    item["suit_items"]["loading"] = _sort_list_dict(item["suit_items"]["loading"], "item_id", "name")
                if isinstance(item["suit_items"].get("pendant"), list):
                    item["suit_items"]["pendant"] = _sort_list_dict(item["suit_items"]["pendant"], "item_id", "name")
                if isinstance(item["suit_items"].get("play_icon"), list):
                    item["suit_items"]["play_icon"] = _sort_list_dict(item["suit_items"]["play_icon"], "item_id", "name")
                if isinstance(item["suit_items"].get("skin"), list):
                    item["suit_items"]["skin"] = _sort_list_dict(item["suit_items"]["skin"], "item_id", "name")
                if isinstance(item["suit_items"].get("space_bg"), list):
                    item["suit_items"]["space_bg"] = _sort_list_dict(item["suit_items"]["space_bg"], "item_id", "name")
                if isinstance(item["suit_items"].get("thumbup"), list):
                    item["suit_items"]["thumbup"] = _sort_list_dict(item["suit_items"]["thumbup"], "item_id", "name")
                if isinstance(item["suit_items"].get("emoji_package"), list):
                    item["suit_items"]["emoji_package"] = _sort_p6_emoji(item["suit_items"]["emoji_package"])
        case 7:
            ...
        case 8:
            ...
        case 9:
            ...
        case 10:
            ...
        case 11:
            ...
        case 12:
            ...
        case 13:
            ...
        case _:
            ...
    _del_keys_if_eq_value(item, "activity_entrance", _EMPTY_ACTIVITY_ENTRANCE, False)
    _del_keys_if_eq_value(item, "fan_user", _EMPTY_FAN_USER, False)
    _del_keys_if_eq_value(item, "suit_items", {})
    _del_keys_anyway(item, "current_activity")
    _del_keys_anyway(item, "current_sources")
    _del_keys_anyway(item, "gray_rule_type")
    _del_keys_anyway(item, "gray_rule")
    _del_keys_anyway(item, "hot")
    _del_keys_anyway(item, "item_stock_surplus")
    _del_keys_anyway(item, "next_activity")
    _del_keys_anyway(item, "open_platform_vip_discount")
    _del_keys_anyway(item, "sale_count_desc")
    _del_keys_anyway(item, "sale_left_time")
    _del_keys_anyway(item, "sale_surplus")
    _del_keys_anyway(item, "sale_time_end", False)
    _del_keys_anyway(item, "state")
    _del_keys_anyway(item, "tag")
    _del_keys_anyway(item, "total_count_desc")
    _del_keys_if_eq_value(item, "activity_entrance", None, False)
    _del_keys_if_eq_value(item, "associate_words", "")
    _del_keys_if_eq_value(item, "items", None)
    _del_keys_if_eq_value(item, "jump_link", "")
    _del_keys_if_eq_value(item, "ref_mid", "0")
    _del_keys_if_eq_value(item, "sales_mode", 0)
    _del_keys_if_eq_value(item, "suit_item_id", 0)
    _del_keys_if_eq_value(item, "unlock_items", None)
    _del_keys_if_int_cmp(item, "sale_time_end", 0, OPR.LEQ)
    if s1 != len(item):
        print("WARN:", item["item_id"])
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(item, fp, ensure_ascii=False, separators=(",", ":"), indent="\t")


if __name__ == "__main__":
    try:
        files = sys.argv[1:]
        for file in files:
            _main(file)
    finally:
        pass
    import time

    time.sleep(10)

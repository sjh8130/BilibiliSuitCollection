import json
import os
import sys
from enum import StrEnum, auto

from tqdm import tqdm

_EMPTY_FAN_USER = {"mid": 0, "nickname": "", "avatar": ""}
_EMPTY_ACTIVITY_ENTRANCE = {
    "id": 0,
    "item_id": 0,
    "title": "",
    "image_cover": "",
    "jump_link": "",
}


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
                ld[i]["properties"]["item_ids"] = _sort_str_list(
                    ld[i]["properties"]["item_ids"]
                )
        ld[i]["items"] = _sort_list_dict(ld[i]["items"], "item_id", "name")
    return ld


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


def _del_keys(d: dict, k: str, v=None, operator: OPR = OPR.EQ, recursive=True):
    if (
        k in d
        and isinstance(d, dict)
        and (type(d[k]) is type(v) or operator in (OPR.IN, OPR.INEQ, OPR.ANY))
    ):
        match operator:
            case OPR.EQ:
                if d.get(k) == v:
                    d.pop(k)
            case OPR.IN | OPR.INEQ | OPR.ANY:
                d.pop(k, None)
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
                    raise
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
    match item["part_id"]:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            if isinstance(item.get("properties"), dict):
                if isinstance(item["properties"].get("item_ids"), str):
                    item["properties"]["item_ids"] = _sort_str_list(
                        item["properties"]["item_ids"]
                    )
            if isinstance(item.get("suit_items"), dict):
                if isinstance(item["suit_items"].get("emoji"), list):
                    item["suit_items"]["emoji"] = _sort_list_dict(
                        item["suit_items"]["emoji"], "item_id", "name"
                    )
        case 6:
            if isinstance(item.get("properties"), dict):
                if isinstance(item["properties"].get("fan_item_ids"), str):
                    item["properties"]["fan_item_ids"] = _sort_str_list(
                        item["properties"]["fan_item_ids"]
                    )
            if isinstance(item.get("suit_items"), dict):
                if isinstance(item["suit_items"].get("card"), list):
                    item["suit_items"]["card"] = _sort_list_dict(
                        item["suit_items"]["card"], "item_id", "name"
                    )
                if isinstance(item["suit_items"].get("card_bg"), list):
                    item["suit_items"]["card_bg"] = _sort_list_dict(
                        item["suit_items"]["card_bg"], "item_id", "name"
                    )
                if isinstance(item["suit_items"].get("loading"), list):
                    item["suit_items"]["loading"] = _sort_list_dict(
                        item["suit_items"]["loading"], "item_id", "name"
                    )
                if isinstance(item["suit_items"].get("pendant"), list):
                    item["suit_items"]["pendant"] = _sort_list_dict(
                        item["suit_items"]["pendant"], "item_id", "name"
                    )
                if isinstance(item["suit_items"].get("play_icon"), list):
                    item["suit_items"]["play_icon"] = _sort_list_dict(
                        item["suit_items"]["play_icon"], "item_id", "name"
                    )
                if isinstance(item["suit_items"].get("skin"), list):
                    item["suit_items"]["skin"] = _sort_list_dict(
                        item["suit_items"]["skin"], "item_id", "name"
                    )
                if isinstance(item["suit_items"].get("space_bg"), list):
                    item["suit_items"]["space_bg"] = _sort_list_dict(
                        item["suit_items"]["space_bg"], "item_id", "name"
                    )
                if isinstance(item["suit_items"].get("thumbup"), list):
                    item["suit_items"]["thumbup"] = _sort_list_dict(
                        item["suit_items"]["thumbup"], "item_id", "name"
                    )
                if isinstance(item["suit_items"].get("emoji_package"), list):
                    item["suit_items"]["emoji_package"] = _sort_p6_emoji(
                        item["suit_items"]["emoji_package"]
                    )
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case 12:
            pass
        case 13:
            pass
        case _:
            pass
    _del_keys(item, "associate", operator=OPR.ANY)
    _del_keys(item, "current_activity", operator=OPR.ANY)
    _del_keys(item, "current_sources", operator=OPR.ANY)
    _del_keys(item, "gray_rule_type", operator=OPR.ANY)
    _del_keys(item, "gray_rule", operator=OPR.ANY)
    _del_keys(item, "hot", operator=OPR.ANY)
    _del_keys(item, "is_symbol", operator=OPR.ANY)
    _del_keys(item, "item_stock_surplus", operator=OPR.ANY)
    _del_keys(item, "next_activity", operator=OPR.ANY)
    _del_keys(item, "non_associate", operator=OPR.ANY)
    _del_keys(item, "open_platform_vip_discount", operator=OPR.ANY)
    _del_keys(item, "realname_auth", operator=OPR.ANY)
    _del_keys(item, "sale_count_desc", operator=OPR.ANY)
    _del_keys(item, "sale_left_time", operator=OPR.ANY)
    _del_keys(item, "sale_promo", operator=OPR.ANY)
    _del_keys(item, "sale_surplus", operator=OPR.ANY)
    _del_keys(item, "sale_time_end", recursive=False, operator=OPR.ANY)
    _del_keys(item, "state", operator=OPR.ANY)
    _del_keys(item, "tag", operator=OPR.ANY)
    _del_keys(item, "total_count_desc", operator=OPR.ANY)
    _del_keys(item, "activity_entrance", _EMPTY_ACTIVITY_ENTRANCE, recursive=False)
    _del_keys(item, "activity_entrance", None, recursive=False)
    _del_keys(item, "associate_words", "")
    _del_keys(item, "fan_user", _EMPTY_FAN_USER, recursive=False)
    _del_keys(item, "finish_sources", None)
    _del_keys(item, "items", None)
    _del_keys(item, "jump_link", "")
    _del_keys(item, "properties", {})
    _del_keys(item, "ref_mid", "0")
    _del_keys(item, "sale_time_end", 0, OPR.LEQ)
    _del_keys(item, "sales_mode", 0)
    _del_keys(item, "suit_item_id", 0)
    _del_keys(item, "suit_items", {})
    _del_keys(item, "tab_id", 0, OPR.EQ)
    _del_keys(item, "unlock_items", None)


def walk_dir(path):
    walk_result = os.walk(os.path.join(base_path, path))
    ret_list = []
    for r in walk_result:
        for p in r[2]:
            ret_list.append(os.path.join(base_path, path, p))
    return ret_list


def _main(path: str):
    with open(path, "r", encoding="utf-8") as fp:
        src = fp.read()
    if path.endswith(".jsonl"):
        target = ""
        for line in src.splitlines():
            item: dict = json.loads(line)
            _p_main(item)
            target += json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n"
    else:
        item: dict = json.loads(src)
        _p_main(item)
        target = json.dumps(
            item, ensure_ascii=False, separators=(",", ":"), indent="\t"
        )
    if src == target:
        return
        print(f"EQ:{path}")
    else:
        ...
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(target)


if __name__ == "__main__":
    base_path = os.path.abspath(".")
    t_list: list[str] = (
        (
            walk_dir("PART_5_表情包")
            + walk_dir("PART_6_main")
            + [
                "PART_10_加载动画.jsonl",
                "PART_11_进度条装扮.jsonl",
                "PART_12_test.jsonl",
                "PART_13_NFT.jsonl",
                "PART_1_头像框.jsonl",
                "PART_2_动态卡片.jsonl",
                "PART_3_点赞效果.jsonl",
                "PART_4_表情.jsonl",
                "PART_7_空间背景.jsonl",
                "PART_8_勋章.jsonl",
                "PART_9_皮肤.jsonl",
            ]
        )
        if len(sys.argv) <= 1
        else sys.argv[1:]
    )

    try:
        for file in tqdm(t_list):
            _main(file)
    finally:
        pass

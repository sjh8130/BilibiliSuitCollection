import glob
import json
import os
import sys

from loguru import logger
from tqdm import tqdm

from a import OPR, del_keys, replace_str, sort_list_dict, sort_p6_emoji, sort_str_list

log = logger.bind(user="S.i")

P = "properties"
S = "suit_items"
_EMPTY_FAN_USER = {"mid": 0, "nickname": "", "avatar": ""}
_EMPTY_ACTIVITY_ENTRANCE = {
    "id": 0,
    "item_id": 0,
    "title": "",
    "image_cover": "",
    "jump_link": "",
}


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
            if isinstance(item.get(P), dict):
                if isinstance(item[P].get("item_ids"), str):
                    item[P]["item_ids"] = sort_str_list(item[P]["item_ids"])
            if isinstance(item.get(S), dict):
                if isinstance(item[S].get("emoji"), list):
                    sort_list_dict(item[S]["emoji"])
        case 6:
            if isinstance(item.get(P), dict):
                if isinstance(item[P].get("fan_item_ids"), str):
                    item[P]["fan_item_ids"] = sort_str_list(item[P]["fan_item_ids"])
            if isinstance(item.get(S), dict):
                if isinstance(item[S].get("card"), list):
                    sort_list_dict(item[S]["card"])
                if isinstance(item[S].get("card_bg"), list):
                    sort_list_dict(item[S]["card_bg"])
                if isinstance(item[S].get("loading"), list):
                    sort_list_dict(item[S]["loading"])
                if isinstance(item[S].get("pendant"), list):
                    sort_list_dict(item[S]["pendant"])
                if isinstance(item[S].get("play_icon"), list):
                    sort_list_dict(item[S]["play_icon"])
                if isinstance(item[S].get("skin"), list):
                    sort_list_dict(item[S]["skin"])
                if isinstance(item[S].get("space_bg"), list):
                    sort_list_dict(item[S]["space_bg"])
                if isinstance(item[S].get("thumbup"), list):
                    sort_list_dict(item[S]["thumbup"])
                if isinstance(item[S].get("emoji_package"), list):
                    item[S]["emoji_package"] = sort_p6_emoji(item[S]["emoji_package"])
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
    del_keys(item, "associate", operator=OPR.ANY)
    del_keys(item, "current_activity", operator=OPR.ANY)
    del_keys(item, "current_sources", operator=OPR.ANY)
    del_keys(item, "gray_rule_type", operator=OPR.ANY)
    del_keys(item, "gray_rule", operator=OPR.ANY)
    del_keys(item, "hot", operator=OPR.ANY)
    del_keys(item, "is_symbol", operator=OPR.ANY)
    del_keys(item, "item_stock_surplus", operator=OPR.ANY)
    del_keys(item, "next_activity", operator=OPR.ANY)
    del_keys(item, "non_associate", operator=OPR.ANY)
    del_keys(item, "open_platform_vip_discount", operator=OPR.ANY)
    del_keys(item, "realname_auth", operator=OPR.ANY)
    del_keys(item, "sale_count_desc", operator=OPR.ANY)
    del_keys(item, "sale_left_time", operator=OPR.ANY)
    del_keys(item, "sale_promo", operator=OPR.ANY)
    del_keys(item, "sale_surplus", operator=OPR.ANY)
    del_keys(item, "sale_time_end", recursive=False, operator=OPR.ANY)
    del_keys(item, "state", operator=OPR.ANY)
    del_keys(item, "tag", operator=OPR.ANY)
    del_keys(item, "total_count_desc", operator=OPR.ANY)
    del_keys(item, "user_vas_order", operator=OPR.ANY)
    del_keys(item, "activity_entrance", _EMPTY_ACTIVITY_ENTRANCE, recursive=False)
    del_keys(item, "activity_entrance", None, recursive=False)
    del_keys(item, "associate_words", "")
    del_keys(item, "fan_user", _EMPTY_FAN_USER, recursive=False)
    del_keys(item, "finish_sources", None)
    del_keys(item, "items", None)
    del_keys(item, "jump_link", "")
    del_keys(item, "properties", {})
    del_keys(item, "ref_mid", "0")
    del_keys(item, "sale_time_end", 0, OPR.LEQ)
    del_keys(item, "sales_mode", 0)
    del_keys(item, "suit_item_id", 0)
    del_keys(item, "suit_items", {})
    del_keys(item, "tab_id", 0, OPR.EQ)
    del_keys(item, "unlock_items", None)
    replace_str(item, "http://", "https://")
    replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "fasle", "false")


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
        target = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if src == target:
        return
        print(f"EQ:{path}")
    else:
        ...
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(target)


def _K() -> list[str]:
    A: list[str] = []
    _M = base_path
    for a in ["PART_5_表情包", "PART_6_main"]:
        for b in glob.glob("*.json", root_dir=os.path.join(_M, a)):
            A.append(os.path.join(_M, a, b))
    for a in glob.glob("PART*.jsonl", root_dir=_M):
        A.append(os.path.join(_M, a))
    return A


if __name__ == "__main__":
    base_path = os.path.abspath(".")
    t_list: list[str] = _K() if len(sys.argv) <= 1 else sys.argv[1:]

    try:
        for file in tqdm(t_list):
            _main(file)
    except Exception as e:
        log.error(file)
        log.exception(e)
    finally:
        pass

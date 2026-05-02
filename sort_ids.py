import contextlib
import json
import re
import sys
from pathlib import Path

from loguru import logger
from tqdm import tqdm

from a import OPR, X1, Properties, del_keys, replace_str, sort_list_dict, sort_p6_emoji, sort_str_list

log = logger.bind(user="S.i")
AA = "https://i0.hdslb.com/bfs/activity-plat/static/20240223/3334b2daefb8be78dcc25a7ec37d60fe/sVvHUQ5IPV.png"
BB = "https://i0.hdslb.com/bfs/garb/item/edfb01bd0fa7de7c7e3f516a16a16e8b0cde9ef5.png"
CC = "https://i0.hdslb.com/bfs/garb/item/bb95a716723fa17354aa18ae10323903747c79ec.png"
P = "properties"
S = "suit_items"
_EMPTY_FAN_USER = {"mid": 0, "nickname": "", "avatar": ""}
_EMPTY_FAN_USER_2 = {"mid": 0, "nickname": ""}
_EMPTY_ACTIVITY_ENTRANCE = {
    "id": 0,
    "item_id": 0,
    "title": "",
    "image_cover": "",
    "jump_link": "",
}
_DEBUG_LST = []
base_path = Path.cwd()
b1 = r"http(s)?://(upos-(hz|sz|tribe)-(mirror|static|estg)(08c|cos|ctos|ali|oss|bd|hw|akam)?(b)?(-cmask)?|data|bvc|(c|d)\d+--(p\d+--)?(cn|ov|tf)-gotcha\d+|cn-[a-z]+-(cm|ct|cc|fx|se|gd|cu|eq|ix|wasu)(-v)?-\d+)\.(bilivideo\.com|akamaized\.net)"
b2 = r"\?e=[0-9a-zA-Z_=]{70,}(&|\\u0026)uipk=\d+(&|\\u0026)nbs=\d+(&|\\u0026)deadline=\d+(&|\\u0026)gen=playurlv2(&|\\u0026)os=(08c|cos|ctos|ali|upos|bd|hw|akam)(b)?(bv)?(&|\\u0026)oi=\d+(&|\\u0026)trid=[0-9a-fA-F]{31,33}(&|\\u0026)mid=\d+(&|\\u0026)platform=html5(&|\\u0026)(og=(08c|cos|ctos|ali|oss|bd|hw|akam)(&|\\u0026))?upsig=[0-9a-f]{32}(&|\\u0026)uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform(,og)?((&|\\u0026)hdnts=exp=\d+~hmac=[0-9a-f]+)?(&|\\u0026)bvc=vod(&|\\u0026)nettype=\d+(&|\\u0026)orderid=\d,\d(&|\\u0026)logo=\d+(&|\\u0026)f=B_0_0"
rg1: re.Pattern[str] = re.compile(b1)
rg2: re.Pattern[str] = re.compile(b2)


def reg_bv(d: Properties) -> None:
    # d["head_myself_mp4_bg"]
    # d["head_myself_mp4_bg_list"]
    if "bilivideo" not in d.get("head_myself_mp4_bg", "") and "bilivideo" not in d.get("head_myself_mp4_bg", ""):
        return
    for s in ["head_myself_mp4_bg", "head_myself_mp4_bg_list"]:
        if s in d:
            fs = rg1.sub("__bilivideo__", d[s])
            d[s] = rg2.sub("", fs)


def _p_main(item: X1) -> None:
    itm_id = item["item_id"]
    if itm_id in _DEBUG_LST:
        pass
    c = item["part_id"]
    if isinstance(item.get(P), dict):
        if isinstance(item[P].get("item_ids"), str):
            item[P]["item_ids"] = sort_str_list(item[P]["item_ids"])
        if isinstance(item[P].get("fan_item_ids"), str):
            item[P]["fan_item_ids"] = sort_str_list(item[P]["fan_item_ids"])
    if isinstance(item.get(S), dict):
        if isinstance(item[S].get("emoji"), list):
            sort_list_dict(item[S]["emoji"])
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
            sort_p6_emoji(item[S]["emoji_package"])  # pyright: ignore[reportArgumentType]
    match c:
        case 1:
            pass
        case 2:
            if item[P].get("image", "") == AA and item[P].get("image_preview_small", "") == BB and item[P].get("sale_type", "") == "collect_card":
                item[P].pop("image")
                item[P].pop("image_preview_small")
                item[P].pop("sale_type")
                item[P]["X_Part2_collect_card"] = 1  # pyright: ignore[reportGeneralTypeIssues, reportArgumentType]
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            with contextlib.suppress(KeyError):
                del item["fan_user"]["avatar"]  # pyright: ignore[reportGeneralTypeIssues]
            if S in item and "skin" in item[S]:
                for xx in item[S]["skin"]:
                    if "head_myself_mp4_bg" in xx[P] or "head_myself_mp4_bg_list" in xx[P]:
                        reg_bv(xx[P])
        case 7:
            pass
        case 8:
            if item[P].get("image", "") == CC and item[P].get("image_preview_small", "") == BB and item[P].get("sale_type", "") == "collect_card":
                item[P].pop("image")
                item[P].pop("image_preview_small")
                item[P].pop("sale_type")
                item[P]["X_Part8_collect_card"] = 1  # pyright: ignore[reportGeneralTypeIssues, reportArgumentType]
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
    del_keys(item, "activity_entrance", _EMPTY_ACTIVITY_ENTRANCE, recursive=False)
    del_keys(item, "activity_entrance", None, recursive=False)
    del_keys(item, "addable", operator=OPR.ANY)
    del_keys(item, "associate_words", "")
    del_keys(item, "associate", operator=OPR.ANY)
    del_keys(item, "current_activity", operator=OPR.ANY)
    del_keys(item, "current_sources", operator=OPR.ANY)
    del_keys(item, "fan_user", _EMPTY_FAN_USER, recursive=False)
    del_keys(item, "finish_sources", None)
    del_keys(item, "gray_rule_type", operator=OPR.ANY)
    del_keys(item, "gray_rule", operator=OPR.ANY)
    del_keys(item, "hot", operator=OPR.ANY)
    del_keys(item, "is_hide", operator=OPR.ANY)
    del_keys(item, "is_symbol", operator=OPR.ANY)
    del_keys(item, "item_stock_surplus", operator=OPR.ANY)
    del_keys(item, "items", None)
    del_keys(item, "jump_link", "")
    del_keys(item, "next_activity", operator=OPR.ANY)
    del_keys(item, "non_associate", operator=OPR.ANY)
    del_keys(item, "open_platform_vip_discount", operator=OPR.ANY)
    del_keys(item, "permanent", operator=OPR.ANY)
    del_keys(item, "preview", operator=OPR.ANY)
    del_keys(item, "rank_investor_show", operator=OPR.ANY)
    del_keys(item, "realname_auth", operator=OPR.ANY)
    del_keys(item, "recently_used", operator=OPR.ANY)
    del_keys(item, "recommend", operator=OPR.ANY)
    del_keys(item, "ref_mid", "0")
    del_keys(item, "removable", operator=OPR.ANY)
    del_keys(item, "sale_count_desc", operator=OPR.ANY)
    del_keys(item, "sale_left_time", operator=OPR.ANY)
    del_keys(item, "sale_promo", operator=OPR.ANY)
    del_keys(item, "sale_quantity_limit", operator=OPR.ANY)
    del_keys(item, "sale_reserve_switch", operator=OPR.ANY)
    del_keys(item, "sale_surplus", operator=OPR.ANY)
    del_keys(item, "sale_time_end", 0, OPR.LEQ)
    del_keys(item, "sale_time_end", operator=OPR.ANY, recursive=False)
    del_keys(item, "sales_mode", 0)
    del_keys(item, "setting_pannel_not_show", operator=OPR.ANY)
    del_keys(item, "sortable", operator=OPR.ANY)
    del_keys(item, "state", operator=OPR.ANY)
    del_keys(item, "suit_item_id", 0)
    del_keys(item, "tab_id", 0)
    del_keys(item, "tag", operator=OPR.ANY)
    del_keys(item, "total_count_desc", operator=OPR.ANY)
    del_keys(item, "tracking_info", "")
    del_keys(item, "unlock_items", None)
    del_keys(item, "user_vas_order", operator=OPR.ANY)
    del_keys(item, "properties", {})
    del_keys(item, "suit_items", {})
    replace_str(item, "http://", "https://")
    replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    # replace_str(item, "fasle", "false")


def _main(path: Path) -> None:
    src = path.read_text(encoding="utf-8")
    if path.suffix == ".jsonl":
        target = ""
        for line in src.splitlines():
            item: X1 = json.loads(line)
            _p_main(item)
            target += json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n"
    else:
        item: X1 = json.loads(src)
        _p_main(item)
        target = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if src == target:
        return
        print(f"EQ:{path}")
    path.write_text(target, encoding="utf-8")


def _K() -> list[Path]:
    c: list[Path] = []
    d = base_path
    for a in ["PART_5_表情包", "PART_6_main"]:
        c.extend(b.resolve() for b in (d / a).rglob("*.json"))
    c.extend(a.resolve() for a in d.rglob("PART*.jsonl"))
    return c


if __name__ == "__main__":
    t_list: list[Path] = _K() if len(sys.argv) <= 1 else [Path(x).resolve() for x in sys.argv[1:]]
    try:
        with tqdm(t_list) as pbar:
            for file in pbar:
                pbar.desc = file.stem
                _main(file)
    except Exception as e:
        log.exception(file)  # pyright: ignore[reportPossiblyUnboundVariable]
        log.exception(e)
    finally:
        pass

import base64
import contextlib
import gzip
import json

try:
    import simdjson as sjson
except ImportError:
    sjson = json
import re
from collections.abc import Mapping, Sequence
from enum import IntEnum, auto
from typing import Any, TypedDict

import git_filter_repo
from loguru import logger

FALSE_CMP = [0, "", [], False, {}, None, set(), frozenset()]
"false compare"
AA = "https://i0.hdslb.com/bfs/activity-plat/static/20240223/3334b2daefb8be78dcc25a7ec37d60fe/sVvHUQ5IPV.png"
BB = "https://i0.hdslb.com/bfs/garb/item/edfb01bd0fa7de7c7e3f516a16a16e8b0cde9ef5.png"
CC = "https://i0.hdslb.com/bfs/garb/item/bb95a716723fa17354aa18ae10323903747c79ec.png"
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
b1 = r"http(s)?://(upos-(hz|sz|tribe)-(mirror|static|estg)(08c|cos|ctos|ali|oss|bd|hw|akam)?(b)?(-cmask)?|data|bvc|(c|d)\d+--(p\d+--)?(cn|ov|tf)-gotcha\d+|cn-[a-z]+-(cm|ct|cc|fx|se|gd|cu|eq|ix|wasu)(-v)?-\d+)\.(bilivideo\.com|akamaized\.net)"
b2 = r"\?e=[0-9a-zA-Z_=]{70,}(&|\\\\u0026)uipk=\d+(&|\\\\u0026)nbs=\d+(&|\\\\u0026)deadline=\d+(&|\\\\u0026)gen=playurlv2(&|\\\\u0026)os=(08c|cos|ctos|ali|upos|bd|hw|akam)(b)?(bv)?(&|\\\\u0026)oi=\d+(&|\\\\u0026)trid=[0-9a-fA-F]{31,33}(&|\\\\u0026)mid=\d+(&|\\\\u0026)platform=html5(&|\\\\u0026)(og=(08c|cos|ctos|ali|oss|bd|hw|akam)(&|\\\\u0026))?upsig=[0-9a-f]{32}(&|\\\\u0026)uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform(,og)?((&|\\\\u0026)hdnts=exp=\d+~hmac=[0-9a-f]+)?(&|\\\\u0026)bvc=vod(&|\\\\u0026)nettype=\d+(&|\\\\u0026)orderid=\d,\d(&|\\\\u0026)logo=\d+(&|\\\\u0026)f=B_0_0"
id_skip = {
    b"34374560514518189cf1621881ab38db7724cc85",
}
id_del = {
    b"9e26dfeeb6e641a33dae4961196235bdb965b21b",
    b"0637a088a01e8ddab3bf3fa98dbe804cbde1a0dc",
}


class SkipAllExc(Exception): ...


if True:

    class Properties(TypedDict):
        desc: str
        fan_id: str
        fan_item_ids: str
        fan_mid: str
        fan_no_color: str
        fan_recommend_desc: str
        fan_recommend_jump_type: str
        fan_recommend_jump_value: str
        fan_share_image: str
        gray_rule_type: str
        gray_rule: str
        image_cover_color: str
        image_cover_long: str
        image_cover: str
        image_desc: str
        is_hide: str
        item_base_intro_image: str
        item_hot_limit: str
        item_id_card: str
        item_id_emoji_package: str
        item_id_emoji: str
        item_id_pendant: str
        item_id_thumbup: str
        item_ids: str
        item_stock_surplus: str
        open_platform_vip_discount: str
        owner_uid: str
        pub_btn_plus_color: str
        pub_btn_shade_color_bottom: str
        pub_btn_shade_color_top: str
        rank_investor_name: str
        rank_investor_show: str
        realname_auth: str
        related_words: str
        sale_bp_forever_raw: str
        sale_bp_pm_raw: str
        sale_buy_num_limit: str
        sale_quantity_limit: str
        sale_quantity: str
        sale_region_ip_limit: str
        sale_reserve_switch: str
        sale_sku_id_1: str
        sale_sku_id_2: str
        sale_time_begin: str
        sale_time_end: str
        sale_type: str
        suit_card_type: str
        timing_online_unix: str
        type: str

    class SuitItems(TypedDict):
        desc: str
        item_id: int
        suit_item_id: int
        fan_id: str
        sale_type: str
        suit_card_type: str
        timing_online_unix: str
        type: str
        properties: Properties

    class FanUser(TypedDict):
        avatar: str
        mid: int
        username: str

    class CurrentNextActivity(TypedDict):
        type: int
        time_limit: bool
        time_left: str
        tag: int
        price_bp_month: int
        price_bp_forever: int
        type_month: int
        tag_month: int
        time_limit_month: bool
        time_left_month: str

    class X1(TypedDict):
        item_id: int
        name: str
        group_id: int
        group_name: str
        part_id: int
        state: str
        properties: Properties | dict
        current_activity: CurrentNextActivity
        next_activity: CurrentNextActivity
        current_sources: int
        finish_sources: int
        sale_left_time: int
        sale_time_end: int
        sale_surplus: int
        sale_count_desc: str
        total_count_desc: str
        tag: str
        jump_link: str
        sales_mode: int
        suit_items: dict[str, list[SuitItems]]
        fan_user: FanUser
        unlock_items: int
        activity_entrance: int

    class EmoteMeta(TypedDict):
        size: int
        item_id: int
        alias: str
        label_text: str
        label_color: str

    class EmoteFlags(TypedDict):
        added: bool
        no_access: bool
        preview: bool
        unlocked: bool

    class EmoteEmote(TypedDict):
        id: int
        package_id: int
        text: str
        url: str
        gif_url: str
        webp_url: str
        mtime: int
        type: int
        meta: EmoteMeta

    class Emote(TypedDict):
        id: int
        text: str
        url: str
        mtime: int
        type: int
        attr: int
        meta: EmoteMeta
        emote: list[EmoteEmote]
        flags: EmoteMeta

    class OPR(IntEnum):
        EQ = auto()
        "=="
        NEQ = auto()
        "!="
        GT = auto()
        ">"
        LT = auto()
        "<"
        GEQ = auto()
        ">="
        LEQ = auto()
        "<="
        ANY = auto()
        IN = auto()
        NIN = auto()
        "not in"
        IS = auto()
        NIS = auto()
        "not is"
        FALSE_CMP = auto()
        "false compare"


def _sort_str_list(s: str, /) -> str:
    if s.count(",") == 0:
        return s
    a = sjson.loads(f"[{s}]")
    b = sorted(a)
    return ",".join(str(c) for c in b)


def _sort_list_dict(ld: Sequence[Mapping[str, Any]], k1: str = "item_id", k2: str = "name") -> Sequence[Mapping[str, Any]]:
    list_temp = [json.loads(i2) for i2 in sorted({json.dumps(item) for item in ld})]
    items_with_k1 = [item for item in list_temp if item[k1] not in {0, "0"}]
    items_with_k2 = [item for item in list_temp if item[k1] in {0, "0"}]
    items_with_k1.sort(key=lambda x: x[k1])
    items_with_k2.sort(key=lambda x: x[k2])
    ld[:] = items_with_k1 + items_with_k2  # pyright: ignore[reportIndexIssue]
    return items_with_k1 + items_with_k2


def _sort_p6_emoji(ld: list[Mapping[str, Any]], /) -> list[Mapping[str, Any]]:
    for i in range(len(ld)):
        if isinstance(ld[i].get("properties"), dict) and isinstance(ld[i]["properties"].get("item_ids"), str):
            ld[i]["properties"]["item_ids"] = _sort_str_list(ld[i]["properties"]["item_ids"])
        _sort_list_dict(ld[i]["items"])
    return ld


def _del_keys(d: Mapping[str, Any], k: str, v: Any = None, operator: OPR = OPR.EQ, *, recursive: bool = True) -> None:
    # return
    if isinstance(d, dict) and k in d and (type(d[k]) is type(v) or operator in {OPR.IN, OPR.ANY, OPR.FALSE_CMP}):
        match operator:
            case OPR.EQ:
                if d.get(k) == v:
                    d.pop(k)
            case OPR.IN:
                if v is not None and d.get(k) in v:
                    d.pop(k, None)
            case OPR.FALSE_CMP:
                if d.get(k) in FALSE_CMP:
                    d.pop(k, None)
            case OPR.ANY:
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
            _del_keys(d[key], k, v, operator, recursive=recursive)
        elif isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    _del_keys(item, k, v, operator, recursive=recursive)


def _replace_str(d: Mapping[str, Any] | Sequence[str], old: str, new: str, count: int = -1, *, recursive: bool = True) -> None:
    if not isinstance(d, (dict, list)):
        return
    if not recursive:
        if isinstance(d, dict):
            for key, val in d.items():
                if isinstance(val, str):
                    d[key] = val.replace(old, new, count)
        elif isinstance(d, list):
            for index, val in enumerate(d):
                if isinstance(val, str):
                    d[index] = val.replace(old, new, count)
        return
    if isinstance(d, dict):
        for key, val in d.items():
            if isinstance(val, str):
                d[key] = val.replace(old, new, count)
            elif isinstance(val, (dict, list)):
                _replace_str(val, old, new, count, recursive=recursive)
    elif isinstance(d, list):
        for index, val in enumerate(d):
            if isinstance(val, str):
                d[index] = d[index].replace(old, new, count)
            elif isinstance(val, (dict, list)):
                _replace_str(val, old, new, count, recursive=recursive)


def _p_main(item: X1) -> None:
    # return
    # c = item["part_id"]
    c = 0
    if isinstance(item.get(P), dict):
        if isinstance(item[P].get("item_ids"), str):
            item[P]["item_ids"] = _sort_str_list(item[P]["item_ids"])
        if isinstance(item[P].get("fan_item_ids"), str):
            item[P]["fan_item_ids"] = _sort_str_list(item[P]["fan_item_ids"])
    if isinstance(item.get(S), dict):
        if isinstance(item[S].get("emoji"), list):
            _sort_list_dict(item[S]["emoji"])
        if isinstance(item[S].get("card"), list):
            _sort_list_dict(item[S]["card"])
        if isinstance(item[S].get("card_bg"), list):
            _sort_list_dict(item[S]["card_bg"])
        if isinstance(item[S].get("loading"), list):
            _sort_list_dict(item[S]["loading"])
        if isinstance(item[S].get("pendant"), list):
            _sort_list_dict(item[S]["pendant"])
        if isinstance(item[S].get("play_icon"), list):
            _sort_list_dict(item[S]["play_icon"])
        if isinstance(item[S].get("skin"), list):
            _sort_list_dict(item[S]["skin"])
        if isinstance(item[S].get("space_bg"), list):
            _sort_list_dict(item[S]["space_bg"])
        if isinstance(item[S].get("thumbup"), list):
            _sort_list_dict(item[S]["thumbup"])
        if isinstance(item[S].get("emoji_package"), list):
            _sort_p6_emoji(item[S]["emoji_package"])  # pyright: ignore[reportArgumentType]
    match c:
        case 2:
            if item[P].get("image", "") == AA and item[P].get("image_preview_small", "") == BB and item[P].get("sale_type", "") == "collect_card":
                item[P].pop("image")
                item[P].pop("image_preview_small")
                item[P].pop("sale_type")
                item[P]["X_Part2_collect_card"] = 1  # pyright: ignore[reportGeneralTypeIssues, reportArgumentType]
        case 6:
            with contextlib.suppress(KeyError):
                del item["fan_user"]["avatar"]  # pyright: ignore[reportGeneralTypeIssues]
            # if "bilivideo" in data:
            #     r = regex.compile(_bilivideo)
            #     data = r.sub(data, "__bilivideo__")
            #     r = regex.compile(
            #         r"\?e=[0-9a-zA-Z_=]{70,}(&|\\\\u0026)uipk=\d+(&|\\\\u0026)nbs=\d+(&|\\\\u0026)deadline=\d+(&|\\\\u0026)gen=playurlv2(&|\\\\u0026)os=(08c|cos|ctos|ali|upos|bd|hw|akam)(b)?(bv)?(&|\\\\u0026)oi=\d+(&|\\\\u0026)trid=[0-9a-fA-F]{31,33}(&|\\\\u0026)mid=\d+(&|\\\\u0026)platform=html5(&|\\\\u0026)(og=(08c|cos|ctos|ali|oss|bd|hw|akam)(&|\\\\u0026))?upsig=[0-9a-f]{32}(&|\\\\u0026)uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform(,og)?((&|\\\\u0026)hdnts=exp=\d+~hmac=[0-9a-f]+)?(&|\\\\u0026)bvc=vod(&|\\\\u0026)nettype=\d+(&|\\\\u0026)orderid=\d,\d(&|\\\\u0026)logo=\d+(&|\\\\u0026)f=B_0_0",
            #     )
            #     data = r.sub(data, "")
            #     blob.data = data.encode("utf-8")

        case 8:
            if item[P].get("image", "") == CC and item[P].get("image_preview_small", "") == BB and item[P].get("sale_type", "") == "collect_card":
                item[P].pop("image")
                item[P].pop("image_preview_small")
                item[P].pop("sale_type")
                item[P]["X_Part8_collect_card"] = 1  # pyright: ignore[reportGeneralTypeIssues, reportArgumentType]
        case _:
            pass
    _del_keys(item, "activity_entrance", _EMPTY_ACTIVITY_ENTRANCE, recursive=False)
    _del_keys(item, "activity_entrance", _EMPTY_ACTIVITY_ENTRANCE, recursive=False)
    _del_keys(item, "activity_entrance", None, recursive=False)
    _del_keys(item, "addable", operator=OPR.ANY)
    _del_keys(item, "associate_words", "")
    _del_keys(item, "associate", operator=OPR.ANY)
    _del_keys(item, "current_activity", operator=OPR.ANY)
    _del_keys(item, "current_sources", operator=OPR.ANY)
    _del_keys(item, "fan_user", _EMPTY_FAN_USER, recursive=False)
    _del_keys(item, "finish_sources", None)
    _del_keys(item, "gray_rule_type", operator=OPR.ANY)
    _del_keys(item, "gray_rule", operator=OPR.ANY)
    _del_keys(item, "hot", operator=OPR.ANY)
    _del_keys(item, "is_hide", operator=OPR.ANY)
    _del_keys(item, "is_symbol", operator=OPR.ANY)
    _del_keys(item, "item_stock_surplus", operator=OPR.ANY)
    _del_keys(item, "items", None)
    _del_keys(item, "image_gif", "")
    _del_keys(item, "jump_link", "")
    _del_keys(item, "next_activity", operator=OPR.ANY)
    _del_keys(item, "non_associate", operator=OPR.ANY)
    _del_keys(item, "open_platform_vip_discount", operator=OPR.ANY)
    _del_keys(item, "permanent", operator=OPR.ANY)
    _del_keys(item, "preview", operator=OPR.ANY)
    _del_keys(item, "rank_investor_show", operator=OPR.ANY)
    _del_keys(item, "realname_auth", operator=OPR.ANY)
    _del_keys(item, "recently_used", operator=OPR.ANY)
    _del_keys(item, "recommend", operator=OPR.ANY)
    _del_keys(item, "ref_mid", "0")
    _del_keys(item, "removable", operator=OPR.ANY)
    _del_keys(item, "sale_count_desc", operator=OPR.ANY)
    _del_keys(item, "sale_left_time", operator=OPR.ANY)
    _del_keys(item, "sale_promo", operator=OPR.ANY)
    _del_keys(item, "sale_quantity_limit", operator=OPR.ANY)
    _del_keys(item, "sale_reserve_switch", operator=OPR.ANY)
    _del_keys(item, "sale_surplus", operator=OPR.ANY)
    _del_keys(item, "sale_time_end", 0, OPR.LEQ)
    _del_keys(item, "sale_time_end", operator=OPR.ANY, recursive=False)
    _del_keys(item, "first_up", operator=OPR.ANY)
    _del_keys(item, "sale_time_begin", operator=OPR.ANY)
    _del_keys(item, "sale_time_end", operator=OPR.ANY)
    _del_keys(item, "sales_mode", 0)
    _del_keys(item, "setting_pannel_not_show", operator=OPR.ANY)
    _del_keys(item, "sortable", operator=OPR.ANY)
    _del_keys(item, "state", operator=OPR.ANY)
    _del_keys(item, "suit_item_id", 0)
    _del_keys(item, "tab_id", 0)
    _del_keys(item, "tag", operator=OPR.ANY)
    _del_keys(item, "total_count_desc", operator=OPR.ANY)
    _del_keys(item, "tracking_info", "")
    _del_keys(item, "unlock_items", None)
    _del_keys(item, "user_vas_order", operator=OPR.ANY)
    _del_keys(item, "properties", {})
    _del_keys(item, "suit_items", {})
    # _replace_str(item, "http://", "https://")
    # _replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    # _replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    # replace_str(item, "fasle", "false")


def _p_emote_main(item: Emote) -> None:
    return
    # print(item["id"])
    _del_keys(item, "suggest", [""])
    _del_keys(item, "flags", operator=OPR.ANY)
    _del_keys(item, "activity", None, OPR.ANY)
    _del_keys(item, "sale_promo", None, OPR.ANY)
    _del_keys(item, "label", None)
    _del_keys(item, "attr", 0)
    _del_keys(item, "package_sub_title", "")
    _del_keys(item, "ref_mid", 0)
    _del_keys(item, "resource_type", 0)
    if "emote" in item:
        _sort_list_dict(item["emote"], "id", "text")
    _replace_str(item, "http://", "https://")
    _replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    _replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    # replace_str(item, "fasle", "false")


def _main222(blob: git_filter_repo.Blob) -> None:
    try:
        src: str = blob.data.decode("utf-8")
    except UnicodeError:
        return
    target = ""
    for line in src.splitlines():
        if line == """{"item_id":xxxxx,"name":"xxx","group_name":"xxx","part_id":4,"properties":{"image":"https://i0.hdslb.com/bfs/emote/xxx.png"}}""":
            continue
        if not line:
            continue
        try:
            item: X1 = sjson.loads(line)
        except json.JSONDecodeError as e:
            logger.warning(blob.original_id)
            logger.exception(e)
            return
        _p_main(item)
        target += json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n"
    if src == target:
        return
    blob.data = target.encode("utf-8")


def git_call(blob: git_filter_repo.Blob) -> None:
    if blob.original_id in id_del:
        blob.skip()
    og_data = blob.data
    if blob.original_id in id_skip:
        return
    try:
        data: str = blob.data.decode("utf-8")
    except UnicodeError:
        return
    if not data.startswith(r"{"):
        return
    if data.startswith("import"):
        return
    if data.startswith("#"):
        return
    # data = data.removesuffix("账号已注销")
    # data = data.replace("i1.hdslb.com", "i0.hdslb.com")
    # data = data.replace("i2.hdslb.com", "i0.hdslb.com")

    # s0 = "md28227527"
    # s1 = f'"fan_recommend_jump_value":"https://www.bilibili.com/bangumi/media/{s0}",'
    # s2 = f'"fan_recommend_jump_value":"https://www.bilibili.com/bangumi/media/{s0}/?from=decoration",'
    # data = data.replace(s1, s2)
    # blob.data = data.encode("utf-8")

    # rg = re.compile(b1)
    # data = rg.sub("__bilivideo__", data)
    # rg2 = re.compile(b2)
    # data = rg2.sub("", data)

    try:
        raise SkipAllExc
        item: dict = sjson.loads(data)
        if isinstance(item, list):
            return
        # if "code" in item:
        #     item = item["data"]
        if "emote" in item or "url" in item:
            _p_emote_main(item)  # pyright: ignore[reportArgumentType]
            target = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent="\t")
            blob.data = target.encode("utf-8")
            return
        _p_main(item)  # pyright: ignore[reportArgumentType]
        if item.get("part_id") == 12:
            target = (json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
            target = (json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
            raise json.JSONDecodeError("fake raise", "", 0)  # noqa: TRY301
        blob.data = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent="\t").encode("utf-8")
    except (json.JSONDecodeError, ValueError):
        try:
            _main222(blob)
        except Exception as e:  # noqa: BLE001
            logger.warning(blob.original_id)
            logger.warning(data)
            logger.exception(e)
    except SkipAllExc:
        pass
    except Exception as e:  # noqa: BLE001
        logger.warning(blob.original_id)
        logger.warning(data)
        logger.exception(e)
    finally:
        pd: bytes = blob.data
        fd = {
            "id": blob.original_id.decode(),
            "size": f"{len(og_data)}->{len(blob.data)}",
            # "og": og_data.decode(),
            # "pd": pd.decode(),
        }
        # if pd == og_data:
        #     fd["pd"] = ""
        if og_data == pd:
            pass
        else:
            with open("Z:\\test.jsonl", "ab") as fp:  # noqa: PTH123
                fp.write(json.dumps(fd, ensure_ascii=False, indent=None).encode())
                fp.write(base64.b64encode(gzip.compress(pd)))
                fp.write(b"\n")


"""
git filter-repo --blob-callback "import xxx;xxx.git_call(blob)"
"""

import json
from collections.abc import Mapping, Sequence
from enum import IntEnum, auto
from typing import Any, TypedDict


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
    ld: Sequence[Mapping],
    k1: str = "item_id",
    k2: str = "name",
) -> Sequence[Mapping]:
    list_temp = [json.loads(i2) for i2 in list({json.dumps(item) for item in ld})]
    items_with_k1 = [item for item in list_temp if item[k1] not in {0, "0"}]
    items_with_k2 = [item for item in list_temp if item[k1] in {0, "0"}]
    items_with_k1.sort(key=lambda x: x[k1])  # noqa: FURB118
    items_with_k2.sort(key=lambda x: x[k2])  # noqa: FURB118
    ld[:] = items_with_k1 + items_with_k2  # type: ignore
    return items_with_k1 + items_with_k2


def sort_p6_emoji(ld: list[Mapping], /) -> list[Mapping]:
    for i in range(len(ld)):
        if isinstance(ld[i].get("properties"), dict) and isinstance(ld[i]["properties"].get("item_ids"), str):
            ld[i]["properties"]["item_ids"] = sort_str_list(ld[i]["properties"]["item_ids"])
        sort_list_dict(ld[i]["items"])
    return ld


def del_keys(d: Mapping, k: str, v=None, operator: OPR = OPR.EQ, *, recursive=True) -> None:
    if isinstance(d, dict) and k in d and (type(d[k]) is type(v) or operator in {OPR.IN, OPR.ANY}):
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
            del_keys(d[key], k, v, operator, recursive=recursive)
        elif isinstance(d[key], list):
            for item in d[key]:  # type: ignore
                if isinstance(item, dict):
                    del_keys(item, k, v, operator, recursive=recursive)


def replace_value_in_list_dict(
    d_or_lst: Mapping[str, Any] | list,
    k_or_idx: int | str,
    old_v,
    new_v,
    *,
    recursive=True,
) -> None:
    if (k_or_idx in d_or_lst and isinstance(d_or_lst, dict) and isinstance(d_or_lst[k_or_idx], str)) or (isinstance(d_or_lst, list) and isinstance(k_or_idx, int) and len(d_or_lst) >= k_or_idx):  # type: ignore # noqa: PLR0916, SIM102
        if d_or_lst[k_or_idx] == old_v:  # type:ignore
            d_or_lst[k_or_idx] = new_v  # type:ignore
    if not recursive:
        return
    for key in d_or_lst:
        if isinstance(d_or_lst[key], dict):  # type: ignore
            replace_value_in_list_dict(d_or_lst[key], k_or_idx, old_v, new_v, recursive=recursive)  # type: ignore
        elif isinstance(d_or_lst[key], list):  # type: ignore
            for index, item in enumerate(d_or_lst[key]):  # type: ignore
                if isinstance(item, dict):
                    replace_value_in_list_dict(item, index, old_v, new_v, recursive=recursive)
                elif isinstance(item, list):
                    replace_value_in_list_dict(d_or_lst[key], index, old_v, new_v, recursive=recursive)  # type: ignore


def replace_str(d: Mapping | Sequence[str], old: str, new: str, count: int = -1, *, recursive=True) -> None:
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
                replace_str(val, old, new, count, recursive=recursive)
    elif isinstance(d, list):
        for index, val in enumerate(d):
            if isinstance(val, str):
                d[index] = d[index].replace(old, new, count)
            elif isinstance(val, (dict, list)):
                replace_str(val, old, new, count, recursive=recursive)


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
    fan_user: int
    unlock_items: int
    activity_entrance: int

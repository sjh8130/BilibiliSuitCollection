import json
import os
import sys
import time
from pathlib import Path
from types import NoneType
from typing import Any

from tqdm import tqdm

result: dict = {}
if 1:
    DONT_CARE_INDEX_SEP: str = "IDX"
    SW1 = True
    DONT_CARE_INDEX_LIST = {
        "root.finish_sources",
        "root.properties.preview_imgs",
        "root.properties.public_time_line",
        "root.suit_items.card_bg",
        "root.suit_items.card",
        "root.suit_items.emoji_package",
        f"root.suit_items.emoji_package[{DONT_CARE_INDEX_SEP}].items",
        f"root.suit_items.emoji_package[{DONT_CARE_INDEX_SEP}].properties.item_emoji_list",
        "root.suit_items.emoji",
        "root.suit_items.loading",
        "root.suit_items.pendant",
        "root.suit_items.play_icon",
        "root.suit_items.skin",
        f"root.suit_items.skin[{DONT_CARE_INDEX_SEP}].properties.head_myself_mp4_bg_list",
        "root.suit_items.space_bg",
        "root.suit_items.thumbup",
    }
    IGNORE_LIST = {
        "root.fan_user.avatar",
        "root.fan_user.mid",
        "root.fan_user.nickname",
        f"root.finish_sources[{DONT_CARE_INDEX_SEP}].id",
        f"root.finish_sources[{DONT_CARE_INDEX_SEP}].jump_url",
        f"root.finish_sources[{DONT_CARE_INDEX_SEP}].time_from",
        f"root.finish_sources[{DONT_CARE_INDEX_SEP}].time_to",
        "root.group_name",
        "root.item_id",
        "root.name",
        "root.properties.desc",
        "root.properties.drag_left_png",
        "root.properties.fan_id",
        "root.properties.fan_item_ids",
        "root.properties.fan_mid",
        "root.properties.fan_no_color",
        "root.properties.fan_recommend_desc",
        "root.properties.fan_share_image",
        "root.properties.first_up",
        "root.properties.head_bg",
        "root.properties.head_myself_mp4_bg",
        "root.properties.head_myself_squared_bg",
        "root.properties.head_tab_bg",
        "root.properties.image_ani",
        "root.properties.image_cover_color",
        "root.properties.image_cover",
        "root.properties.image_gif",
        "root.properties.image_preview_small",
        "root.properties.image_preview",
        "root.properties.image_webp",
        "root.properties.image",
        "root.properties.imageIDX_landscape",
        "root.properties.imageIDX_portrait",
        "root.properties.intro_imgs",
        "root.properties.item_id_card",
        "root.properties.item_id_emoji_package",
        "root.properties.item_id_emoji",
        "root.properties.item_id_thumbup",
        "root.properties.item_ids",
        "root.properties.loading_frame_url",
        "root.properties.loading_url",
        "root.properties.owner_uid",
        "root.properties.package_md5",
        "root.properties.sale_bp_forever_raw",
        "root.properties.sale_quantity_limit",
        "root.properties.sale_quantity",
        "root.properties.sale_sku_id_1",
        "root.properties.sale_sku_id_2",
        "root.properties.sale_time_begin",
        "root.properties.sale_time_end",
        "root.properties.squared_image",
        "root.properties.static_icon_image",
        "root.properties.tail_color_selected",
        "root.properties.tail_icon_myself",
        "root.properties.ver",
        "root.suit_items.card_bg[IDX].item_id",
        "root.suit_items.card_bg[IDX].name",
        "root.suit_items.card_bg[IDX].properties.fan_no_color",
        "root.suit_items.card_bg[IDX].properties.image_preview_small",
        "root.suit_items.card_bg[IDX].properties.image",
        "root.suit_items.card_bg[IDX].suit_item_id",
        "root.suit_items.card[IDX].fan_no_color",
        "root.suit_items.card[IDX].fans_image",
        "root.suit_items.card[IDX].fans_material_id",
        "root.suit_items.card[IDX].image_preview_small",
        "root.suit_items.card[IDX].image",
        "root.suit_items.card[IDX].item_id",
        "root.suit_items.card[IDX].name",
        "root.suit_items.card[IDX].properties.fan_no_color",
        "root.suit_items.card[IDX].properties.fans_image",
        "root.suit_items.card[IDX].properties.fans_material_id",
        "root.suit_items.card[IDX].properties.image_preview_small",
        "root.suit_items.card[IDX].properties.image",
        "root.suit_items.card[IDX].suit_item_id",
        "root.suit_items.emoji_package[IDX].item_id",
        "root.suit_items.emoji_package[IDX].items[IDX].item_id",
        "root.suit_items.emoji_package[IDX].items[IDX].name",
        "root.suit_items.emoji_package[IDX].items[IDX].properties.image",
        "root.suit_items.emoji_package[IDX].name",
        "root.suit_items.emoji_package[IDX].properties.image",
        "root.suit_items.emoji_package[IDX].properties.item_emoji_list[IDX].image",
        "root.suit_items.emoji_package[IDX].properties.item_emoji_list[IDX].name",
        "root.suit_items.emoji_package[IDX].properties.item_ids",
        "root.suit_items.emoji_package[IDX].suit_item_id",
        "root.suit_items.emoji[IDX].item_id",
        "root.suit_items.emoji[IDX].name",
        "root.suit_items.emoji[IDX].properties.image_gif",
        "root.suit_items.emoji[IDX].properties.image_webp",
        "root.suit_items.emoji[IDX].properties.image",
        "root.suit_items.loading[IDX].item_id",
        "root.suit_items.loading[IDX].name",
        "root.suit_items.loading[IDX].properties.image_preview_small",
        "root.suit_items.loading[IDX].properties.loading_frame_url",
        "root.suit_items.loading[IDX].properties.loading_url",
        "root.suit_items.loading[IDX].properties.ver",
        "root.suit_items.loading[IDX].suit_item_id",
        "root.suit_items.pendant[IDX].item_id",
        "root.suit_items.pendant[IDX].properties.garb_avatar",
        "root.suit_items.pendant[IDX].properties.image",
        "root.suit_items.pendant[IDX].suit_item_id",
        "root.suit_items.play_icon[IDX].item_id",
        "root.suit_items.play_icon[IDX].name",
        "root.suit_items.play_icon[IDX].properties.drag_icon_hash",
        "root.suit_items.play_icon[IDX].properties.drag_icon",
        "root.suit_items.play_icon[IDX].properties.drag_left_png",
        "root.suit_items.play_icon[IDX].properties.drag_right_png",
        "root.suit_items.play_icon[IDX].properties.icon_hash",
        "root.suit_items.play_icon[IDX].properties.icon",
        "root.suit_items.play_icon[IDX].properties.middle_png",
        "root.suit_items.play_icon[IDX].properties.squared_image",
        "root.suit_items.play_icon[IDX].properties.static_icon_image",
        "root.suit_items.play_icon[IDX].properties.ver",
        "root.suit_items.play_icon[IDX].suit_item_id",
        "root.suit_items.skin[IDX].item_id",
        "root.suit_items.skin[IDX].name",
        "root.suit_items.skin[IDX].properties.color_second_page",
        "root.suit_items.skin[IDX].properties.head_bg",
        "root.suit_items.skin[IDX].properties.head_myself_bg",
        "root.suit_items.skin[IDX].properties.head_myself_mp4_bg_list",
        "root.suit_items.skin[IDX].properties.head_myself_mp4_bg",
        "root.suit_items.skin[IDX].properties.head_myself_squared_bg",
        "root.suit_items.skin[IDX].properties.head_tab_bg",
        "root.suit_items.skin[IDX].properties.image_cover",
        "root.suit_items.skin[IDX].properties.image_preview",
        "root.suit_items.skin[IDX].properties.package_md5",
        "root.suit_items.skin[IDX].properties.package_url",
        "root.suit_items.skin[IDX].properties.pub_btn_plus_color",
        "root.suit_items.skin[IDX].properties.tail_bg",
        "root.suit_items.skin[IDX].properties.tail_color_selected",
        "root.suit_items.skin[IDX].properties.tail_color",
        "root.suit_items.skin[IDX].properties.tail_icon_channel",
        "root.suit_items.skin[IDX].properties.tail_icon_dynamic",
        "root.suit_items.skin[IDX].properties.tail_icon_main",
        "root.suit_items.skin[IDX].properties.tail_icon_myself",
        "root.suit_items.skin[IDX].properties.tail_icon_pub_btn_bg",
        "root.suit_items.skin[IDX].properties.tail_icon_selected_channel",
        "root.suit_items.skin[IDX].properties.tail_icon_selected_dynamic",
        "root.suit_items.skin[IDX].properties.tail_icon_selected_main",
        "root.suit_items.skin[IDX].properties.tail_icon_selected_myself",
        "root.suit_items.skin[IDX].properties.tail_icon_selected_pub_btn_bg",
        "root.suit_items.skin[IDX].properties.tail_icon_selected_shop",
        "root.suit_items.skin[IDX].properties.tail_icon_shop",
        "root.suit_items.skin[IDX].properties.ver",
        "root.suit_items.skin[IDX].suit_item_id",
        "root.suit_items.skin[IDX].tab_id",
        "root.suit_items.space_bg[IDX].item_id",
        "root.suit_items.space_bg[IDX].name",
        "root.suit_items.space_bg[IDX].properties.fan_no_color",
        "root.suit_items.space_bg[IDX].properties.fan_no_image",
        "root.suit_items.space_bg[IDX].properties.image1_landscape",
        "root.suit_items.space_bg[IDX].properties.imageIDX_landscape",
        "root.suit_items.space_bg[IDX].properties.imageIDX_portrait",
        "root.suit_items.space_bg[IDX].suit_item_id",
        "root.suit_items.thumbup[IDX].item_id",
        "root.suit_items.thumbup[IDX].name",
        "root.suit_items.thumbup[IDX].properties.image_ani_cut",
        "root.suit_items.thumbup[IDX].properties.image_ani",
        "root.suit_items.thumbup[IDX].properties.image_preview",
        "root.suit_items.thumbup[IDX].suit_item_id",
    }
    S1 = {
        "root.suit_items.space_bg[IDX].properties.image1_landscape",
        "root.suit_items.space_bg[IDX].properties.image2_landscape",
        "root.suit_items.space_bg[IDX].properties.image3_landscape",
        "root.suit_items.space_bg[IDX].properties.image4_landscape",
        "root.suit_items.space_bg[IDX].properties.image5_landscape",
        "root.suit_items.space_bg[IDX].properties.image6_landscape",
        "root.suit_items.space_bg[IDX].properties.image7_landscape",
        "root.suit_items.space_bg[IDX].properties.image8_landscape",
        "root.suit_items.space_bg[IDX].properties.image9_landscape",
        "root.suit_items.space_bg[IDX].properties.image10_landscape",
        "root.suit_items.space_bg[IDX].properties.image11_landscape",
    }
    S2 = {
        "root.suit_items.space_bg[IDX].properties.image1_portrait",
        "root.suit_items.space_bg[IDX].properties.image2_portrait",
        "root.suit_items.space_bg[IDX].properties.image3_portrait",
        "root.suit_items.space_bg[IDX].properties.image4_portrait",
        "root.suit_items.space_bg[IDX].properties.image5_portrait",
        "root.suit_items.space_bg[IDX].properties.image6_portrait",
        "root.suit_items.space_bg[IDX].properties.image7_portrait",
        "root.suit_items.space_bg[IDX].properties.image8_portrait",
        "root.suit_items.space_bg[IDX].properties.image9_portrait",
        "root.suit_items.space_bg[IDX].properties.image10_portrait",
        "root.suit_items.space_bg[IDX].properties.image11_portrait",
    }
    S3 = {
        "root.properties.image1_landscape",
        "root.properties.image2_landscape",
        "root.properties.image3_landscape",
        "root.properties.image4_landscape",
        "root.properties.image5_landscape",
        "root.properties.image6_landscape",
        "root.properties.image7_landscape",
        "root.properties.image8_landscape",
        "root.properties.image9_landscape",
        "root.properties.image10_landscape",
        "root.properties.image11_landscape",
    }
    S4 = {
        "root.properties.image1_portrait",
        "root.properties.image2_portrait",
        "root.properties.image3_portrait",
        "root.properties.image4_portrait",
        "root.properties.image5_portrait",
        "root.properties.image6_portrait",
        "root.properties.image7_portrait",
        "root.properties.image8_portrait",
        "root.properties.image9_portrait",
        "root.properties.image10_portrait",
        "root.properties.image11_portrait",
    }
    STR_ITM = {
        "root.properties.preview_imgs",
        "root.properties.public_time_line",
        "root.suit_items.emoji_package[IDX].properties.item_emoji_list",
        "root.suit_items.skin[IDX].properties.head_myself_mp4_bg_list",
    }
if 0:
    DONT_CARE_INDEX_LIST = set()
if 0:
    IGNORE_LIST = set()


def sort_final(item):
    if isinstance(item, dict):
        for key in item:
            sort_final(item[key])
    elif isinstance(item, list) and bool(item):
        item.sort()
        for itm in item:
            if isinstance(itm, dict):
                sort_final(itm)


def analyze_structure(item: Any, target_key="root") -> None:
    if target_key in S1:
        target_key = "root.suit_items.space_bg[IDX].properties.imageIDX_landscape"
    if target_key in S2:
        target_key = "root.suit_items.space_bg[IDX].properties.imageIDX_portrait"
    if target_key in S3:
        target_key = "root.properties.imageIDX_landscape"
    if target_key in S4:
        target_key = "root.properties.imageIDX_portrait"
    if result.get(target_key) is None:
        result[target_key] = {"type": {}}
    typ = type(item).__name__
    if target_key in STR_ITM:
        item = json.loads(item)  # type:ignore[reportOperatorIssue]
        typ = "str_list"
    if typ not in result[target_key]["type"]:
        result[target_key]["type"][typ] = result[target_key]["type"].get(typ, 0) + 1
    if isinstance(item, dict):
        for key, value in item.items():
            analyze_structure(value, f"{target_key}.{key}")
    elif isinstance(item, list):
        for index, li in enumerate(item):
            tk = f"{target_key}[{DONT_CARE_INDEX_SEP}]" if target_key in DONT_CARE_INDEX_LIST else f"{target_key}[{index}]"
            analyze_structure(li, tk)
    if isinstance(item, (dict, list)):
        return
    if SW1 and target_key in IGNORE_LIST:
        return
    if result[target_key].get("value") is None:
        result[target_key]["value"] = {}
    if isinstance(item, (int, NoneType, bool)):
        t1 = "REPR:" + repr(item)
    elif True:
        t1 = str(item)
    if result[target_key]["value"].get(t1) is None:
        result[target_key]["value"][t1] = 0
    result[target_key]["value"][t1] += 1


def walk_dir() -> list[Path]:
    A: list[Path] = []
    for a in ["PART_5_表情包", "PART_6_main"]:
        A.extend(b.resolve() for b in (base_path / a).rglob("*.json"))
    A.extend(base_path / a for a in base_path.glob("PART*.jsonl"))
    return A


def main():
    for p in tqdm(t_list):
        with p.open(encoding="utf-8") as fp:
            if str(p).endswith(".jsonl"):
                for line in fp:
                    item: dict = json.loads(line)
                    analyze_structure(item)
            elif str(p).endswith(".json"):
                item: dict = json.load(fp)
                analyze_structure(item)
    # sort_final(result)
    return result


if __name__ == "__main__":
    output_dir = Path("Z:\\") if os.name == "nt" else Path("/mnt/z/")
    base_path = Path.cwd().resolve()
    t_list: list[Path] = walk_dir() if len(sys.argv) <= 1 else [Path(x) for x in sys.argv[1:]]

    if not output_dir.exists():
        output_dir.mkdir()
    # if os.path.exists(os.path.join(output_dir, "result.json")):
    #     with open(os.path.join(output_dir, "result.json"), "r", encoding="utf-8") as fp:
    #         result.update(json.load(fp))
    start_time = time.time()
    main()
    with (output_dir / "result.json").open("w", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent="\t", sort_keys=True)
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    # time.sleep(10)

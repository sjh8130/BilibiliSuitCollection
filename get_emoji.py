import json
import os
import sys
import time
from pathlib import Path
from typing import TypedDict

from tqdm import tqdm

result: list[str] = []


class EmoteMeta(TypedDict):
    size: int
    item_id: int
    alias: str
    label_text: str
    label_color: str


class Emote(TypedDict):
    id: int
    package_id: int
    text: str
    url: str
    gif_url: str
    webp_url: str
    mtime: int
    type: int
    meta: EmoteMeta


class EmoteMain(TypedDict):
    id: int
    text: str
    url: str
    mtime: int
    type: int
    meta: EmoteMeta
    emote: list[Emote]


def walk_dir() -> list[Path]:
    A: list[Path] = []
    for b in (base_path / "emoji").rglob("*.json"):
        A.append(b.resolve())
    return A


def main():
    for p in tqdm(t_list):
        with p.open(encoding="utf-8") as fp:
            item: EmoteMain = json.load(fp)
            if "emote" in item:
                for x in item["emote"]:
                    result.append(x["text"])
    return result


if __name__ == "__main__":
    output_dir = Path("Z:\\") if os.name == "nt" else Path("/mnt/z/")
    base_path = Path.cwd().resolve()
    t_list: list[Path] = walk_dir() if len(sys.argv) <= 1 else [Path(x) for x in sys.argv[1:]]

    if not output_dir.exists():
        output_dir.mkdir()
    if os.path.exists(output_dir / "emoji_result.json"):
        with open(output_dir / "emoji_result.json", "r", encoding="utf-8") as fp:
            result = json.load(fp)
    start_time = time.time()
    main()
    with (output_dir / "emoji_result.json").open("w", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent="\t", sort_keys=True)
    total_time = time.time() - start_time
    print(f"处理完成，耗时：{total_time:.3f}秒")
    # time.sleep(10)

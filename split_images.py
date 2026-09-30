"""Split each combined before/after image into before.png and after.png.

Crop boxes are (left, top, right, bottom) in source pixels. They exclude
dividers, titles, logos and scale boxes. Both halves of a pair have identical
size so they can be aligned in Step 1.
"""
from pathlib import Path

from PIL import Image

SRC_DIR = Path(__file__).parent / "Images"
OUT_DIR = Path(__file__).parent / "pairs"

# name -> (source file, before box, after box)
PAIRS = {
    "01_amazon": ("Amazon.jpg", (12, 62, 504, 488), (520, 62, 1012, 488)),
    "02_amazon_brazil": ("Amazon2.jpeg", (0, 50, 594, 590), (606, 50, 1200, 590)),
    "03_forest_mine": ("Forest.jpg", (0, 0, 230, 250), (246, 0, 476, 250)),
    "04_australia": ("Image.jpeg", (8, 0, 950, 1080), (968, 0, 1910, 1080)),
    "05_queensland": ("Image2.jpg", (0, 50, 350, 375), (364, 50, 714, 375)),
    "06_warehouse": ("Image3.jpeg.jpg", (0, 0, 922, 570), (0, 582, 922, 1152)),
    "07_china_city": ("Image4.jpeg", (0, 0, 592, 1010), (606, 0, 1198, 1010)),
    "08_uk_housing": ("Image5.jpeg", (0, 0, 453, 434), (471, 0, 924, 434)),
    "09_canberra": ("Image6.jpeg", (68, 22, 412, 386), (442, 22, 786, 386)),
    "10_arizona": ("NY.jpeg", (0, 115, 770, 735), (778, 115, 1548, 735)),
}


def box_size(box):
    return (box[2] - box[0], box[3] - box[1])


def split_pair(name, filename, before_box, after_box):
    if box_size(before_box) != box_size(after_box):
        raise ValueError(f"{name}: before/after crop sizes differ")
    src_path = SRC_DIR / filename
    if not src_path.exists():
        raise FileNotFoundError(src_path)
    out = OUT_DIR / name
    out.mkdir(parents=True, exist_ok=True)
    with Image.open(src_path) as img:
        rgb = img.convert("RGB")
        rgb.crop(before_box).save(out / "before.png")
        rgb.crop(after_box).save(out / "after.png")


def main():
    for name, (filename, before_box, after_box) in PAIRS.items():
        split_pair(name, filename, before_box, after_box)
        print(f"{name}: {box_size(before_box)}")


if __name__ == "__main__":
    main()

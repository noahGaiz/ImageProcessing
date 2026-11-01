#scores a detection method against the hand-labelled boxes in labels.py
#for each box: % of its pixels where the method agrees with the label, then averaged over boxes
from pathlib import Path
import cv2
import numpy as np
from labels import BOXES

PAIRS_DIR = Path(__file__).resolve().parent.parent / "pairs"


def score_boxes(method, boxes=BOXES, pairs_dir=PAIRS_DIR):
    #returns one row per box: (pair, half, label, what, % correct)
    cache = {}
    rows = []
    for pair, half, label, x1, y1, x2, y2, what in boxes:
        key = (pair, half)
        if key not in cache:
            img = cv2.imread(str(pairs_dir / pair / f"{half}.png"))
            if img is None:
                raise FileNotFoundError(f"Could not read {pairs_dir / pair / half}.png")
            cache[key] = method(img)
        mask = cache[key][y1:y2, x1:x2]
        correct = mask if label == 1 else ~mask
        rows.append((pair, half, label, what, correct.mean() * 100))
    return rows


def summary(rows):
    #overall = mean over all boxes; balanced = average of the vegetation and not-vegetation scores
    veg = [r[4] for r in rows if r[2] == 1]
    not_veg = [r[4] for r in rows if r[2] == 0]
    return {
        "overall": np.mean([r[4] for r in rows]),
        "vegetation": np.mean(veg),
        "not vegetation": np.mean(not_veg),
        "balanced": (np.mean(veg) + np.mean(not_veg)) / 2,
    }

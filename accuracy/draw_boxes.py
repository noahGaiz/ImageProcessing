#draws every labelled box on its image so the team can check the labels by eye
#yellow = vegetation, magenta = not vegetation; saves boxes/pair<NN>.jpg
from pathlib import Path
import cv2
import numpy as np
from labels import BOXES

HERE = Path(__file__).resolve().parent
PAIRS_DIR = HERE.parent / "pairs"
COLOURS = {1: (0, 255, 255), 0: (255, 0, 255)}#BGR yellow, magenta

for pair in sorted({b[0] for b in BOXES}):
    halves = []
    for half in ("before", "after"):
        img = cv2.imread(str(PAIRS_DIR / pair / f"{half}.png"))
        for i, (p, h, label, x1, y1, x2, y2, _) in enumerate(BOXES):
            if (p, h) == (pair, half):
                cv2.rectangle(img, (x1, y1), (x2, y2), COLOURS[label], 2)
                cv2.putText(img, str(i), (x1 + 2, y1 + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, COLOURS[label], 1)
        cv2.putText(img, half, (8, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        halves.append(img)
    gap = np.full((halves[0].shape[0], 10, 3), 255, np.uint8)
    cv2.imwrite(str(HERE / "boxes" / f"pair{pair}.jpg"), np.hstack([halves[0], gap, halves[1]]), [cv2.IMWRITE_JPEG_QUALITY, 85])

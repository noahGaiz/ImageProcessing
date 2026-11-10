# Accuracy Check

The change map, hand-check and bar graph show **what the method finds**. This folder checks **whether it's right**. Areas are marked by eye as "definitely vegetation" or "definitely not", then each method is scored on how many pixels it gets right.

## Files

| File | What it is |
|---|---|
| `labels.py` | 62 ground-truth boxes on all 8 pairs, both halves (28 vegetation, 34 not vegetation) |
| `score.py` | `score_boxes(method)` gives the % correct per box; `summary(rows)` gives the averages |
| `draw_boxes.py` | Draws the boxes on the images into `boxes/` (yellow = vegetation, magenta = not) |
| `boxes/pairNN.jpg` | The boxes on each pair, for checking the labels by eye |

**Please check the boxes** in `boxes/` before trusting the numbers. One person marked them, so if a box looks wrong, fix it in `labels.py`.

What was labelled:
- **Vegetation:** forest, single trees, grass, green crop fields, and brown autumn trees (pair 06; they're still vegetation, just not green).
- **Not vegetation:** cleared land, bare soil, building sites, roads, roofs, car parks, water, and solid labels such as date boxes and scale bars.
- **Left out on purpose:** mixed or unclear areas (dry grass, gardens between houses, thin white text over the photo).

## How to run (notebook cell, after the detection functions)

```python
import sys
sys.path.append("accuracy")
from score import score_boxes, summary

for name, method in [("RGB + edges", vegetation_rgb_texture), ("HSV + edges", vegetation_hsv_texture)]:
    s = summary(score_boxes(method))
    print(f"{name}: overall {s['overall']:.1f}% | vegetation {s['vegetation']:.1f}% | "
          f"not vegetation {s['not vegetation']:.1f}% | balanced {s['balanced']:.1f}%")
```

- **Overall** is the average over all boxes.
- **Vegetation** is how much real vegetation the method finds.
- **Not vegetation** is how well it avoids false vegetation.
- **Balanced** is the average of the two, so the result doesn't depend on how many boxes of each kind there are.

## Results: current code (commit `3c4bad4`, 1 Nov), before any improvements

| Method | Overall | Vegetation | Not vegetation | Balanced |
|---|---|---|---|---|
| RGB + edges | 75.7% | 64.3% | 85.0% | 74.7% |
| HSV + edges | 73.4% | 77.8% | 69.8% | 73.8% |

The two methods are **almost tied overall** but make opposite mistakes. RGB misses real vegetation; HSV adds false vegetation.

Per pair (average of that pair's boxes):

| Pair | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 |
|---|---|---|---|---|---|---|---|---|
| RGB + edges | 91 | 85 | 57 | 79 | 76 | 69 | 63 | 83 |
| HSV + edges | 79 | 79 | 66 | 90 | 73 | 69 | 48 | 78 |

### Where they fail (% of box correct, RGB / HSV)

- **Brown autumn trees, pair 06: 0 / 0.** Both methods miss them completely.
- **Dark tree crowns, pair 03 before: 0–3 / 11–13.** Dark trees on dry grass aren't picked up.
- **Water.** Pair 07 lake 9–18 / 1–7, pair 05 pond 37–94 / 26–67, pair 06 pond 48 / 41. Green water is counted as vegetation.
- **HSV counts bare ground and buildings.** Pair 05 after building site 100 / **0**, pair 08 building site 93 / 37, pair 01 cleared land 78–94 / 21–23, pair 07 city 95 / 56.
- **RGB misses grass and forest.** Pair 04 after green field **3** / 100, pair 03 park 52 / 90, pair 05 forest 36–66 / 77–90.
- **Black date labels, pair 01: 72–76 / 82–85.** Some very dark pixels count as vegetation.

## After improvements

| Improvement | Method | Overall | Vegetation | Not vegetation | Notes |
|---|---|---|---|---|---|
| Water check (Polina, `water_mask`) | RGB + edges | 75.7% → 77.3% | 64.3% → 64.3% | 85.0% → 87.9% | Water boxes 41.0% → 60.5% |
| | HSV + edges | 73.4% → 75.0% | 77.8% → 77.8% | 69.8% → 72.8% | Water boxes 28.5% → 48.7% |
| Speckle clean-up (Heeyeon, `clean_mask`) | RGB + edges | 75.7% → 76.0% | 64.3% → 64.3% | 85.0% → 85.7% | No box worse |
| | HSV + edges | 73.4% → 74.4% | 77.8% → 78.7% | 69.8% → 70.8% | Pair 03 trees 11–13% → 7–9% |
| Both: water removed, then `clean_mask` | RGB + edges | 75.7% → **77.6%** | 64.3% → 64.3% | 85.0% → 88.6% | |
| | HSV + edges | 73.4% → **76.0%** | 77.8% → 78.7% | 69.8% → 73.8% | |

The water thresholds were tuned on these same boxes, so treat that gain as a slightly optimistic estimate. "Both" was checked outside the notebook with `clean_mask(method(img) & ~water_mask(img))`; there's no notebook function for it yet.

### Final table (all improvements, last cell of the notebook)

Each improvement added one at a time. Label masking (`label_mask`) leaves printed labels and borders out; for scoring, masked pixels count as not vegetation, so the 6 label boxes (date text, scale bars, date labels) reach 99% by design. "Land boxes" (the other 56) shows the real effect.

| Pipeline | RGB + edges overall | HSV + edges overall | Land boxes (RGB / HSV) | Label boxes (RGB / HSV) |
|---|---|---|---|---|
| Original | 75.7% | 73.4% | 74.0% / 71.2% | 91.2% / 94.0% |
| + water check | 77.3% | 75.0% | 75.8% / 73.0% | 91.2% / 94.0% |
| + clean_mask | 76.0% | 74.4% | 74.3% / 72.2% | 91.9% / 94.7% |
| water check + clean_mask | 77.6% | 76.0% | 76.1% / 74.0% | 91.9% / 94.7% |
| water check + clean_mask + labels | **78.3%** | **76.5%** | 76.1% / 74.0% | 99.0% / 99.0% |

Label masking doesn't change any land box. Its main effect is on vegetation %: pair 01 before (all rainforest) goes from 88.8% to 99.3% (RGB + edges). Alignment can't be scored here (see Heeyeon's grey difference in the notebook).

## Before vs after improvements

To show an improvement helped, keep these boxes the same and score both versions:

1. Keep the old functions, e.g. copy them as `vegetation_hsv_texture_old`, or note the commit hash above.
2. Score the old and new versions with the same cell and put both in one table.
3. Look at the failure list above. The fix should raise its own boxes (e.g. a water check raises the lake and pond boxes) **without lowering the others**.

Some fixes don't show up here. Swapping pair 08 changes the direction of the result (gain becomes loss), not which pixels are right. Area in km² doesn't change accuracy either.

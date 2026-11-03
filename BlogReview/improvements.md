# Improvements: What's Left (Polina and Heeyeon)

Tick items when done and write who did it and the commit. Nojus keeps the change map, so improvements should be **functions** his cells can call, not new copies of his cells.

**Before starting any item:** `git pull`, commit only your own cells, push soon after. Notebook conflicts broke the file once already.

**How to show an improvement worked:** run the accuracy check (see [accuracy/README.md](../accuracy/README.md)) before and after the change, using the same boxes. The fix should raise its own boxes **without lowering the others**. Put both numbers in your blog.

Starting point (current code, 1 Nov):

| Method      | Overall | Vegetation | Not vegetation |
| ----------- | ------- | ---------- | -------------- |
| RGB + edges | 75.7%   | 64.3%      | 85.0%          |
| HSV + edges | 73.4%   | 77.8%      | 69.8%          |

---

## Done

- [x] **Pair 08 swap** (Polina). The left half of `Image5.jpeg` is the newer photo: there's a construction site next to the estate, and the estate covers fields that are still there in the right half. `SWAPPED = {"Image5.jpeg"}` in the paths cell, and `split_image` swaps the halves for files in that set. Notebook rerun: pair 08 is now vegetation **loss** (RGB + edges 51.6% → 36.3%, HSV + edges 81.1% → 74.9%). Pairs 01–07 are unchanged. The 08 boxes in `accuracy/labels.py` are swapped to match, so the accuracy numbers stay the same.
- [ ] **Accuracy boxes and scoring** (Polina). `accuracy/` folder: 62 boxes on all 8 pairs, score script, box pictures. _Status: ready, not pushed. Team to check the boxes in `accuracy/boxes/`._

## This week

### Polina

- [ ] **Bar graph cell** (Nojus's cell 18): all 8 pairs grouped by category (forest loss / urban sprawl / data centre), both methods.
- [ ] **Water check**: a function that removes water from the vegetation mask, e.g. green but very low GLI, or green but smooth (few edges) and dark.
  - Measure on the water boxes. Now (RGB / HSV): pair 07 lake 18 / 7 (before) and 9 / 1 (after), pair 05 pond 94 / 67 and 37 / 26, pair 06 pond 48 / 41.
  - Check that the forest boxes don't drop. Forest is dark too.
- [ ] Blog: what you changed, accuracy before → after, and the pair 08 fix (one line).

### Heeyeon

- [x] **Hand-check cell** (Nojus's cell 17): show all categories, and point out the failures (brown trees in 06, lake in 07, building site in 05). Heeyeon: pairs 02 (forest loss), 03, 05, 07 (urban sprawl) and 06 (data centre); yellow boxes on the failures with % right for each method.
- [x] **Speckle clean-up**: a function `clean_mask(mask)` that removes tiny blobs and fills tiny holes (morphological opening and closing). Heeyeon: `clean_mask` removes blobs and fills holes under 25 px by blob size, because 5x5 opening/closing cut the pair 05 forest (36% → 23%) and the pair 03 trees (11–13% → 0–4%). RGB + edges 75.7% → 76.0% (no box worse), HSV + edges 73.4% → 74.4% (03 trees 11–13% → 7–9%, 05 pond 26% → 20%). Change-map blobs drop 3–6x (pair 03: 5894 → 1002), vegetation % changes by 3 points or less. Pair 08 hedges kept. New functions `vegetation_rgb_texture_clean` / `vegetation_hsv_texture_clean` for Nojus's cells.
  - Measure: overall accuracy before → after for both methods, plus how the change maps look.
  - Check that single trees don't disappear (pair 03 trees, pair 08 hedges).
- [ ] Blog: what you changed and accuracy before → after.

### Both

- [ ] Ask Nojus to confirm: detection stays on the **original** images, not brightness-matched ones. Matching changes the result by about 1 point on 6 of 8 pairs.
- [ ] Ask Nojus why HSV is used for the change map and bar graph. Accuracy is nearly tied, so the report needs a reason.

## Next week

Nojus: accuracy write-up. He can use `accuracy/`, check the boxes and add his own.

### Polina

- [ ] **Mask dates, logos and scale bars** on pairs 01, 02, 04, 05, 07 (a rectangle per image that's left out when measuring). Measure on the pair 01 date-label boxes (now 72–85%).
- [ ] **Area in km²** for pairs 01 and 02 using their scale bars. This doesn't change accuracy; it makes the result easier to understand.

### Heeyeon

- [ ] **Align the images**: shift by the measured dx, dy where the response is high (05, 08), and fix pair 06 (about 10 px vertical). Accuracy boxes won't show this, because they're scored on each image separately. Show it in the change maps instead: fewer thin red and green lines along roads and building edges.

## Not fixing (limitations for the report)

- **Brown autumn trees, pair 06** (0% for both methods). Needs near-infrared data, same-season images or machine learning.
- **Dark tree crowns, pair 03 before** (0–13%). Dark pixels have too little colour to judge.

## Housekeeping

- [ ] `Plan.txt`: Step 2 still says detection uses `after_meanstd`. Otsu, mask clean-up and trees vs grass are ticked but not in the code.
- [ ] `to-fix.md`: texture issue is fixed (`14c49d7`). Pair 08 is ticked.
- [x] `.gitignore`: added `__pycache__/` (running the accuracy cell creates it).

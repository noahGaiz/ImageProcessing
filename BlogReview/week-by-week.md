# Week by Week: Blogs vs Code

Legend: ✅ matches code · ⚠️ partly matches / differs · 📝 research or plan only (no code expected yet) · ❌ not in code

---

## Week 1 (28 Sep – 4 Oct): Splitting the images

**Code that week:** `find_divider` (Gaussian blur + Sobel + Canny, white strip check, colour comparison fallback), `split_image`, red-line preview cell, batch loop. Commits `c5374c2` → `5df9520`.

| Who | Blog says | Status |
|---|---|---|
| Nojus ([post](https://c23391116.wordpress.com/2026/10/04/week-1-of-image-processing-project28th-sep-4th-oct/)) | Set up repo, collected 10 images, helped write split code: Case 1 (white gap, Gaussian/Sobel/Canny) and Case 2 (no gap, colour difference) | ✅ |
| Polina ([post](https://d22124948.wordpress.com/2026/10/04/project-week-1-verifying-the-divider-and-splitting-the-images-28-sep-4-oct/)) | Wrote the preview cell (red lines) and batch loop; 10 pairs, Image3 top/bottom, 6 with white gap, 4 without | ✅ |
| Heeyeon ([post](https://d22127506.wordpress.com/2026/10/05/image-processing-project/)) | Wrote `split_image`, divider removal, numbered folders; **says resizing was also done** | ⚠️ Split is correct, but resizing first appears in code on 21 Oct (`350eb3a`), not Week 1 |

---

## Week 2 (5 – 11 Oct): Research week

**Code that week:** comments only (`570693b`, `0096d73`, `43d26eb`).

| Who | Blog says | Status |
|---|---|---|
| Nojus ([post](https://c23391116.wordpress.com/2026/10/12/week2-image-processing-project5-11th-october/)) | Alignment research (manual, ORB/SIFT + homography, overlay check) and vegetation detection (RGB threshold, HSV threshold, ExG). Plans to try manual vs ORB/SIFT and compare RGB vs HSV | 📝 None of it in code yet |
| Polina ([post](https://d22124948.wordpress.com/2026/10/11/project-week-2-matching-brightness-and-contrast-between-images-research-4-oct-11-oct/)) | Brightness/contrast matching: histogram matching, mean/std (Reinhard), regression, pseudo-invariant features. Plans Y-channel histogram matching first, then compare with pseudo-invariant features | 📝 Not in code yet |
| Heeyeon ([post](https://d22127506.wordpress.com/2026/10/12/image-processing-project-week2-5th-oct-11th-oct/)) | Resizing research. Size table for all 10 pairs. Proposes `match_size`: shrink both to the **smaller** size, `INTER_AREA`, warn if >5% different. Says pairs 03, 09, 10 should **not** be plainly stretched | ⚠️ See Week 4 code below: the resize that was added does the opposite |

---

## Week 3 (12 – 18 Oct): What counts as vegetation

**Code that week:** none.

| Who | Blog says | Status |
|---|---|---|
| Nojus ([post](https://c23391116.wordpress.com/2026/10/21/week3-image-processing-project12-18th-october/)) | No time this week (FYP + individual project) | ✅ Honest, nothing to check |
| Polina ([post](https://d22124948.wordpress.com/2026/10/20/project-week-3-12-19-october-research-on-what-rgb-range-do-we-use-to-detect-vegetation/)) | No fixed RGB range works; compares ExG, VARI, GLI; recommends **GLI + Otsu per image**, match brightness first | 📝 Not in code yet |
| Heeyeon ([post](https://d22127506.wordpress.com/2026/10/19/image-processing-project-week3-12th-oct-18th-oct/)) | Defines vegetation as living green plants; edge-case table (shadows, water, green roofs); proposes `excess_green()` function | 📝 Not in code yet |

---

## Week 4 (19 – 25 Oct): code so far

**Code:**
- `350eb3a` (Nojus, 21 Oct): resize loop, `after` stretched to `before`'s size. **Since removed** by `e9ed553`.
- `e9ed553` (Nojus, 21 Oct): **reverted edge-based splitting** (`find_divider` with Gaussian/Sobel/Canny is gone). Images are now cut exactly in half, so both halves are always the same size and no resize is needed. `Plan.txt` updated: resize [x], ORB alignment [-], overlay [x].
- Heeyeon: **overlay check** cell, blends before/after 50/50 for every pair (sharp = aligned, ghosting = misaligned).
- Polina: **Step 2 brightness/contrast matching in YUV** (only the Y channel changes, colour is kept). Two methods: Y histogram matching and Y mean/std matching (Reinhard). Saves `after_histmatched.png` and `after_meanstd.png` per pair, prints Y mean/std, and plots the images with Y histograms.

Polina's Y mean/std results (brightness / contrast):

| Pair | before | after | hist matched | mean/std matched |
|---|---|---|---|---|
| 01 | 99.9 / 47.2 | 105.8 / 53.4 | 99.3 / 47.4 | 99.4 / 47.2 |
| 02 | 108.7 / 22.4 | 155.5 / 49.0 | 108.0 / 22.5 | 108.2 / 22.4 |
| 03 | 89.1 / 71.5 | 92.4 / 66.9 | 88.5 / 71.3 | 87.8 / 69.4 |
| 04 | 128.8 / 46.1 | 129.4 / 60.6 | 128.3 / 46.2 | 128.3 / 46.1 |
| 05 | 142.9 / 42.1 | 125.1 / 39.8 | 142.4 / 41.9 | 142.3 / 41.9 |
| 06 | 108.2 / 39.0 | 108.6 / 56.0 | 107.8 / 39.6 | 107.7 / 39.0 |
| 07 | 77.1 / 39.3 | 102.6 / 50.7 | 76.7 / 39.7 | 76.7 / 39.2 |
| 08 | 119.2 / 54.6 | 109.2 / 47.2 | 118.8 / 54.5 | 118.2 / 52.9 |
| 09 | 128.1 / 87.6 | 115.7 / 82.2 | 127.2 / 86.8 | 123.2 / 80.2 |
| 10 | 177.3 / 36.1 | 139.4 / 56.7 | 177.5 / 33.6 | 176.8 / 36.2 |

Observations:
- Both methods bring `after` brightness/contrast close to `before` on all 10 pairs.
- As predicted in Polina's Week 2 research, matching the whole image can hide real change: in pairs 02 and 03 the cleared (bright) land gets darkened to fit the forested `before`. Pseudo-invariant features (match using unchanged areas only) would avoid this.
- Splitting in half leaves strips of the other image in pair 03 `before` and pair 09 `after` (with axis text/labels), which will skew matching and vegetation %.

Blogs not posted yet. Things to look for in Week 4 posts:
- Nojus explains why edge-based splitting was dropped for a simple half cut (the Week 1 posts all describe the edge method).
- Heeyeon shows overlay results.
- Polina shows the matching results and the "hides real change" limitation.

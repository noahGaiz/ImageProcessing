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
| Nojus ([post](https://c23391116.wordpress.com/2026/10/21/week3-image-processing-project12-18th-october/)) | *Post updated since first review.* Resized pairs to the same size, found it stretched the images, so went back to **cutting each image in half** (drops the edge-based divider). Wider image = side by side, taller = stacked. Keeps white borders (may hold dates/watermarks). Notes the risk if the two halves aren't equal | ✅ Matches `350eb3a` and `e9ed553`, although the commits are dated 21 Oct (Week 4 dates) |
| Polina ([post](https://d22124948.wordpress.com/2026/10/20/project-week-3-12-19-october-research-on-what-rgb-range-do-we-use-to-detect-vegetation/)) | No fixed RGB range works; compares ExG, VARI, GLI; recommends **GLI + Otsu per image**, match brightness first | 📝 Not in code yet |
| Heeyeon ([post](https://d22127506.wordpress.com/2026/10/19/image-processing-project-week3-12th-oct-18th-oct/)) | Defines vegetation as living green plants; edge-case table (shadows, water, green roofs); proposes `excess_green()` function | 📝 Not in code yet |

---

## Week 4 (19 – 25 Oct): code so far

**Code:**
- `350eb3a` (Nojus, 21 Oct, written up in his **Week 3** post): resize loop, `after` stretched to `before`'s size. **Since removed** by `e9ed553`.
- `e9ed553` (Nojus, 21 Oct, written up in his **Week 3** post): **reverted edge-based splitting** (`find_divider` with Gaussian/Sobel/Canny is gone). Images are now cut exactly in half, so both halves are always the same size and no resize is needed. `Plan.txt` updated: resize [x], ORB alignment [-], overlay [x].
- Heeyeon: **overlay check** cell, blends before/after 50/50 for every pair (sharp = aligned, ghosting = misaligned).
- Polina: **Step 2 brightness/contrast matching in YUV** (only the Y channel changes, colour is kept). Two methods: Y histogram matching and Y mean/std matching (Reinhard). Saves `after_histmatched.png` and `after_meanstd.png` per pair, prints Y mean/std, and plots the images with Y histograms.
- `198c62e` (Heeyeon, 26 Oct): **phase correlation shift check** after the overlay (dx, dy, response per pair); fixes the overlay comment.
- `9f21754` (Heeyeon, 26 Oct): **restores the split loop** that `01e9f5b` had deleted (a fresh clone crashed without it) and reads from the repo `Images/`/`pairs/`. Output is pixel-identical to the existing pairs.
- `8343ee2` (Polina, 26 Oct): `Plan.txt` brought in line with the code.
- `4c4e085` (Polina, 26 Oct): **new image set**. Dropped `Forest.jpg`, `Image6.jpeg`, `NY.jpeg` (old pairs 03, 09, 10: the big size differences and the strips/labels left by the half cut), added `image.jpg` (2010 → 2025 farmland to housing). **8 pairs now**, and numbering shifted: old 04 (`Image.jpeg`) is now 03, new image is 04, 05–08 unchanged. Categories: forest loss (01, 02), urban sprawl (03, 04, 05, 07, 08), data centre (06); no mining pair any more.

Polina's Y mean/std results on the 8 new pairs (brightness / contrast, rerun 26 Oct):

| Pair | before | after | hist matched | mean/std matched |
|---|---|---|---|---|
| 01 | 99.9 / 47.2 | 105.8 / 53.4 | 99.3 / 47.4 | 99.4 / 47.2 |
| 02 | 108.7 / 22.4 | 155.5 / 49.0 | 108.0 / 22.5 | 108.2 / 22.4 |
| 03 | 128.8 / 46.1 | 129.4 / 60.6 | 128.3 / 46.2 | 128.3 / 46.1 |
| 04 | 87.1 / 36.5 | 98.5 / 48.9 | 86.5 / 36.6 | 86.6 / 36.5 |
| 05 | 142.9 / 42.1 | 125.1 / 39.8 | 142.4 / 41.9 | 142.3 / 41.9 |
| 06 | 108.2 / 39.0 | 108.6 / 56.0 | 107.8 / 39.6 | 107.7 / 39.0 |
| 07 | 77.1 / 39.3 | 102.6 / 50.7 | 76.7 / 39.7 | 76.7 / 39.2 |
| 08 | 119.2 / 54.6 | 109.2 / 47.2 | 118.8 / 54.5 | 118.2 / 52.9 |

Heeyeon's phase correlation on the 8 new pairs (rerun 26 Oct): dx, dy in px, response 0–1. Only 05 (0.47) and 08 (0.33) have a response high enough to trust; 06 (+9.8 px vertical) agrees with the ghosting seen in the overlay.

| Pair | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 |
|---|---|---|---|---|---|---|---|---|
| dx, dy | −4.1, −1.3 | +6.3, −3.6 | −14.6, −1.2 | −2.8, +1.7 | −0.4, −2.1 | +0.4, +9.8 | −11.1, +54.6 | −2.2, −0.2 |
| response | 0.08 | 0.04 | 0.07 | 0.05 | 0.47 | 0.11 | −0.00 | 0.33 |

Observations:
- Both methods bring `after` brightness/contrast close to `before` on all 8 pairs. Mean/std is slightly off on pair 08 because 3.5% of its pixels are clipped to 0–255 (0.6% on 05, none elsewhere); unclipped it matches exactly.
- As predicted in Polina's Week 2 research, matching the whole image distorts real change: in pair 02 the cleared (bright) land gets darkened to fit the forested `before` (bright pixels Y ≈ 206 → 125–131), and in pair 04 the construction sites get darkened towards the 2010 fields (Y ≈ 202 → 163), with both methods. Pseudo-invariant features (match using unchanged areas only) would avoid this.
- The half-cut strips from old pairs 03 and 09 are gone with those images. Dates, logos and scale bars are still printed on 01, 02, 04, 05, 07 and will skew matching and vegetation % unless masked.
- Pair 08 may have before/after swapped (housing estate on the left, open fields on the right). Check before running detection.

| Who | Blog says | Status |
|---|---|---|
| Nojus ([post](https://c23391116.wordpress.com/2026/10/25/week4-image-processing-project19th-25th-october/)) | Vegetation detection: RGB rule (G > R and G > B) and HSV (hue 35–85, S and V ≥ 40). Both miss the brown autumn trees in pair 06, so he adds an edge-density texture mask (grey → Gaussian → Canny → density per window → threshold → closing/opening). Compares RGB+edges vs HSV+edges; edge threshold 0.12–0.4 gives 42.6%–0.0% on pair 06, picks 0.15 (31.3%). Limitation: tested on one pair, bare soil also has texture | ✅ Pushed in `716b259` (26 Oct); pair 06 result (31.3% at 0.15) matches the code. ⚠️ On all 8 pairs the texture mask also counts buildings/streets as vegetation (see [to-fix.md](to-fix.md)). No references or next steps in the post |
| Polina ([post](https://d22124948.wordpress.com/2026/10/26/project-week-4-matching-brightness-and-contrast-in-yuv-implementation-19-25-oct/)) | Y histogram matching vs Y mean/std matching on all 8 pairs; results table; figures for pairs 02, 04, 06; limitation: matching darkens real change (02, 04); printed labels; colour not corrected (Nojus's pair 06). References [1]–[4] (IEEE) | ✅ Matches the code and rerun numbers. No "Next week" section |
| Heeyeon ([post](https://d22127506.wordpress.com/2026/10/27/image-processing-project-week4-19th-oct-25th-oct/)) | 50/50 overlay check plus phase correlation on all 8 pairs; only pair 06 clearly shifted (~10 px vertical); resizing correction; references [1]–[3] | ✅ Matches `198c62e` (cell restored in `7499724` after it was dropped in `a20f45d`) |

Things to look for in the remaining Week 4 posts:
- Heeyeon shows overlay results.
- Polina shows the matching results and the "hides real change" limitation.

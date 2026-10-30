# Splitting the Last Two Notebook Cells (Heeyeon + Polina)

Nojus is taking the **change map** cell (`#before | after | change map for every pair`). He says the next two cells, the **hand-check** and the **bar graph**, should be divided between Heeyeon and Polina. This note explains what those cells do now, how they could be split, and what Heeyeon should change in her next post.

## What changed in the code (29–30 Oct, Nojus)

- **Better detection.** Green is now judged by colour *proportions* instead of raw values. The HSV rule also needs a small green signal (normalised ExG > 0.02). Edges only count as vegetation where there is green nearby, so houses and streets no longer count.
- **Detection uses the original images** (`before.png`, `after.png`), **not** the brightness-matched ones. Nojus's reason: brightness matching doesn't fix seasonal leaf colour. Polina tested it: running his detection on the matched images changes vegetation % by at most about 5 points, usually 1–2.
- **Still missed:** the brown autumn trees in pair 06 (only about 3% of the after image counts as vegetation).
- **No Otsu yet.** `Plan.txt` ticks "ExG with automatic threshold (Otsu)", but the code only uses ExG with a fixed 0.02 threshold inside the HSV rule.

## The two cells

| Cell | What it does now | What's missing |
|---|---|---|
| **Hand-check** (`#hand-check: photo next to the same photo with detected vegetation tinted green`) | Shows pairs 02, 03 and 06, before and after, with the pixels each method calls vegetation tinted green (HSV and RGB) | It's only a visual check. There is no number saying how *accurate* the methods are |
| **Bar graph** (`# Compare vegetation coverage for three example categories`) | Bar chart of vegetation % before and after for pair 02 (forest), 03 (urban) and 06 (seasonal), HSV method only | Only 3 of the 8 pairs and one method. No category comparison across all pairs |

## How we could split them

### Option A (suggested)

- **Heeyeon: hand-check → accuracy score** (Plan Step 5)
  - Pick 3–4 pairs (for example 02 forest, 03 urban, 06 seasonal, 04 new housing).
  - On each, mark a few small areas by eye as "vegetation" or "not vegetation". These are the ground truth.
  - For each method (RGB + edges, HSV + edges, and her own ExG + Otsu), report the % of marked pixels it gets right, before and after.
  - Fits her work: this was already in her Week 3 and Week 4 plans ("hand-label a few small reference areas"), and her Week 3 definition of vegetation and edge-case table (shadows, water, green roofs, brown vegetation) say what to label.
- **Polina: bar graph → results by category** (Plan Step 6, "compare results by category")
  - All 8 pairs, grouped as forest loss (01, 02), urban sprawl (03, 04, 05, 07, 08) and data centre / seasonal (06).
  - Both methods side by side.
  - One extra bar or note showing that brightness matching changes the result very little.
  - Fits her work: it uses her matching results and her Week 4 categories, and it's the summary chart for the report.

### Option B (swap)

- **Heeyeon: bar graph.** Add her ExG + Otsu as a third method, and compare all 8 pairs by category.
- **Polina: hand-check → accuracy score.** Use the hand-labelled areas, and test her GLI + Otsu idea from Week 3 against Nojus's methods.

### Either way

- **ExG + Otsu (Heeyeon) and GLI + Otsu (Polina)** can each be added as a new method function next to Nojus's. Then both cells, and Nojus's change map, can use them.
- **Pair 08** may have before and after swapped (houses on the left, fields on the right). Check it before it goes into the bar graph or the accuracy test.
- **Pull before starting** and commit only your own cell, so the notebook doesn't get conflict markers again.

## What Heeyeon should change in her blog

**Week 4 post: nothing has to change.** It was correct for the code at the time. If she wants, she can add a short update note at the bottom: "Update (30 Oct): detection now uses the original images, not the brightness-matched ones, so `excess_green()` will run on the original images."

**Next post (Week 5):**
- Run `excess_green()` on the **original** images, not the brightness-matched ones. This replaces the Week 4 plan "using the aligned, brightness-matched images (Polina's Y matching)".
- Nojus's HSV method already uses a normalised ExG with a fixed threshold (0.02). To add something new, her ExG should use **Otsu** (an automatic threshold for each image), as a separate method compared with his RGB and HSV methods.
- Link [Nojus's Week 5 post](https://c23391116.wordpress.com/2026/10/30/week5-image-processing-project26th-october-to-1st-of-november/) (change maps) and say which cell she took and why.
- Her alignment plan (shift pairs by dx, dy, or ORB + homography for pair 08) is still valid. Alignment matters more now that change maps compare pixel by pixel.
- Keep IEEE references, and add one 2020+ paper if it fits (for example on accuracy assessment or ExG / Otsu).

## To decide

- [ ] Option A or B (or another split)?
- [ ] Should ExG + Otsu and GLI + Otsu go in as new method functions, or just inside each person's cell?
- [ ] Who checks pair 08?

# To Fix Before Final Submission

Tick items off as they're resolved, and note who fixed it.

## Code vs blog differences

- [x] ~~**Resize method.**~~ No longer applies: `e9ed553` cuts images exactly in half, so halves are always the same size and the resize code was removed.
- [ ] **Splitting method changed.** All Week 1 posts describe the edge-based `find_divider` (Gaussian/Sobel/Canny), but `e9ed553` replaced it with a half cut. Nojus explains it in his Week 3 post; Polina and Heeyeon should link to it in their Week 4 posts, and the report should explain it.
- [ ] **Half cut leaves strips** of the other image in pair 03 `before` and pair 09 `after` (axis text too). Crop these before vegetation detection, or note as a limitation.
- [ ] **Resizing timeline.** Heeyeon's Week 1 post says resizing was done; it was actually done by Nojus in Week 3 (his post; commit dated 21 Oct) and then removed. Clarify in the post or the report.
- [ ] **Heeyeon's Week 2 resizing research** (`match_size`, interpolation comparison) is no longer used in code. Mention in the report why it's not needed now.
- [ ] **Feature alignment** (Nojus, Week 2 plan): ORB/SIFT + homography: not implemented (marked [-] in `Plan.txt`). Overlay check done by Heeyeon.
- [x] **Brightness/colour matching** (Polina, Week 2 plan): Y histogram matching and Y mean/std matching added. Still open: pick one, and test pseudo-invariant features (matching distorts real change: darkens cleared land in pair 02, blows the mine out to near white in pair 03).
- [ ] **Vegetation detection** (Heeyeon `excess_green()`, Polina GLI + Otsu): not implemented yet.
- [ ] **Nojus's Week 4 detection code** (RGB/HSV + edge-density texture, results for pair 06) is described in his blog but not pushed to GitHub. Push it so the blog and repo match, and run it on all 10 pairs, not just 06.

## Team decisions needed

- [ ] **Pick one detection method** and say why in the blogs/report. Options so far:
  - `Plan.txt`: ExG + Otsu
  - Polina (Week 3): GLI + Otsu
  - Nojus (Week 2, tried in Week 4): RGB / HSV thresholds + edge-density texture
- [ ] **Agree the vegetation definition** (Heeyeon proposed "living green plants", Week 3).
- [ ] **Decide what to do with pairs 03, 09, 10** (big size differences): fix divider, crop, or align.

## Blog references

- [ ] Polina, Week 2: references [2]–[6] have placeholder authors/years/journals.
- [ ] Nojus, Week 2: two sources listed only as PDF filenames (`1-s2.0-S2214317315000347-main.pdf`, `Rtm005 9..23`). Add proper titles/authors.

## Repo housekeeping

- [x] Update `Plan.txt` checkboxes for Step 1 (done by Nojus in `e9ed553`).
- [ ] Tick Step 2 "Match colours of after to before" in `Plan.txt` once the team agrees on the matching method.
- [ ] Check `9dd6536` `.gitignore` change: make sure images/`pairs/` aren't committed by accident.

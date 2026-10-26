# To Fix Before Final Submission

Tick items off as they're resolved, and note who fixed it.

## Code vs blog differences

- [x] ~~**Resize method.**~~ No longer applies: `e9ed553` cuts images exactly in half, so halves are always the same size and the resize code was removed.
- [ ] **Splitting method changed.** All Week 1 posts describe the edge-based `find_divider` (Gaussian/Sobel/Canny), but `e9ed553` replaced it with a half cut. Nojus explains it in his Week 3 post; Polina and Heeyeon should link to it in their Week 4 posts, and the report should explain it. Heeyeon: done (Week 4 post links Nojus's Week 3). Still open: Polina's Week 4 post, report.
- [x] ~~**Half cut leaves strips** of the other image in pair 03 `before` and pair 09 `after` (axis text too).~~ Resolved by `4c4e085`: those images were dropped from the set (26 Oct). In the new set, thin strips of the other half remain on the right edge of pairs 03 and 08 (noted as a limitation in Heeyeon's Week 4 post).
- [ ] **Printed dates, logos and scale bars** on pairs 01, 02, 04, 05, 07. Crop or mask before vegetation detection, or note as a limitation.
- [ ] **Pair 08 may be swapped** (housing estate in the left half, open fields in the right). Check which half is really `before`; if swapped, detection will report vegetation gained instead of lost.
- [x] **Resizing timeline.** Heeyeon's Week 1 post says resizing was done; it was actually done by Nojus in Week 3 (his post; commit dated 21 Oct) and then removed. Clarify in the post or the report. Heeyeon: Update note added to Week 1, correction in Week 4.
- [ ] **Heeyeon's Week 2 resizing research** (`match_size`, interpolation comparison) is no longer used in code. Mention in the report why it's not needed now. Explained in Heeyeon's Week 4 post ("Resizing" paragraph). Still open: copy it into the report.
- [ ] **Feature alignment** (Nojus, Week 2 plan): ORB/SIFT + homography: not implemented (marked [-] in `Plan.txt`). Overlay check done by Heeyeon, plus a phase correlation shift measurement (`198c62e`): only pair 06 is clearly shifted (~10 px vertical).
- [x] **Brightness/colour matching** (Polina, Week 2 plan): Y histogram matching and Y mean/std matching added. Still open: pick one, and test pseudo-invariant features (matching distorts real change: darkens cleared land in pair 02 and the new construction in pair 04).
- [ ] **Vegetation detection** (Heeyeon `excess_green()`, Polina GLI + Otsu): not implemented yet.
- [ ] **Nojus's Week 4 detection code** (RGB/HSV + edge-density texture, results for pair 06) is described in his blog but not pushed to GitHub. Push it so the blog and repo match, and run it on all 8 pairs, not just 06.

## Team decisions needed

- [ ] **Pick one detection method** and say why in the blogs/report. Options so far:
  - `Plan.txt`: ExG + Otsu
  - Polina (Week 3): GLI + Otsu
  - Nojus (Week 2, tried in Week 4): RGB / HSV thresholds + edge-density texture
- [ ] **Agree the vegetation definition** (Heeyeon proposed "living green plants", Week 3).
- [x] ~~**Decide what to do with pairs 03, 09, 10** (big size differences): fix divider, crop, or align.~~ Dropped from the image set in `4c4e085` (26 Oct); `image.jpg` added, 8 pairs now. Everyone's Week 4 post should say so.

## Blog references

- [x] ~~Polina, Week 2: references [2]–[6] have placeholder authors/years/journals.~~ Fixed on the live post (full IEEE list, checked 26 Oct).
- [ ] Nojus, Week 2: two sources listed only as PDF filenames (`1-s2.0-S2214317315000347-main.pdf`, `Rtm005 9..23`). Add proper titles/authors.

## Repo housekeeping

- [x] Update `Plan.txt` checkboxes for Step 1 (done by Nojus in `e9ed553`).
- [ ] Tick Step 2 in `Plan.txt` once the team agrees on the matching method (marked [-] for now in `8343ee2`).
- [x] Check `9dd6536` `.gitignore` change. Source images are now committed on purpose in `Images/` (`1cdcd6c`, `4c4e085`); `pairs/` is still ignored.
- [x] Split loop was deleted by Nojus's cleanup (`01e9f5b`), so a fresh clone crashed; restored by Heeyeon in `9f21754`, which also points the notebook at the repo `Images/` and `pairs/`.
- [x] `Plan.txt` updated to match the code (`8343ee2`): half cut doesn't crop labels (new open item), 8 pairs, no resize needed.

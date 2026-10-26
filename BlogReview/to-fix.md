# To Fix Before Final Submission

Tick items off as they're resolved, and note who fixed it.

## Code vs blog differences

- [x] ~~**Resize method.**~~ No longer applies: `e9ed553` cuts images exactly in half, so halves are always the same size and the resize code was removed.
- [ ] **Splitting method changed.** All Week 1 posts describe the edge-based `find_divider` (Gaussian/Sobel/Canny), but `e9ed553` replaced it with a half cut. Nojus explains it in his Week 3 post; Polina and Heeyeon should link to it in their Week 4 posts, and the report should explain it. Heeyeon: done (Week 4 post links Nojus's Week 3). Polina: done (Week 4 post explains the switch to the centre cut). Still open: report.
- [x] ~~**Half cut leaves strips** of the other image in pair 03 `before` and pair 09 `after` (axis text too).~~ Resolved by `4c4e085`: those images were dropped from the set (26 Oct). In the new set, thin strips of the other half remain on the right edge of pairs 03 and 08 (noted as a limitation in Heeyeon's Week 4 post).
- [ ] **Printed dates, logos and scale bars** on pairs 01, 02, 04, 05, 07. Crop or mask before vegetation detection, or note as a limitation.
- [ ] **Pair 08 may be swapped** (housing estate in the left half, open fields in the right). Check which half is really `before`; if swapped, detection will report vegetation gained instead of lost. The colour-only masks already show a gain on 08 (RGB 21.7% → 32.3%), which fits a swap.
- [x] **Resizing timeline.** Heeyeon's Week 1 post says resizing was done; it was actually done by Nojus in Week 3 (his post; commit dated 21 Oct) and then removed. Clarify in the post or the report. Heeyeon: Update note added to Week 1, correction in Week 4.
- [ ] **Feature alignment** (Nojus, Week 2 plan): ORB/SIFT + homography: not implemented (marked [-] in `Plan.txt`). Overlay check done by Heeyeon, plus a phase correlation shift measurement (`198c62e`): only pair 06 is clearly shifted (~10 px vertical).
- [x] **Brightness/colour matching** (Polina, Week 2 plan): Y histogram matching and Y mean/std matching added. Still open: pick one (Nojus's detection already reads `after_meanstd.png`, so mean/std is the de facto choice; team to confirm), and test pseudo-invariant features (matching distorts real change: darkens cleared land in pair 02 and the new construction in pair 04).
- [ ] **Vegetation detection.** Nojus's RGB/HSV + edge-density texture is now in the notebook (`716b259`, run on all 8 pairs). Heeyeon's `excess_green()` and Polina's GLI + Otsu are not implemented yet.
- [x] ~~**Nojus's Week 4 detection code** is described in his blog but not pushed to GitHub.~~ Pushed in `716b259` and runs on all 8 pairs. His pair 06 number (31.3% at threshold 0.15) matches the code. Small mismatch: the threshold-test cell now uses `pair_number = 3`, while his blog shows the test on pair 06.
- [ ] **Texture mask counts buildings and streets as vegetation** (Nojus). The detection marks a pixel as vegetation if it is green OR has many edges, and houses, roofs and roads have many edges too, so real loss gets hidden. Pair 02: colour only (RGB) 89.5% → 56.6%, but RGB + edges 97.2% → 95.0%. Pair 03 (fields → housing): RGB + edges rises 72.5% → 74.6%, texture alone is ~72% on both halves. Pair 06 looks right, which is why the Week 4 test on 06 alone didn't show it. His Week 4 post is fine as written; fix in code (e.g. only count edges where the colour is also green/brown) and report it on all 8 pairs in his next post. This also matters for Polina's "non-vegetation in both images" matching idea, which needs masks that don't call almost everything vegetation.

## Team decisions needed

- [ ] **Pick one detection method** and say why in the blogs/report. Options so far:
  - `Plan.txt`: ExG + Otsu
  - Polina (Week 3): GLI + Otsu
  - Nojus (Week 2, tried in Week 4): RGB / HSV thresholds + edge-density texture
- [ ] **Agree the vegetation definition** (Heeyeon proposed "living green plants", Week 3).
- [x] ~~**Decide what to do with pairs 03, 09, 10** (big size differences): fix divider, crop, or align.~~ Dropped from the image set in `4c4e085` (26 Oct); `image.jpg` added, 8 pairs now. Everyone's Week 4 post should say so.

## Future work (final report)

- [ ] **Heeyeon's Week 2 resizing research** (`match_size`, interpolation comparison) is no longer used in code, because the half cut always gives equal-sized halves. Already explained in Heeyeon's Week 4 post ("Resizing" paragraph). For the report: say why it isn't needed now, and that it would be needed if we split at a divider again or add images from other sources.

## Blog references

- [x] ~~Polina, Week 2: references [2]–[6] have placeholder authors/years/journals.~~ Fixed on the live post (full IEEE list, checked 26 Oct).
- [ ] Nojus, Week 4: no references and no next steps in the post. Add them in his next post.
- [ ] Polina, Week 4: no "Next week" section (optional, helps Blog: Progress). Could add one paragraph at the end.
- [ ] Nojus, Week 2: two sources listed only as PDF filenames (`1-s2.0-S2214317315000347-main.pdf`, `Rtm005 9..23`). Add proper titles/authors.

## Repo housekeeping

- [x] Update `Plan.txt` checkboxes for Step 1 (done by Nojus in `e9ed553`).
- [ ] Tick Step 2 in `Plan.txt` once the team agrees on the matching method (marked [-] for now in `8343ee2`; `7499724` notes that detection uses mean/std).
- [x] Check `9dd6536` `.gitignore` change. Source images are now committed on purpose in `Images/` (`1cdcd6c`, `4c4e085`); `pairs/` is still ignored.
- [x] Split loop was deleted by Nojus's cleanup (`01e9f5b`), so a fresh clone crashed; restored by Heeyeon in `9f21754`, which also points the notebook at the repo `Images/` and `pairs/`.
- [x] `Plan.txt` updated to match the code (`8343ee2`): half cut doesn't crop labels (new open item), 8 pairs, no resize needed.
- [x] Merge `7910550` (Nojus) left conflict markers in the notebook and `Plan.txt`, so the notebook wouldn't open; his fix `a20f45d` kept an older notebook and dropped the split loop, Heeyeon's phase correlation cell and the repo `Images/` path. Restored by Polina in `7499724` (all cells run on the 8 pairs). Everyone: `git pull` before committing.

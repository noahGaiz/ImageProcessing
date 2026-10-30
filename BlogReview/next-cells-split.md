# Who Does What Next (Proposal)

Nojus suggested splitting the **hand-check** and **bar graph** cells between Heeyeon and Polina. Polina's counter-proposal: **Nojus keeps those two cells** (he wrote them and the change map), and Heeyeon and Polina take on improvements to the pipeline instead. **Nojus, please confirm.**

## What changed in the code (29–30 Oct, Nojus)

- **Better detection.** Green is now judged by colour *proportions* instead of raw values. The HSV rule also needs a small green signal (normalised ExG > 0.02). Edges only count as vegetation where there is green nearby, so houses and streets no longer count.
- **Detection uses the original images** (`before.png`, `after.png`), **not** the brightness-matched ones. Polina tested it: running his detection on the matched images changes vegetation % by at most about 5 points, usually 1–2.
- **Still missed:** the brown autumn trees in pair 06 (only about 3% of the after image counts as vegetation).

## Proposed split

| Who | Work | Why it matters |
|---|---|---|
| **Nojus** | Change map, hand-check and bar graph cells. Could turn the hand-check into an **accuracy score**: label a few small areas by eye as vegetation / not vegetation, then report how often each method is right | At the moment nobody can say whether the results are correct. An accuracy score shows which method to trust |
| **Heeyeon** | **Align the images** before the change map, using her measured shifts (pair 06 is about 10 px off), or ORB + homography where the shift isn't reliable | Change maps compare pixel by pixel, so misalignment shows up as fake loss and gain along edges |
| **Heeyeon** | **Clean up the masks**: remove small specks and fill small holes (morphological opening and closing) | The latest detection code has no clean-up step, so the masks and change maps are speckled |
| **Polina** | **GLI + Otsu** as a new detection method next to Nojus's RGB and HSV methods (from her Week 3 research) | Gives a real comparison. If Nojus's method scores better, that's evidence it's the right choice |
| **Polina** | **Mask printed dates, logos and scale bars** on pairs 01, 02, 04, 05 and 07 | They are counted as land in the vegetation % |
| **Polina** | **Area in km²** for pairs 01 and 02, using their scale bars | "X km² of forest lost" is clearer than a percentage |
| **Whoever has time** | **Pair 06 brown autumn trees**, which every method calls "lost" | The biggest known wrong result |

New methods and fixes should be functions the existing cells can use, so Nojus's change map, hand-check and bar graph can show them too.

Before starting:
- **Pair 08** may have before and after swapped (houses on the left, fields on the right). Someone needs to check.
- **Pull before you start**, and commit only your own cells, so the notebook doesn't get conflict markers again.

## What Heeyeon should change in her blog

**Week 4 post: nothing has to change.** It was correct for the code at the time. If she wants, she can add a short update note at the bottom saying detection now uses the original images, not the brightness-matched ones.

**Next post (Week 5):**
- Her Week 4 plan said she'd run `excess_green()` on the brightness-matched images. Detection now uses the original images, and Nojus's HSV method already includes a normalised ExG check, so explain that the plan changed and why.
- Write about her new work (alignment and mask clean-up), and show change maps before and after aligning.
- Link [Nojus's Week 5 post](https://c23391116.wordpress.com/2026/10/30/week5-image-processing-project26th-october-to-1st-of-november/) (change maps).
- Keep IEEE references, and add one 2020+ paper if it fits (for example on image registration for change detection).

## To decide

- [ ] Nojus: OK to keep the hand-check and bar graph (and do the accuracy score)?
- [ ] Heeyeon: OK with alignment + mask clean-up?
- [ ] Who checks pair 08?
- [ ] Who takes pair 06?

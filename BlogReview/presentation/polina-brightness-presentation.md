# Presentation: Polina's Part (Brightness Matching)

The story in one line: **I researched and built brightness matching. Then Nojus's improved detection turned out not to need it, and my test showed why.** That makes a good presentation point: we tested the step and have evidence for dropping it.

Figures are in this folder and were made from the notebook's own functions on our 8 pairs.

---

## Slide 1: The problem

**Title:** Why brightness matters

- Before and after photos are taken years apart, with a different sun, season, haze and camera.
- The after photo is often brighter or darker overall (e.g. pair 07: average brightness 77 before, 103 after).
- A colour rule could mistake "brighter" for "the land changed".

**Visual:** `matching_pair07.png` (top row only, or the whole figure)

**Say:** "If one photo is just brighter, a simple rule might report vegetation change that didn't happen. So in Week 2 I looked at how to make the two photos equally bright first."

---

## Slide 2: Research (Week 2)

**Title:** Four ways to match brightness

| Method | Idea | Note |
|---|---|---|
| Histogram matching | Reshape after's brightness distribution to match before's | Standard method [1] |
| Mean / std matching | Match the average brightness and the spread (contrast) | Reinhard et al. [2] |
| Regression | Fit a line from after's values to before's | Needs matching points |
| Pseudo-invariant features | Match using only areas that didn't change (roads, roofs) | Most accurate, more work [3], [4] |

**Decision:** change only the **Y (brightness) channel in YUV**, so the colours stay exactly the same. Colour is what detection uses.

**Say:** "I picked the two simplest methods to build first, and worked on brightness only so I wouldn't change the colours."

---

## Slide 3: What I built (Week 4)

**Title:** Two methods, on all 8 pairs

- `match_histogram_y`: histogram matching on Y.
- `match_mean_std_y`: mean/std matching on Y.
- Each saves a matched after image (`after_histmatched.png`, `after_meanstd.png`) and prints the before/after brightness numbers.

**Visual:** `matching_pair07.png`. The after image's mean goes from 103 to 77 and its spread from 51 to 39, the same as before.

**Result:** both methods bring the after image to the same brightness and contrast as before on all 8 pairs.

---

## Slide 4: The limitation

**Title:** Matching can hide real change

- Matching treats the **whole** image as "should look the same".
- In pair 02 the forest was cleared, so the after image is brighter for a **real** reason. Matching darkened the cleared land to look more like the old forest.
- The same thing happens to the building sites in pair 04.

**Visual:** `matching_hides_change_pair02.png`

**Say:** "This is the trade-off I predicted in my research. The fix would be pseudo-invariant features: match using only the parts that didn't change."

---

## Slide 5: Testing it with the detection

**Title:** Does matching change the vegetation result?

- Nojus improved his detection (29–30 Oct) to use colour **proportions**, and switched it to read the original images.
- I tested his detection on the original after image vs my matched one, for all 8 pairs:

| Pair | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 |
|---|---|---|---|---|---|---|---|---|
| Difference (% points, HSV + edges) | −0.4 | +4.8 | −1.0 | +1.0 | −5.3 | −0.5 | +0.8 | −0.8 |

- 6 of 8 pairs change by about 1 point or less. The biggest are 02 (+4.8) and 05 (−5.3), where the brightness gap was largest.

**Visual:** `detection_original_vs_matched.png`

---

## Slide 6: Why, and what it means

**Title:** Proportions don't care about brightness

- A forest pixel (R 60, G 90, B 50): green is 90 of 200 = **45%**.
- The same pixel made brighter (90, 135, 75): green is 135 of 300 = **still 45%**.
- His rules ask "is green the biggest share?", so making a pixel brighter doesn't change the answer.

**Conclusion:**
- For our final method, matching **isn't needed**, so the pipeline runs on the original images. That also avoids the limitation from slide 4.
- It would still matter for rules that use raw values or a fixed brightness cut-off, or for images with very different lighting.
- The work wasn't wasted: the research and the test are the **evidence** for leaving this step out.

**Say:** "I didn't just drop the step. I tested it, and the test shows why our detection doesn't need it."

---

## Possible questions

- **"So was your part useless?"** No. Without the test, we wouldn't know the detection is robust to brightness. Skipping a step needs evidence, and this is it.
- **"Why did pairs 02 and 05 change most?"** They have big brightness gaps (02: 109 to 155; 05: 143 to 125). Not every part of the detection uses proportions: the edge detector (Canny) and HSV's minimum brightness and saturation use fixed cut-offs, and those react to brightness and contrast. So a few pixels near those cut-offs flip.
- **"Which method would you pick if you had to?"** Mean/std. It's simpler and gave the same result as histogram matching on our pairs.
- **"What would you do with more time?"** Pseudo-invariant features: match brightness using only the unchanged areas.

---

## References

Use the full IEEE entries from my [Week 4 post](https://d22124948.wordpress.com/2026/10/26/project-week-4-matching-brightness-and-contrast-in-yuv-implementation-19-25-oct/):

- [1] Gonzalez & Woods, *Digital Image Processing* (histogram matching)
- [2] Reinhard et al., 2001, "Color transfer between images" (mean/std matching)
- [3] Hong & Zhang, 2005 (radiometric normalisation)
- [4] Sharaf El Din, 2022 (radiometric normalisation)

## Before presenting

- [ ] Check with the team that we're officially keeping detection on the original images. Nojus switched it, but it was never agreed.
- [ ] Rerun the notebook if the detection code changes again, because the numbers on slide 5 come from the 30 Oct version.

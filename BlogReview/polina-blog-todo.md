# Polina: What to Add to My Blog

Blog: https://d22124948.wordpress.com/

## Week 4 post (19 – 25 Oct): Implementing brightness/contrast matching in YUV

Weeks 2 and 3 were research only. This post should show the research turned into code with real results.

### Checklist

- [ ] **Recap (1–2 lines):** Week 2 research recommended histogram matching on the Y channel first. This week I implemented it, plus mean/std matching to compare.
- [ ] **Why YUV:** Y = brightness, U/V = colour. Changing only Y fixes lighting differences without changing the green of the vegetation, which we need for detection later.
- [ ] **Method 1: Y histogram matching.** Build the cumulative histogram (CDF) of Y for before and after, then map each after brightness to the before brightness with the same CDF value (`np.interp` lookup table).
- [ ] **Method 2: Y mean/std matching (Reinhard et al. 2001).** Mean of Y = brightness, std of Y = contrast. `new_y = (after_y - after_mean) * (before_std / after_std) + before_mean`, clipped to 0–255.
- [ ] **Short code snippet** of one function (e.g. `match_mean_std_y`), not the whole notebook.
- [ ] **Results table:** Y mean/std for before, after, and both matched versions (copy from [week-by-week.md](week-by-week.md), Week 4). Point out a big case like pair 02: after 155.5/49.0 → matched 108.2/22.4, before is 108.7/22.4.
- [ ] **Figure:** screenshot of the plot cell for 2–3 pairs (before, after, hist matched, mean/std matched, Y histogram). Good examples:
  - Pair 02: big brightness difference, matching clearly fixes it.
  - Pair 10: after is darker/more contrasty, both methods bring it back.
  - Pair 03: shows the limitation below (histogram matching blows the mine out to near white).
- [ ] **Comparison:** both methods get very close to the before values. Histogram matching matches the whole shape of the histogram; mean/std only matches the average and spread, so it's gentler and the histogram shape stays the same.
- [ ] **Limitation (important, links back to Week 2 research):** matching the whole image distorts the area that really changed, because the correction is calculated from the whole image, including the changed part. In pair 02 the bright cleared land gets darkened to fit the forested before image, so the change looks smaller. In pair 03 histogram matching does the opposite: the mine gets brighter (average Y 233 → 249) and turns almost white, while mean/std matching barely changes it. This is exactly the drawback of histogram matching from my Week 2 sources.
- [ ] **Other issue found:** the half cut leaves strips of the other image in pair 03 before and pair 09 after (with axis text), which affects the brightness stats.
- [ ] **Team context (one line each):** Nojus switched splitting to a simple half cut for consistency (his Week 3 post) and tried RGB/HSV + edge-texture detection (his Week 4 post); Heeyeon added the 50/50 overlay check. Matching runs on the half-cut pairs.
- [ ] **Next week:** try pseudo-invariant features (calculate the correction from unchanged areas like roads/roofs only), then pick one matching method with the team before vegetation detection (my GLI + Otsu from Week 3, Heeyeon's ExG, or Nojus's RGB/HSV + edge texture from his Week 4 post).
- [ ] **Link to Nojus's Week 4 (one line):** his colour thresholds missed the brown autumn trees in pair 06. Y-only matching keeps U/V unchanged, so it won't fix seasonal colour differences like that (and won't create fake ones either). That's why detection still needs something like his texture mask or an Otsu threshold per image.
- [ ] **References:** Reinhard et al. 2001 (mean/std), plus the histogram matching sources from Week 2.

### Rubric boosts (see [rubric.md](rubric.md))

- [ ] **Blog: Content**: include real screenshots and the results table (demonstration of methods and results).
- [ ] **Research: Citations**: IEEE style, numbered [1], [2] in the text with a full reference list.
- [ ] **Research: Publications**: add at least one recent (2020+) peer-reviewed paper on radiometric normalisation / change detection next to Reinhard 2001.
- [ ] **Research: Comparisons**: compare the two methods with numbers (the Y mean/std table), not just in words.
- [ ] **Design: Testing**: say it was tested on all 10 pairs covering forest, mining, urban sprawl and a data centre.
- [ ] **Design: Innovation** (next week idea): use pixels that are non-vegetation in both images as the "unchanged areas" for matching.

### Suggested title

"Project Week 4: Matching Brightness and Contrast in YUV: Implementation (19 – 25 Oct)"

## Fixes to earlier posts

- [ ] **Week 2:** references [2]–[6] still have placeholder authors/years/journals. Fill them in.
- [ ] **Week 1:** describes the edge-based divider (Gaussian/Sobel/Canny), which the code no longer uses. No need to rewrite it; just mention the switch to the half cut in Week 4 so the blog and code agree.
- [ ] **Week 3:** recommended GLI + Otsu. When the team picks a detection method, say in a later post whether GLI was chosen and why.

# Heeyeon: What to Add to Her Blog

Blog: https://d22127506.wordpress.com/

## Week 4 post (19 – 25 Oct): Checking alignment with a 50/50 overlay

Weeks 2 and 3 were research (resizing, then "what counts as vegetation"). Her code this week is the **overlay check** cell in `VegetationChange.ipynb`, which blends `before` and `after` 50/50 for every pair. This post should show that code and what it found.

### Suggested title

"Image Processing Project: Week4 (19th Oct – 25th Oct)"

### Checklist (same layout as her Week 3 post: H2/H3 headings, bullets, one table, IEEE references)

- [ ] **Recap (1–2 lines):** Week 2 looked at resizing, Week 3 defined vegetation and proposed `excess_green()`. Before we compare vegetation pixel by pixel, we need to know the two images actually line up.
- [ ] **Team context (one line, link [Nojus's Week 3 post](https://c23391116.wordpress.com/2026/10/21/week3-image-processing-project12-18th-october/)):** in Week 3 Nojus first resized the pairs, found that it stretched the images, and then went back to cutting each image exactly in half (dropping the edge-based Gaussian/Sobel/Canny divider from our Week 1 posts). Both halves are now always the same size, so no resizing is needed. Her overlay check runs on these half-cut pairs.
  - Add one honest line correcting Week 1: "In Week 1 I wrote that we resized the images. Resizing was actually done later, by Nojus in Week 3, and then replaced by the half cut, which makes it unnecessary." (No need to edit the old post.)
  - Add one line on Week 2: her `match_size` research isn't used now, but it would be needed if we ever go back to splitting at the divider or add images from other sources.
- [ ] **Why an overlay check:** if the two images are shifted even a few pixels, a road or roof edge in `before` lands on grass in `after`, and it shows up as fake vegetation change. This is the same "false change" point from her Week 3 post.
- [ ] **Method + code snippet:** `cv2.addWeighted(before, 0.5, after, 0.5, 0)`. Each output pixel = half of each image. Things that didn't move look **sharp**; things that are shifted show **double edges / ghosting**. Mention the BGR→RGB conversion for matplotlib. Paste only the loop, not the whole notebook. Small fix before screenshotting: the cell's first comment still says `after_resized`, but the code now blends `after.png` (resizing was removed), so change it to `after`.
- [ ] **Results table (all 10 pairs).** Fill in after zooming in on each overlay in the notebook. What a quick look at the centre of each overlay shows:

  | Pair | Overlay result | Notes |
  |---|---|---|
  | 01 | Sharp | Rivers and roads line up; the red marker is doubled by only a pixel or two |
  | 03 | Sharp, but strip and label | Grey strip on the right and the "2018" year label (two dates printed on top of each other) come from the other half |
  | 04 | Slight ghosting | Road edges doubled, small horizontal shift |
  | 06 | Ghosting | Double edges around the warehouses, roughly 10 px vertical shift |
  | 09 | Labels overlap | Axis ticks and labels from the plot frame are doubled; the image area itself lines up roughly |
  | 10 | Clear ghosting | Street outlines are doubled; the most misaligned pair |
  | 02, 05, 07, 08 | Check by zooming | 07 is so textured that a 50/50 blend is hard to judge by eye |

- [ ] **Figure:** a screenshot of 2–3 overlays side by side: one sharp (01), one ghosted (06 or 10), one with labels or a strip (03 or 09). Crop and zoom in so the double edges are visible.
- [ ] **Limitations:**
  - It's a visual check, not a number. The overlay tells us *whether* a pair is misaligned, not *by how much*.
  - Heavily changed pairs (02, 07) are hard to judge, because the content itself is different.
  - Text/labels/scale bars in pairs 01, 03, 09, 10 will be counted in vegetation % unless they are cropped or masked.
- [ ] **Next week:**
  - Measure the shift instead of eyeballing it: phase correlation (`cv2.phaseCorrelate`) or ORB + homography (Nojus's Week 2 plan), then compare the overlay before and after alignment.
  - Run `excess_green()` on all 10 pairs (still open from her Week 3 next steps) on the aligned, brightness-matched images (Polina's Y matching).
  - Link to [Nojus's Week 4 post](https://c23391116.wordpress.com/2026/10/25/week4-image-processing-project19th-25th-october/): his RGB/HSV thresholds missed the brown autumn trees in pair 06, so he added an edge-density (texture) mask. This is the "dry or brown vegetation: not detected" limitation from her Week 3 table, so she can say ExG will have the same problem and compare against his texture method.
  - Hand-label a few small reference areas for testing (also from Week 3).
  - Agree the vegetation definition and detection method with the team (ExG vs GLI).
- [ ] **References (IEEE, numbered):** e.g. B. Zitová and J. Flusser, "Image registration methods: a survey," *Image and Vision Computing*, vol. 21, no. 11, pp. 977–1000, 2003, for why misregistration matters, plus J. R. G. Townshend *et al.*, "The impact of misregistration on change detection," *IEEE Trans. Geosci. Remote Sens.*, vol. 30, no. 5, pp. 1054–1060, 1992. Add one 2020+ paper on registration for change detection. Check all details against the actual papers before posting.

### Rubric boosts (see [rubric.md](rubric.md))

- [ ] **Blog: Content**: first post with screenshots of our own results.
- [ ] **Design: Testing**: say the check ran on all 10 pairs (forest, mining, urban, data centre).
- [ ] **Research: Comparisons**: compare visual overlay vs a measured shift (next week).
- [ ] **Blog: Progress**: explain the change from edge splitting → half cut, and the resizing correction, so Week 1 and the code tell the same story.

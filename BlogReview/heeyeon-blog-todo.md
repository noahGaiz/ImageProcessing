# Heeyeon: What to Add to Her Blog

Blog: https://d22127506.wordpress.com/

## Week 4 post (19 – 25 Oct): Checking alignment with a 50/50 overlay

✅ Posted 27 Oct: https://d22127506.wordpress.com/2026/10/27/image-processing-project-week4-19th-oct-25th-oct/ (checked 26 Oct). Small things to check in the post: pair 04's labels are "2010"/"2025" (a summary of the post read "2015"), and the WordPress template footer ("123 Example Street") is still there.

**Posted (26 Oct).** All items below are done. The image set changed to 8 images (`4c4e085`), so the post covers 8 pairs, not 10.

Weeks 2 and 3 were research (resizing, then "what counts as vegetation"). Her code this week is the **overlay check** cell in `VegetationChange.ipynb`, which blends `before` and `after` 50/50 for every pair. This post should show that code and what it found.

### Suggested title

"Image Processing Project: Week4 (19th Oct – 25th Oct)"

### Checklist (same layout as her Week 3 post: H2/H3 headings, bullets, one table, IEEE references)

- [x] **Recap (1–2 lines):** Week 2 looked at resizing, Week 3 defined vegetation and proposed `excess_green()`. Before we compare vegetation pixel by pixel, we need to know the two images actually line up.
- [x] **Team context (one line, link [Nojus's Week 3 post](https://c23391116.wordpress.com/2026/10/21/week3-image-processing-project12-18th-october/)):** in Week 3 Nojus first resized the pairs, found that it stretched the images, and then went back to cutting each image exactly in half (dropping the edge-based Gaussian/Sobel/Canny divider from our Week 1 posts). Both halves are now always the same size, so no resizing is needed. Her overlay check runs on these half-cut pairs.
  - Add one honest line correcting Week 1: "In Week 1 I wrote that we resized the images. Resizing was actually done later, by Nojus in Week 3, and then replaced by the half cut, which makes it unnecessary." (No need to edit the old post.)
  - Add one line on Week 2: her `match_size` research isn't used now, but it would be needed if we ever go back to splitting at the divider or add images from other sources.
- [x] **Why an overlay check:** if the two images are shifted even a few pixels, a road or roof edge in `before` lands on grass in `after`, and it shows up as fake vegetation change. This is the same "false change" point from her Week 3 post.
- [x] **Method + code snippet:** `cv2.addWeighted(before, 0.5, after, 0.5, 0)`. Each output pixel = half of each image. Things that didn't move look **sharp**; things that are shifted show **double edges / ghosting**. Mention the BGR→RGB conversion for matplotlib. Paste only the loop, not the whole notebook. (The old `after_resized` comment was fixed in `198c62e`.) Her new phase correlation cell (`198c62e`) can go in the same post: `cv2.phaseCorrelate` on greyscale halves with a Hanning window, giving dx, dy and a response.
- [x] **Image set changed (26 Oct): rerun before posting.** Forest.jpg, Image6.jpeg and NY.jpeg (old pairs 03, 09, 10) were dropped and image.jpg (2010 → 2025 farmland to housing) was added, so there are now **8 pairs** and the numbering shifted: old 04 (Image.jpeg) is now 03, and 04 is the new image. Any overlay notes or phase correlation numbers from before 26 Oct are for the old pairs. Add one line to the post saying the set changed and why (dropped pairs had big size differences and strips/labels after the half cut; confirm the reason with the team). Her Week 2 point that pairs 03, 09, 10 shouldn't be stretched is settled by dropping them.
- [x] **Results table (all 8 pairs).** ✅ Done in the post: checked by zooming into the full-size overlays and backed by phase correlation (only pair 06 clearly shifted, ~10 px vertical). The prep notes below are kept for reference; the post is the final version. The phase correlation numbers below come from her cell run on the new pairs (26 Oct). A low response (below about 0.15) means the scenes changed too much to trust the shift, so only 05 and 08 are reliable, and 06 agrees with the ghosting seen by eye. Open the overlay output, zoom along roads and building edges (one sharp line = aligned, two faint lines = shifted) and fill in the overlay column.

  | Pair | dx, dy (px) | Response | Overlay result | Notes |
  |---|---|---|---|---|
  | 01 | −4.1, −1.3 | 0.08 | Check | Red marker and date boxes are in both halves |
  | 02 | +6.3, −3.6 | 0.04 | Check | Heavily changed, hard to judge |
  | 03 | −14.6, −1.2 | 0.07 | Check | Was "slight ghosting, road edges doubled" when it was pair 04 |
  | 04 | −2.8, +1.7 | 0.05 | Check | New pair; "2010"/"2025" labels and EUSI logo |
  | 05 | −0.4, −2.1 | 0.47 | Check | Reliable: barely shifted |
  | 06 | +0.4, +9.8 | 0.11 | Ghosting | Double edges around the warehouses; measured ~10 px vertical shift matches |
  | 07 | −11.1, +54.6 | −0.00 | Check | No usable match; so textured and changed that a blend is hard to judge |
  | 08 | −2.2, −0.2 | 0.33 | Check | Reliable: small shift. Before/after may be swapped (houses on the left, fields on the right); check with the team |

- [x] **Figure:** a screenshot of 2–3 overlays side by side: one sharp (05 or 08), one ghosted (06), one with labels (04). Posted as 01 sharp, 06 double edges, 04 overlapping year labels.
- [x] **Limitations:**
  - The overlay is a visual check; phase correlation adds a number, but it is only trustworthy when the response is high (05, 08).
  - Heavily changed pairs (02, 07) are hard to judge, because the content itself is different.
  - Text/labels/scale bars in pairs 01, 02, 04, 05, 07 will be counted in vegetation % unless they are cropped or masked.
- [x] **Next week:**
  - Use the measured shift to actually align the pairs (shift by dx, dy where the response is high, or ORB + homography from Nojus's Week 2 plan for the rest), then compare the overlay before and after alignment.
  - Run `excess_green()` on all 8 pairs (still open from her Week 3 next steps) on the aligned, brightness-matched images (Polina's Y matching).
  - Link to [Nojus's Week 4 post](https://c23391116.wordpress.com/2026/10/25/week4-image-processing-project19th-25th-october/): his RGB/HSV thresholds missed the brown autumn trees in pair 06, so he added an edge-density (texture) mask. This is the "dry or brown vegetation: not detected" limitation from her Week 3 table, so she can say ExG will have the same problem and compare against his texture method.
  - Hand-label a few small reference areas for testing (also from Week 3).
  - Agree the vegetation definition and detection method with the team (ExG vs GLI).
- [x] **References (IEEE, numbered):** e.g. B. Zitová and J. Flusser, "Image registration methods: a survey," *Image and Vision Computing*, vol. 21, no. 11, pp. 977–1000, 2003, for why misregistration matters, plus J. R. G. Townshend *et al.*, "The impact of misregistration on change detection," *IEEE Trans. Geosci. Remote Sens.*, vol. 30, no. 5, pp. 1054–1060, 1992. Add one 2020+ paper on registration for change detection. Check all details against the actual papers before posting.

### Rubric boosts (see [rubric.md](rubric.md))

- [x] **Blog: Content**: first post with screenshots of our own results.
- [x] **Design: Testing**: say the check ran on all 8 pairs (forest loss, urban sprawl, data centre).
- [x] **Research: Comparisons**: compare visual overlay vs a measured shift. Done this week: phase correlation cell (`198c62e`) and numbers in the post.
- [x] **Blog: Progress**: explain the change from edge splitting → half cut, and the resizing correction, so Week 1 and the code tell the same story.

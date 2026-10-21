# Marking Rubric and Where We Stand

Rubric from *Course Intro 2026.pdf*. "Where we are" is based on the review on 21 Oct 2026 (blogs up to Week 3, code up to `e9ed553` plus the YUV matching cells). Update it as the project moves on.

## Rubric

| Criterion | Expectations Exceeded | Expectations Met | Expectations Not Met |
|---|---|---|---|
| Research: Publications | Up-to-date peer-reviewed publications | Some research in the area | Little research done |
| Research: Comparisons | Comparison with other designs | Awareness of existing designs | Other methods not investigated |
| Research: Theory | Explanation and application of theory | Some theory outlined | No theory outlined |
| Research: Citations | IEEE style citations | Some citations | No useful citations |
| Design: Specifications | Design fully meets all objectives | Design does something useful towards the main objective | Design does not meet specifications |
| Design: Testing | Tested on a variety of different inputs of the required type | Tested on an input of the required type | Design not sufficiently tested |
| Design: Complexity | Design reflects a technical complexity beyond module content | Design complexity is typical of module content | Design basic |
| Design: Innovation | Innovative compared to other approaches | Implementation of existing approach | Design is not original |
| Presentation: Knowledge | Comprehensive knowledge of the area demonstrated | Awareness of the area demonstrated | No knowledge of area demonstrated |
| Presentation: Content | Presentation is clear, engaging and entertaining | Presentation is clear | Presentation unclear |
| Presentation: Discussion | Significant contribution and insight in discussion | Ability to discuss concepts demonstrated | No participation in discussion |
| Blog: Content | Engaging blog with demonstrations of methods and ongoing research and results | Some blog records kept | Limited blog maintenance |
| Blog: Progress | Project is well organised and progresses from week to week | Some progress throughout | Poor organisation. Little progress. |

## Where we are and how to reach "Exceeded"

| Criterion | Where we are | To reach Exceeded |
|---|---|---|
| Publications | Polina and Heeyeon cite peer-reviewed papers (Otsu 1979, Reinhard 2001, Woebbecke 1995, Gitelson 2002, Townshend 1992, Zheng 2025). Nojus's Week 2 uses a Medium post and unnamed PDFs. | Add more **recent** (2020+) papers alongside the classics, e.g. on remote sensing change detection or RGB vegetation indices. Replace blog/Medium sources with papers. |
| Comparisons | Each post compares several methods in research. Code now compares two matching methods side by side. | Keep comparing **in code with numbers**: matching (histogram vs mean/std vs pseudo-invariant), detection (ExG vs GLI vs HSV), and compare our results against published approaches. |
| Theory | Good theory in Weeks 2–3 (YUV, CDFs, chromatic coordinates, NDVI vs RGB). | Each post should link the theory to **our** code and **our** images ("applied" not just "outlined"). |
| Citations | Mixed. Polina's Week 2 references [2]–[6] have placeholders; Nojus lists filenames. | **IEEE style everywhere**: numbered [1] in text, full reference list (authors, title, journal, vol, no, pages, year). Fix the placeholders. |
| Specifications | Splitting, overlay check and brightness matching done. No vegetation % or change map yet, so the main objective isn't met yet. | Finish Steps 3–4 of `Plan.txt`: vegetation mask, vegetation % before/after, change map (red lost, green gained). |
| Testing | Every step runs on all 10 pairs (forest, mining, urban sprawl, data centre). Accuracy not measured yet. | We already have **variety**. Add accuracy: hand-label 3–4 pairs (Plan Step 5) and report a score; test sensitivity to threshold/misalignment (Step 6). |
| Complexity | Typical of the module so far (splitting, resizing, histogram matching). | Automatic pseudo-invariant feature selection, ORB/SIFT + homography alignment, Otsu-based indices, texture for trees vs grass. |
| Innovation | Implementation of existing approaches. | Something of our own, e.g. using pixels that are **non-vegetation in both images** as the unchanged areas for brightness matching (links matching and detection), or comparing results by category (deforestation vs mining vs urban). |
| Presentation (all 3) | Not started. | Use the blog figures and results tables as slides; each of us presents our own part and can explain the theory and limitations. |
| Blog content | Week 1 describes code; Weeks 2–3 are research only, no figures of our results. | **Show demonstrations**: screenshots of our outputs, results tables, before/after figures, short code snippets in every post from Week 4 on. |
| Blog progress | Weekly posts from all three. Nojus's Week 3 had no work. Week 1 posts describe the edge splitter that has since been replaced. | Each post: recap last week → what I did → results → problems → next week. Explain changes of direction (e.g. half cut) so the story is consistent. |

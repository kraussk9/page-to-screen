# 🎞 Page to Screen
### An open-data proxy for literary scouting - sci-fi publishing vs. streaming commissioning trends.

## Author
Keagan Krauss

## Overview
Literary scouting - tracking which books are trending to predict what gets optioned for film and TV - is a real, growing function in the entertainment industry. This project builds an open-source proxy for that work: an end-to-end data analytics project comparing sci-fi publishing trends against streaming/film commissioning trends, using public Kaggle book datasets and the TMDb API instead of proprietary industry data. It compares thematic trends across both industries on a shared timeline to identify lag, gaps, and divergence between what's being written and what's being greenlit.

## Business Question
**Is streaming/film sci-fi commissioning tracking what's being published in sci-fi literature, or running on its own agenda?**

When a theme trends in books (e.g. climate collapse, AI anxiety), does the screen pick it up later, ignore it, or is there no relationship at all?

**Audience:** Streaming/studio content strategists deciding what sci-fi IP to option or greenlight next; also relevant to working and aspiring sci-fi authors curious how literary trends do or don't translate to screen.

## Real-World Precedent
This isn't a hypothetical exercise - it's a lightweight, open-data version of a function the entertainment industry already pays for.

- **Literary scouts are a real, formal role in the adaptation pipeline.** One scout described streamers as "optioning quite aggressively," and reported that the volume of scouting business has quadrupled since streaming platforms entered the market - driven largely by the sheer number of new books being published each year. [CNN / News Channel 3, Mar 2026]
- **Streamers explicitly use cross-platform trend data - not just bestseller lists - to decide what to option.** Book sales, social trends, and search interest all factor into acquisition decisions. [readers.life, Mar 2026]
- **Commercial platforms exist specifically to track this.** Services like Vitrina Business Network are built around helping industry professionals identify which books are trending and how to secure adaptation rights, including genre-specific and regional adaptation opportunities. [Vitrina, Nov 2024]
- **The industry frames this as a data problem.** Streaming platforms are described as providing data-driven insights that help studios select books with strong viewer engagement potential. [Vitrina, Nov 2024]

In other words: this project builds an open-source proxy for the trend-tracking work literary scouts and platforms like Vitrina already do commercially - using public datasets and a free API instead of proprietary sales and engagement data. It won't match the precision of a paid industry tool, but it demonstrates the same underlying logic a streaming acquisitions team or literary scout would actually use.

## Research Questions & Key Findings
- **Is overall sci-fi output volume rising, falling, or diverging over time?** Both publishing and commissioning show a shared long-term rise from the 1990s through the mid-2010s, peaking in the same general window before declining toward 2020.
- **When a theme spikes in publishing, is there a measurable lag before it spikes in commissioning?** Yes - quantified via cross-correlation for all 11 themes. Most themes (apocalyptic, dystopia, space_opera, cyberpunk, time_travel) show commissioning leading publishing by 1-3 years. Robots (which includes AI-related content, per the theme mapping) shows zero lag (the tightest correlation of any theme, r=0.83). Steampunk and aliens are the two themes where books lead. *(Caveat: a single best-fit lag can flatten a relationship that shifts character across eras - see Data Limitations.)*
- **Are there themes well-represented in books but underrepresented on screen, or vice versa?** Yes. Cyberpunk, alternate_history, alternate_universe, and steampunk are consistently books-ahead-of-screen; aliens, apocalyptic, and time_travel show commissioning historically leading or dominating.
- **How many commissioned projects are adaptations vs. original, and does that correlate with publishing themes?** Overall adaptation rate is 8.4% (344/4,105 titles). Dystopia has a reliably above-average rate (21.3%, n=394). Robots has the lowest rate (6.9%) despite being the most heavily and consistently commissioned theme - meaning high commissioning volume does not imply high adaptation rate. A formal volume-vs-adaptation-rate correlation across all themes was tested but found unreliable (see Data Limitations).
- **How do real-world events line up with shifts in themes?** Addressed narratively rather than as formal chart annotations (a stated stretch goal, not fully built out): robots/AI commissioning stays elevated through 2021-2025, plausibly tied to the ChatGPT-era AI boom, and this is corroborated by the recent-signal analysis showing robots as the strongest theme on both the publishing and commissioning sides in that window.

## Datasets
| Dataset | Source | Coverage | Used For |
|---|---|---|---|
| Sci-fi book publishing data | Kaggle — "Science Fiction Books (10,000+)" dataset, pre-split into 12 sub-genre files (dystopia, cyberpunk, space opera, time travel, etc.) | ~14,700 books after cleaning; publication years 1950-2020 (scoped to this window — see Data Limitations) | Publishing-side trend analysis (core, historical) |
| Recent publishing supplement | Manually compiled and manually theme-tagged Hugo Award, Nebula Award, and Arthur C. Clarke Award finalists (2021-2025), cross-referenced and deduplicated across all three award lists | ~125 unique titles, 2021-2025, winner/nominee status and award attribution tagged | Publishing-side trend analysis (recent years, closes the gap left by the core dataset's cutoff); also used for a dedicated recent-signal mini-analysis comparing award-recognized publishing against commissioning by theme |
| Sci-fi film & TV data | TMDb API (`/discover`, genre + keyword filters) | Film (genre 878) and TV (genre 10765, with Animation excluded to filter non-sci-fi anime/fantasy noise), filtered to `vote_count >= 50` as a proxy for real audience reach; 1950-2025 | Commissioning-side trend analysis |
| Theme tags (commissioning side) | Full per-title TMDb keyword pull (~4,105 calls), mapped to an 11-theme vocabulary matching the book sub-genres | 2,535 (title, theme) matches; ~55% of titles matched no theme (see Data Limitations) | Theme-level comparison against publishing |
| Adaptation flag | TMDb "based on novel or book" keyword | Subset of film/TV dataset (344 of 4,105 titles, 8.4%) | Secondary lens: adapted vs. original, by theme |

## Data Limitations
- **Publishing-side core data is a static Kaggle snapshot, not a live API pull** (switched from Open Library after repeated API outages during data collection). It's pre-categorized into 12 sub-genre files, a real advantage for theme-level analysis. Investigation of the data revealed the dataset is only reliably complete through **2020** — 2021 shows a sharp, artificial drop-off (27 books vs. 524 in 2019), indicating the scrape was cut off mid-year rather than reflecting a real decline in publishing. Analysis is scoped to 1950-2020 accordingly; books published before 1950 (a small number of genre-founding classics) were also excluded to align with the period where meaningful film/TV sci-fi data exists for comparison. **Each of the 12 sub-genre source files is roughly equal in size by construction (1209-1247 total books per theme across the full dataset) — this is an artifact of how the source dataset was scraped/split, not a reflection of real-world relative publishing volume by theme.** This means total-book-count-by-theme should not be read as "how popular this theme is in publishing" and is not reliable for cross-theme volume comparisons (see the adaptation-rate correlation note below).
- **The recent-years supplement (2021-2025) uses a different sampling method than the core dataset** — Hugo Award, Nebula Award, and Arthur C. Clarke Award finalists, manually compiled and manually theme-tagged, rather than a full publishing catalog. This measures award recognition, not raw publishing volume. In main-era theme charts, commissioning data is extended through 2025 as a dashed/visually distinct segment beyond the comparable 1950-2020 publishing window, rather than blending mismatched data as if directly comparable. Where a title was a finalist for more than one award, the earliest listed year was used (award ceremonies don't always align to the same eligibility year), and award attribution was combined rather than counted twice. Hugo and Nebula jointly cover science fiction and fantasy; the Arthur C. Clarke Award is sci-fi-specific, which was added specifically to strengthen the reliability of the recent-signal analysis.
- **A separate "recent signal" mini-analysis** (2021-2025, award-tagged publishing vs. full commissioning volume, by theme) uses aggregated totals across the whole 5-year window rather than year-by-year trends, given how sparse the award-tagged sample is per year. Themes with fewer than ~10 total tagged books in this window (military, alternate_universe, cyberpunk, alternate_history, steampunk) should be read directionally, not as confirmed trends.
- **The core dataset does not reliably distinguish novels from novellas** (Goodreads shelving doesn't enforce this distinction), so some shorter works are likely already present there. The award supplement explicitly includes Best Novella alongside Best Novel for the same reason — prioritizing genre-relevant published work over rigid format boundaries.
- **TMDb's Sci-Fi & Fantasy TV genre (10765) is broader and messier than the Science Fiction film genre (878)** - an initial pull was heavily polluted with non-sci-fi anime and fantasy content. This was addressed by excluding the Animation genre (16) from TV results, which removed most of the noise at the cost of also excluding legitimate sci-fi animation (e.g. Love, Death & Robots) as a side effect.
- **TMDb's Science Fiction / Sci-Fi & Fantasy genre tags are broader than the book dataset's sub-genre taxonomy** - they include superhero franchises (Marvel), kaiju/monster films, and supernatural horror, none of which have a corresponding book sub-genre in this project's scope. Roughly 55% of the vote-filtered commissioning dataset falls into this broader-genre-but-unmapped-theme category. Total-volume comparisons use the full dataset; theme-level comparisons are scoped to the ~45% of titles matching one of the 11 mapped content themes. "Hard" sci-fi (a narrative-style descriptor, not a content tag) has no TMDb keyword equivalent and is excluded from all commissioning-side theme comparisons.
- **The lag calculation (cross-correlation by theme, 1950-2020) reports a single best-fit lag per theme**, which can flatten a relationship that changes character across different eras. The clearest example: aliens' full-window result (+5 years, books leading) appears to contradict the theme's own chart, which shows commissioning leading for decades early on before books later caught up and surged past - the single-number method is dominated by the high-volume 2000s-2010s period and can't represent both regimes at once.
- **A formal correlation between total publishing volume and adaptation rate, across all 11 themes, was tested and found unreliable** - publishing volume by theme is nearly constant across the dataset (see the sub-genre file-size artifact noted above), so a correlation against a variable with almost no real variance is not a trustworthy result and is not reported as a finding. Theme-specific observations (e.g. robots: high commissioning volume, low adaptation rate) remain valid on their own.
- **Adaptation sample size**: books-to-screen adaptations are a minority of total sci-fi film/TV output (8.4% overall), so per-theme adaptation rates on small samples (e.g. steampunk, n=39; alternate_history, n=27) are flagged as suggestive rather than conclusive.
- **World-event annotations** (e.g. the 2022 AI/ChatGPT boom) were addressed narratively rather than built as formal chart annotations — a stated stretch goal that wasn't fully implemented given time constraints.
- **SQL was part of the original project plan but was intentionally not built** — the publishing/commissioning join was completed and validated in pandas, and adding a parallel SQL implementation wasn't necessary to reach a working, analysis-ready dataset given time constraints.

## Project Structure
```
page-to-screen/
├── 01_data/
│   ├── raw/                       <- raw source files
│   │   └── science_fiction_books/  <- 12 sub-genre Kaggle CSVs
│   └── processed/                  <- cleaned, merged, theme-tagged datasets
│                                      (includes the manually compiled
│                                       Hugo/Nebula/Clarke award finalist
│                                       data — see note below)
├── 02_notebooks/                   <- data collection, cleaning, EDA notebooks
├── 03_visualizations/              <- exported charts
├── 04_streamlit/                   <- Streamlit comparison dashboard
├── src/                            <- reusable Python functions (API pulls, cleaning, theme tagging)
├── requirements.txt
├── .gitignore
└── README.md
```
*Note: the Hugo/Nebula/Clarke award finalist data is manually compiled and tagged directly in the notebook (not sourced from downloadable files), then saved to `01_data/processed/`.*

## Pipeline
Data Collection → Cleaning & Theme Tagging → Comparative Analysis → Streamlit Dashboard

| Step | Notebook/Script | Tool | Description |
|---|---|---|---|
| Data Collection | `01_load_kaggle_books.ipynb`, `02_collect_tmdb.ipynb` | Python / pandas (Kaggle CSVs), requests (TMDb) | Load sci-fi books from Kaggle (12 sub-genre CSVs); manually compile and theme-tag Hugo/Nebula/Clarke finalists (2021-2025); pull sci-fi film/TV (TMDb) via API, including a full per-title keyword pull for theme tagging |
| Cleaning & Theme Tagging | `03_cleaning_wrangling.ipynb` | Python / pandas | Standardize schemas, build and apply an 11-theme keyword-to-genre mapping reconciling Kaggle sub-genre folders vs. TMDb keywords, flag adaptations |
| Comparative Analysis | `04_eda_comparison.ipynb` | Python / matplotlib | Total and per-theme volume trends (1950-2020, commissioning extended through 2025), a recent-signal mini-analysis (2021-2025 award publishing vs. commissioning), adaptation-rate-by-theme analysis, and a cross-correlation lag calculation per theme |
| Dashboard | `app.py` | Streamlit | Interactive theme-filterable comparison of publishing vs. commissioning trends over time |

## MVP
- Merged dataset: sci-fi book vs. film/TV volume by year, tagged by top-level theme — complete
- 3–4 comparative visualizations answering the core lag/gap questions — complete (all 11 themes, plus total-volume, recent-signal, adaptation-rate, and lag charts)
- Streamlit dashboard presenting the comparison — complete
- This README, including data limitations — complete

## Stretch Goals
Completed:
- Theme-level tagging beyond top-level genre, via an 11-theme keyword mapping (rather than full NLP), applied to both commissioning data and the recent award supplement
- Adapted-vs-original analysis, as a standalone adaptation-rate-by-theme comparison

Not included in this version (future work):
- Trend line/regression to project where commissioning is heading
- Formal world-event annotations layered onto the timeline charts (addressed narratively in the findings instead)

## How to Run
### Requirements
```
pip install -r requirements.txt
```

### Steps
```bash
# 1. Clone the repo
git clone https://github.com/[your-username]/page-to-screen.git
cd page-to-screen

# 2. Add API keys and download data
# TMDb requires a free API key — see https://www.themoviedb.org/settings/api
# Download the Kaggle "Science Fiction Books (10,000+)" dataset (12 CSVs)
# and place the files in 01_data/raw/science_fiction_books/
# The Hugo/Nebula/Clarke finalists dataset (2021-2025) is manually compiled
# and included in 01_data/processed/

# 3. Run notebooks in order (01 -> 04)
jupyter notebook

# 4. Launch the dashboard
streamlit run 04_streamlit/app.py
```

## References
- Kaggle - "Science Fiction Books (10,000+)" dataset - kaggle.com/datasets/tanguypledel/science-fiction-books-subgenres
- The Hugo Awards - thehugoawards.org
- The Nebula Awards - nebulas.sfwa.org
- The Arthur C. Clarke Award - clarkeaward.com
- The Movie Database (TMDb) API - developer.themoviedb.org

All analysis is for educational and portfolio purposes only.

# 🎞 Page to Screen
### An open-data proxy for literary scouting - sci-fi publishing vs. streaming commissioning trends.
 
## Author
Keagan Krauss
 
## Overview
Literary scouting — tracking which books are trending to predict what gets optioned for film and TV - is a real, growing function in the entertainment industry. This project builds an open-source proxy for that work: an end-to-end data analytics project comparing sci-fi publishing trends against streaming/film commissioning trends, using public Kaggle book datasets and the TMDb API instead of proprietary industry data. It compares thematic trends across both industries on a shared timeline to identify lag, gaps, and divergence between what's being written and what's being greenlit.
 
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
 
## Research Questions
- Is overall sci-fi output volume (books vs. film/TV) rising, falling, or diverging over time?
- When a theme spikes in publishing, is there a measurable lag before it spikes in streaming/film commissioning - and if so, how long?
- Are there themes well-represented in books that are underrepresented on screen, or vice versa?
- Of streaming/film sci-fi projects, how many are direct book adaptations vs. original - and does that correlate with which publishing themes made it to screen?
- Where relevant, how do major real-world events (e.g. the 2022 AI/ChatGPT boom) line up with shifts in either publishing or commissioning themes? *(annotation/context, not a formal causal claim)*
  
## Datasets
| Dataset | Source | Coverage | Used For |
|---|---|---|---|
| Sci-fi book publishing data | Kaggle — "Science Fiction Books (10,000+)" dataset, pre-split into 12 sub-genre files (dystopia, cyberpunk, space opera, hard sci-fi, etc.) | ~14,700 books after cleaning; publication years 1950-2020 (scoped to this window — see Data Limitations) | Publishing-side trend analysis (core, historical) |
| Recent publishing supplement | Manually compiled Hugo Award and Nebula Award Best Novel/Novella finalists (2021-2025), cross-referenced and deduplicated where a title appeared on both award lists | 100 titles, 2021-2025, winner/nominee status tagged | Publishing-side trend analysis (recent years, closes the gap left by the core dataset's cutoff) |
| Sci-fi film & TV data | TMDb API (`/discover`, genre + keyword filters) | Multi-decade, film (genre 878) and TV (genre 10765) | Commissioning-side trend analysis |
| Adaptation flag | TMDb "based on novel or book" keyword | Subset of film/TV dataset | Secondary lens: adapted vs. original |
 
## Data Limitations
- **Publishing-side core data is a static Kaggle snapshot, not a live API pull** (switched from Open Library after repeated API outages during data collection). It's pre-categorized into 12 sub-genre files, a real advantage for theme-level analysis. Investigation of the data revealed the dataset is only reliably complete through **2020** — 2021 shows a sharp, artificial drop-off (27 books vs. 524 in 2019), indicating the scrape was cut off mid-year rather than reflecting a real decline in publishing. Analysis is scoped to 1950-2020 accordingly; books published before 1950 (a small number of genre-founding classics) were also excluded to align with the period where meaningful film/TV sci-fi data exists for comparison.
- **The recent-years supplement (2021-2025) uses a different sampling method than the core dataset** — Hugo/Nebula Best Novel and Best Novella finalists, manually compiled, rather than a full publishing catalog. This measures award recognition, not raw publishing volume, and is flagged as a distinct measurement in charts rather than blended as if directly comparable. Where a title was a finalist for both awards, the earlier of the two award years was used (Hugo and Nebula ceremonies don't always align to the same eligibility year), and award attribution was combined rather than counted twice.
- **The core dataset does not reliably distinguish novels from novellas** (Goodreads shelving doesn't enforce this distinction), so some shorter works are likely already present there. The Hugo/Nebula supplement explicitly includes Best Novella alongside Best Novel for the same reason — prioritizing genre-relevant published work over rigid format boundaries.
- **TMDb TV genre tagging** is weaker than film genre tagging — TV results may be thinner than expected relative to film, which could skew the "commissioning" side toward film-heavy conclusions unless adjusted for.
- **Adaptation sample size**: books-to-screen adaptations are a minority of total sci-fi film/TV output, so the adapted-vs-original lens is treated as a secondary cut, not a standalone statistical claim.
- **World-event annotations** are added as narrative/visual context on relevant timelines, not as a modeled variable — no causal claim is being made about events driving thematic trends.
  

## Project Structure
```
page-to-screen/
├── 01_data/
│   ├── raw/                       <- raw source files
│   │   ├── science_fiction_books/  <- 12 sub-genre Kaggle CSVs
│   │   └── awards_finalists/       <- manually compiled Hugo/Nebula finalists CSV
│   └── processed/                  <- cleaned, merged, theme-tagged datasets
├── 02_notebooks/                   <- data collection, cleaning, EDA notebooks
├── 03_visualizations/              <- exported charts
├── 04_streamlit/                   <- Streamlit comparison dashboard
├── src/                            <- reusable Python functions (API pulls, cleaning, theme tagging)
├── requirements.txt
├── .gitignore
└── README.md
```
 
## Pipeline
Data Collection → Cleaning & Theme Tagging → EDA → Comparative Analysis → Streamlit Dashboard
 
| Step | Notebook/Script | Tool | Description |
|---|---|---|---|
| Data Collection | `01_load_kaggle_books.ipynb`, `02_collect_tmdb.ipynb` | Python / pandas (Kaggle CSVs), requests (TMDb) | Load sci-fi books from Kaggle (12 sub-genre CSVs), compile Hugo/Nebula finalists (2021-2025), and pull sci-fi film/TV (TMDb) via API |
| Cleaning & Theme Tagging | `03_cleaning_wrangling.ipynb` | Python / pandas | Standardize schemas, reconcile Kaggle sub-genre folders vs. TMDb genres/keywords into a shared theme taxonomy, flag adaptations |
| Database | — | SQL (SQLite) | Join publishing and commissioning tables by year and theme |
| EDA & Comparative Analysis | `04_eda_comparison.ipynb` | Python / matplotlib / seaborn | Volume trends, theme-level lag/gap analysis, adaptation-lens cut |
| Dashboard | `app.py` | Streamlit | Interactive theme-filterable comparison of publishing vs. commissioning trends over time |
 
## MVP
- Merged dataset: sci-fi book vs. film/TV volume by year, tagged by top-level theme
- 3–4 comparative visualizations answering the core lag/gap questions
- Streamlit dashboard presenting the comparison
- This README, including data limitations
  
## Stretch Goals
- NLP-derived sub-theme tagging beyond top-level genre
- Adapted-vs-original as a filterable dashboard lens
- Basic trend line/regression to project where commissioning is heading
- World-event annotations layered onto timeline visualizations
  
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
# The Hugo/Nebula finalists dataset (2021-2025) is manually compiled and
# included in 01_data/processed/hugo_nebula_finalists.csv
 
# 3. Run notebooks in order (01 -> 04)
jupyter notebook
 
# 4. Launch the dashboard
streamlit run 04_streamlit/app.py
```
 
## References
- Kaggle - "Science Fiction Books (10,000+)" dataset - kaggle.com/datasets/tanguypledel/science-fiction-books-subgenres
- The Hugo Awards - thehugoawards.org
- The Nebula Awards - nebulas.sfwa.org
- The Movie Database (TMDb) API - developer.themoviedb.org
  
All analysis is for educational and portfolio purposes only.

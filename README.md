# 🎞 Page to Screen
### An open-data proxy for literary scouting - sci-fi publishing vs. streaming commissioning trends.
 
## Author
Keagan Krauss
 
## Overview
Literary scouting - tracking which books are trending to predict what gets optioned for film and TV - is a real, growing function in the entertainment industry. This project builds an open-source proxy for that work: an end-to-end data analytics project comparing sci-fi publishing trends against streaming/film commissioning trends, using free public APIs (Open Library and TMDb) instead of proprietary industry data. It compares thematic trends across both industries on a shared timeline to identify lag, gaps, and divergence between what's being written and what's being greenlit.
 
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
In other words: this project builds an open-source proxy for the trend-tracking work literary scouts and platforms like Vitrina already do commercially - using free public APIs instead of proprietary sales and engagement data. It won't match the precision of a paid industry tool, but it demonstrates the same underlying logic a streaming acquisitions team or literary scout would actually use.
 
## Research Questions
- Is overall sci-fi output volume (books vs. film/TV) rising, falling, or diverging over time?
- When a theme spikes in publishing, is there a measurable lag before it spikes in streaming/film commissioning - and if so, how long?
- Are there themes well-represented in books that are underrepresented on screen, or vice versa?
- Of streaming/film sci-fi projects, how many are direct book adaptations vs. original - and does that correlate with which publishing themes made it to screen?
- Where relevant, how do major real-world events (e.g. the 2022 AI/ChatGPT boom) line up with shifts in either publishing or commissioning themes? *(annotation/context, not a formal causal claim)*
  
## Datasets
| Dataset | Source | Coverage | Used For |
|---|---|---|---|
| Sci-fi book publishing data | Kaggle — "Science Fiction Books (10,000+)" dataset, pre-split into 12 sub-genre files (dystopia, cyberpunk, space opera, hard sci-fi, etc.) | ~10,000 books, title/description/rating/genre level | Publishing-side trend analysis |
| Sci-fi film & TV data | TMDb API (`/discover`, genre + keyword filters) | Multi-decade, film (genre 878) and TV (genre 10765) | Commissioning-side trend analysis |
| Adaptation flag | TMDb "based on novel or book" keyword | Subset of film/TV dataset | Secondary lens: adapted vs. original |
 
## Data Limitations
- **Open Library subject tagging** is crowd-sourced and inconsistent below the top level — reliable for "is this sci-fi and when was it published," noisy for granular sub-themes (dystopia, first-contact, etc.). Sub-theme tagging will require an additional keyword/NLP pass rather than trusting raw subject tags.
- **TMDb TV genre tagging** is weaker than film genre tagging — TV results may be thinner than expected relative to film, which could skew the "commissioning" side toward film-heavy conclusions unless adjusted for.
- **Adaptation sample size**: books-to-screen adaptations are a minority of total sci-fi film/TV output, so the adapted-vs-original lens is treated as a secondary cut, not a standalone statistical claim.
- **World-event annotations** are added as narrative/visual context on relevant timelines, not as a modeled variable — no causal claim is being made about events driving thematic trends.
## Project Structure
```
page-to-screen/
├── 01_data/
│   ├── raw/            <- raw API pulls (Open Library, TMDb)
│   └── processed/       <- cleaned, merged, theme-tagged datasets
├── 02_notebooks/         <- data collection, cleaning, EDA notebooks
├── 03_visualizations/    <- exported charts
├── 04_streamlit/         <- Streamlit comparison dashboard
├── src/                  <- reusable Python functions (API pulls, cleaning, theme tagging)
├── requirements.txt
├── .gitignore
└── README.md
```
 
## Pipeline
Data Collection → Cleaning & Theme Tagging → EDA → Comparative Analysis → Streamlit Dashboard
 
| Step | Notebook/Script | Tool | Description |
|---|---|---|---|
| Data Collection | `01_collect_openlibrary.ipynb`, `02_collect_tmdb.ipynb` | Python / requests | Pull sci-fi books (Open Library) and film/TV (TMDb) via API |
| Cleaning & Theme Tagging | `03_cleaning_wrangling.ipynb` | Python / pandas | Standardize schemas, reconcile Open Library subjects vs. TMDb genres/keywords into a shared theme taxonomy, flag adaptations |
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
 
# 2. Add API keys
# TMDb requires a free API key — see https://www.themoviedb.org/settings/api
# Open Library requires no key
 
# 3. Run notebooks in order (01 -> 04)
jupyter notebook
 
# 4. Launch the dashboard
streamlit run 04_streamlit/app.py
```
 
## References
- Open Library API — openlibrary.org/developers/api
- The Movie Database (TMDb) API — developer.themoviedb.org
  
All analysis is for educational and portfolio purposes only.


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64

st.set_page_config(page_title="Page to Screen", layout="wide")

VOID_BLACK = "#06070A"
ELECTRIC_COBALT = "#3D5AFE"
SYNTH_MAGENTA = "#FF2FA3"
PHOSPHOR_GREEN = "#81EC86"
TITANIUM_FOG = "#AEB6C2"
HOLOGRAPHIC_PEARL = "#F5F7FF"
BOREAL_GREEN = "#09AB3B"

THEME_MAX_BOOKS = 174
THEME_MAX_TITLES = 21
TOTAL_MAX_BOOKS = 1187
TOTAL_MAX_TITLES = 104

def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

hero_img_b64 = get_base64_image("04_streamlit/blade-runner-1-867x362.jpg")

st.markdown('''
<style>
.block-container {
    padding-top: 3.5rem;
}
.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border: none !important;
    padding: 8px 14px;
    color: #F5F7FF;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #81EC86 !important;
}
.stTabs [aria-selected="true"] {
    background: transparent !important;
    color: #81EC86 !important;
    font-weight: bold;
    border: none !important;
}
.stTabs [data-baseweb="tab-highlight"] {
    background-color: #81EC86 !important;
}
[data-testid="stMetricDelta"] {
    color: #09AB3B !important;
}
[data-testid="stMetricDelta"] svg {
    fill: #09AB3B !important;
}
.hero-banner {
    border-radius: 14px;
    padding: 90px 40px;
    margin-bottom: 24px;
    text-align: center;
    background-size: cover;
    background-position: center;
}
.hero-title {
    font-family: 'Futura', 'Century Gothic', 'Trebuchet MS', sans-serif;
    font-size: 88px;
    font-weight: 900;
    color: #F5F7FF;
    letter-spacing: 3px;
    margin-bottom: 14px;
    text-shadow: 0 2px 16px rgba(0,0,0,0.95);
}
.hero-subtitle-line {
    font-size: 28px;
    font-weight: 600;
    color: #F5F7FF;
    line-height: 1.5;
    text-shadow: 0 2px 10px rgba(0,0,0,0.95);
}
.business-question-box {
    background: transparent;
    padding: 4px 0;
    margin: 24px 0;
}
.business-question-box .main-q {
    color: #81EC86;
    font-size: 19px;
    font-weight: 700;
    line-height: 1.5;
}
.business-question-box .sub-q {
    color: #F5F7FF;
    font-size: 19px;
    font-weight: 400;
    margin-top: 8px;
    line-height: 1.5;
}
.business-question-box .audience {
    color: #F5F7FF;
    font-size: 19px;
    font-weight: 400;
    margin-top: 12px;
    line-height: 1.5;
}
.key-finding-box {
    background: #0F1220;
    border: 1px solid #AEB6C2;
    border-radius: 10px;
    padding: 20px 24px;
    margin: 20px 0;
}
.key-finding-box .label {
    color: #81EC86;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.key-finding-box ul {
    margin-top: 10px;
    margin-bottom: 0;
}
.key-finding-box li {
    color: #F5F7FF;
    font-size: 15px;
    margin-bottom: 8px;
    line-height: 1.5;
}
.key-finding-box .finding-text {
    color: #F5F7FF;
    font-size: 15px;
    margin-top: 8px;
    line-height: 1.5;
}
.stat-box {
    background: transparent;
    border: 1px solid #AEB6C2;
    border-radius: 10px;
    padding: 18px;
    text-align: center;
}
.stat-number {
    font-size: 28px;
    font-weight: 800;
    color: #81EC86;
}
.stat-label {
    font-size: 13px;
    color: #AEB6C2;
}
.precedent-line {
    font-size: 14px;
    color: #AEB6C2;
    font-style: italic;
    margin-top: 20px;
}
.precedent-box {
    background: #0F1220;
    border-left: 3px solid #FF2FA3;
    border-radius: 8px;
    padding: 20px 24px;
}
.precedent-box h4 {
    color: #F5F7FF;
    margin-top: 0;
}
.precedent-box li {
    color: #F5F7FF;
    margin-bottom: 10px;
    line-height: 1.5;
}
.precedent-box .source {
    color: #AEB6C2;
    font-size: 12px;
}
.precedent-box .closer {
    color: #AEB6C2;
    font-style: italic;
    margin-top: 16px;
    line-height: 1.5;
}
</style>
''', unsafe_allow_html=True)

@st.cache_data
def load_data():
    publishing = pd.read_csv("01_data/processed/publishing_yearly_theme_counts.csv")
    commissioning = pd.read_csv("01_data/processed/commissioning_yearly_theme_counts.csv")
    return publishing, commissioning

@st.cache_data
def load_adaptation_data():
    by_theme = pd.read_csv("01_data/processed/adaptation_by_theme.csv")
    by_decade = pd.read_csv("01_data/processed/adaptation_by_decade.csv")
    return by_theme, by_decade

@st.cache_data
def load_market_share_data():
    share = pd.read_csv("01_data/processed/genre_market_share.csv", index_col=0)
    share = share.drop(columns=["decade"], errors="ignore")
    decade = pd.read_csv("01_data/processed/genre_decade_summary.csv", index_col=0)
    decade = decade.drop(columns=["decade"], errors="ignore")
    scope_df = pd.read_csv("01_data/processed/genre_scope_labels.csv")
    scope_labels = dict(zip(scope_df["genre"], scope_df["scope_label"]))
    return share, decade, scope_labels

@st.cache_data
def load_lag_data():
    return pd.read_csv("01_data/processed/lag_by_theme.csv")

publishing_yearly_theme_counts, yearly_commissioning_theme_counts = load_data()
adaptation_by_theme, adaptation_by_decade = load_adaptation_data()
genre_market_share, genre_decade_summary, scope_labels = load_market_share_data()
lag_by_theme = load_lag_data()

ALL_THEMES = sorted([t for t in publishing_yearly_theme_counts["theme"].unique().tolist() if t != "hard"])
TAB_LABELS = ["Total"] + [t.replace("_", " ").title() for t in ALL_THEMES]

genre_order = genre_market_share.mean().sort_values(ascending=False).index.tolist()
genre_colors = {
    "Science Fiction": ELECTRIC_COBALT,
    "Sci-Fi & Fantasy": SYNTH_MAGENTA,
    "Fantasy": "#B983FF",
    "Horror": "#FF6B4A",
}
tab20 = plt.get_cmap("tab20")
remaining_genres = [g for g in genre_order if g not in genre_colors]
for i, genre in enumerate(remaining_genres):
    base_color = tab20(i % 20)
    r, g, b, a = base_color
    genre_colors[genre] = (r + (1 - r) * 0.55, g + (1 - g) * 0.55, b + (1 - b) * 0.55, 1.0)

COMPARISON_GENRES = ["Science Fiction", "Sci-Fi & Fantasy", "Fantasy", "Horror", "Action"]

THEME_FINDINGS = {
    "Total": "Both series share a long-term rise from the 1990s through the mid-2010s, peaking in the same general window before declining toward 2020.",
    "aliens": "Commissioning shows real activity decades before books catch up - the clearest case of commissioning leading publishing for an extended stretch in the whole dataset.",
    "alternate_history": "Books climb steadily then surge sharply after 2005; commissioning stays thin and volatile throughout - one of the most extreme 'books-ahead-of-screen' themes alongside steampunk.",
    "alternate_universe": "Books far outpace commissioning for most of the timeline, but commissioning shows a late, sustained uptick right at the edge of the comparable window - plausibly tied to the industry's post-2018 multiverse trend.",
    "apocalyptic": "The strongest synchronized peak in the dataset - both series reach their highest raw volume together around 2013-2015, then decline in tandem.",
    "cyberpunk": "The clearest 'books far ahead of screen' theme - publishing accelerates sharply after 2010 while commissioning stays comparatively flat and thin throughout.",
    "dystopia": "A single dramatic spike defines this theme: books surge to their highest level around 2012-2013, aligning with the real-world YA dystopian publishing boom.",
    "military": "Two distinct eras: sharp, isolated commissioning spikes early on with no book-side counterpart, followed by a period of tight correlation similar to robots from the mid-2000s onward.",
    "robots": "The tightest correlation of any theme - both series climb together gradually from the 1970s onward, tracking each other closely for decades.",
    "space_opera": "An early commissioning spike around 1979 - likely tied to the post-Star Wars boom - precedes sustained book growth by years, one of the clearest examples of commissioning leading publishing.",
    "steampunk": "An extreme 'books-ahead' theme: commissioning barely registers (peaking at just 3 titles across 70+ years) while books surge to a striking peak around 2013.",
    "time_travel": "Commissioning builds steadily from the late 1970s while books stay flat for decades; both series later converge and peak close together around 2013-2014.",
}

def build_chart(theme_choice):
    if theme_choice == "Total":
        pub_raw = (
            publishing_yearly_theme_counts[publishing_yearly_theme_counts["Year_published"] <= 2020]
            .groupby("Year_published")["book_count"].sum()
        )
        comm_raw = yearly_commissioning_theme_counts.groupby("Year_released")["title_count"].sum()
        chart_title = "Total, 1950-2025"
        max_books = TOTAL_MAX_BOOKS
        max_titles = TOTAL_MAX_TITLES
    else:
        pub_raw = publishing_yearly_theme_counts[
            (publishing_yearly_theme_counts["theme"] == theme_choice)
            & (publishing_yearly_theme_counts["Year_published"] <= 2020)
        ].groupby("Year_published")["book_count"].sum()
        comm_raw = yearly_commissioning_theme_counts[
            yearly_commissioning_theme_counts["theme"] == theme_choice
        ].groupby("Year_released")["title_count"].sum()
        theme_label = theme_choice.replace("_", " ").title()
        chart_title = theme_label + ", 1950-2025"
        max_books = THEME_MAX_BOOKS
        max_titles = THEME_MAX_TITLES

    pub_scoped = pub_raw.reindex(range(1950, 2021), fill_value=0).reset_index()
    pub_scoped.columns = ["Year_published", "book_count"]

    comm_full = comm_raw.reindex(range(1950, 2026), fill_value=0).reset_index()
    comm_full.columns = ["Year_released", "title_count"]

    comm_comparable = comm_full[comm_full["Year_released"] <= 2020]
    comm_extended = comm_full[comm_full["Year_released"] >= 2020]

    fig, ax1 = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(VOID_BLACK)
    ax1.set_facecolor(VOID_BLACK)

    ax1.plot(pub_scoped["Year_published"], pub_scoped["book_count"],
              color=ELECTRIC_COBALT, label="Books Published", linewidth=2.2)
    ax1.set_xlabel("Year", color=HOLOGRAPHIC_PEARL)
    ax1.set_ylabel("Books Published", color=HOLOGRAPHIC_PEARL)
    ax1.set_ylim(0, max_books * 1.05)
    ax1.set_xlim(1950, 2025)
    ax1.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    ax1.tick_params(axis="x", labelcolor=HOLOGRAPHIC_PEARL)
    ax1.spines["bottom"].set_color(TITANIUM_FOG)
    ax1.spines["top"].set_color(VOID_BLACK)
    ax1.spines["left"].set_color(TITANIUM_FOG)
    ax1.spines["right"].set_color(VOID_BLACK)
    ax1.grid(True, alpha=0.15, color=TITANIUM_FOG)

    ax2 = ax1.twinx()
    ax2.plot(comm_comparable["Year_released"], comm_comparable["title_count"],
              color=SYNTH_MAGENTA, label="Films & TV Commissioned", linewidth=2.2)
    ax2.plot(comm_extended["Year_released"], comm_extended["title_count"],
              color=SYNTH_MAGENTA, linestyle="--", alpha=0.7, linewidth=2.2)
    ax2.set_ylabel("Films & TV Commissioned", color=HOLOGRAPHIC_PEARL)
    ax2.set_ylim(0, max_titles * 1.05)
    ax2.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    ax2.spines["right"].set_color(TITANIUM_FOG)
    ax2.spines["top"].set_color(VOID_BLACK)

    ax1.axvline(x=2020, color=TITANIUM_FOG, linestyle=":", alpha=0.6)
    ax1.text(2020.3, max_books * 1.0, "2020: publishing\ndata cutoff", fontsize=8, color=TITANIUM_FOG, va="top")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left",
                facecolor=VOID_BLACK, edgecolor=TITANIUM_FOG, labelcolor=HOLOGRAPHIC_PEARL)

    ax1.set_title("Sci-Fi Publishing vs. Commissioning Volume - " + chart_title, color=HOLOGRAPHIC_PEARL)
    fig.tight_layout()
    return fig, pub_scoped, comm_full

def build_recent_signal_data():
    pub_recent = publishing_yearly_theme_counts[publishing_yearly_theme_counts["Year_published"] >= 2021]
    pub_recent_totals = pub_recent.groupby("theme")["book_count"].sum()
    comm_recent = yearly_commissioning_theme_counts[yearly_commissioning_theme_counts["Year_released"] >= 2021]
    comm_recent_totals = comm_recent.groupby("theme")["title_count"].sum()
    recent_signal = pd.DataFrame({"book_count": pub_recent_totals, "title_count": comm_recent_totals}).fillna(0)
    recent_signal = recent_signal[recent_signal.index != "hard"]
    recent_signal = recent_signal.sort_values("title_count", ascending=False)
    return recent_signal

RECENT_SIGNAL_DF = build_recent_signal_data()

RECENT_FINDINGS = {
    "Total": "Across all themes, 2021-2025 award-recognized publishing (100 tagged titles across Hugo/Nebula/Clarke) is dwarfed by commissioning volume (341 tagged titles) - expected, since award finalists are a small, curated sample, not a full publishing catalog.",
    "robots": "Robots leads both sides (17 books, 60 titles) - the strongest cross-industry signal in this window, directly confirming the AI-anxiety trend seen across the whole 75-year analysis.",
    "aliens": "Aliens shows a steep imbalance (8 books, 58 titles) - continuing the same commissioning-led pattern seen throughout the full 1950-2020 era.",
    "time_travel": "Time travel is the most commissioning-skewed theme in this window (3 books, 57 titles) - echoing its historical pattern of commissioning leading publishing.",
    "apocalyptic": "Apocalyptic stays active on both sides (14 books, 48 titles), consistent with the strong post-2020 commissioning rebound seen in the main-era chart.",
    "dystopia": "Dystopia nearly doubled its award-tagged book count after adding the Clarke Award (19 books, 40 titles) - Clarke's sci-fi-specific shortlists lean more toward social-critique/dystopian work.",
    "space_opera": "Space opera has the highest publishing count of any theme in this window (27 books) and the narrowest gap to commissioning (39 titles) of any major theme.",
    "military": "Military shows modest activity on both sides (3 books, 14 titles) - too small a sample for confident trend claims.",
    "alternate_universe": "Alternate universe stays thin on both sides (5 books, 10 titles) - consistent with its niche status across the full dataset.",
    "cyberpunk": "Cyberpunk gained its first real signal in this window (1 book, 9 titles), via Extremophile's biopunk classification - still thin, but no longer completely absent.",
    "alternate_history": "Alternate history remains the smallest theme in this window (3 books, 5 titles) - read directionally only.",
    "steampunk": "Steampunk shows almost no activity in this window (0 books, 1 title) - consistent with its persistently thin commissioning presence across the whole 70-year dataset.",
}

def build_recent_chart(highlight_theme):
    x = np.arange(len(RECENT_SIGNAL_DF))
    width = 0.35
    theme_list = list(RECENT_SIGNAL_DF.index)
    highlight_idx = theme_list.index(highlight_theme) if (highlight_theme is not None and highlight_theme in theme_list) else None

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(VOID_BLACK)
    ax.set_facecolor(VOID_BLACK)

    ax.bar(x - width/2, RECENT_SIGNAL_DF["book_count"], width, color=ELECTRIC_COBALT, label="Books Published", zorder=2)
    ax.bar(x + width/2, RECENT_SIGNAL_DF["title_count"], width, color=SYNTH_MAGENTA, label="Films & TV Commissioned", zorder=2)

    for i in range(len(RECENT_SIGNAL_DF)):
        b = RECENT_SIGNAL_DF["book_count"].iloc[i]
        t = RECENT_SIGNAL_DF["title_count"].iloc[i]
        is_highlight = (i == highlight_idx)
        label_color = PHOSPHOR_GREEN if is_highlight else HOLOGRAPHIC_PEARL
        label_weight = "bold" if is_highlight else "normal"
        ax.text(x[i] - width/2, b + 1, str(int(b)), ha="center", fontsize=8, color=label_color, fontweight=label_weight, zorder=3)
        ax.text(x[i] + width/2, t + 1, str(int(t)), ha="center", fontsize=8, color=label_color, fontweight=label_weight, zorder=3)

    ax.set_xticks(x)
    xtick_labels = ax.set_xticklabels([str(t).replace("_", " ").title() for t in RECENT_SIGNAL_DF.index], rotation=45, ha="right")
    for i, lbl in enumerate(xtick_labels):
        if i == highlight_idx:
            lbl.set_color(PHOSPHOR_GREEN)
            lbl.set_fontweight("bold")
        else:
            lbl.set_color(HOLOGRAPHIC_PEARL)

    ax.set_ylabel("Count, 2021-2025", color=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    ax.spines["bottom"].set_color(TITANIUM_FOG)
    ax.spines["top"].set_color(VOID_BLACK)
    ax.spines["left"].set_color(TITANIUM_FOG)
    ax.spines["right"].set_color(VOID_BLACK)
    ax.grid(True, alpha=0.15, color=TITANIUM_FOG, axis="y")

    lines, labels = ax.get_legend_handles_labels()
    ax.legend(lines, labels, loc="upper right",
               facecolor=VOID_BLACK, edgecolor=TITANIUM_FOG, labelcolor=HOLOGRAPHIC_PEARL)

    ax.set_title("Recent Signal, 2021-2025 - Award Publishing vs. Commissioning", color=HOLOGRAPHIC_PEARL)
    fig.tight_layout()
    return fig

def build_adaptation_theme_chart():
    df = adaptation_by_theme.sort_values("adaptation_rate", ascending=False).reset_index(drop=True)
    overall_rate = adaptation_by_theme["adapted_count"].sum() / adaptation_by_theme["total_count"].sum() * 100

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(VOID_BLACK)
    ax.set_facecolor(VOID_BLACK)

    labels = [str(t).replace("_", " ").title() for t in df["theme"]]
    bars = ax.bar(labels, df["adaptation_rate"] * 100, color=ELECTRIC_COBALT)

    ax.axhline(y=overall_rate, color=TITANIUM_FOG, linestyle="--", alpha=0.6)
    ax.text(len(df) - 1, overall_rate + 1, "Overall average: " + str(round(overall_rate, 1)) + "%",
             ha="right", fontsize=9, color=TITANIUM_FOG)

    for bar, n in zip(bars, df["total_count"]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.6, "n=" + str(int(n)),
                 ha="center", fontsize=8, color=HOLOGRAPHIC_PEARL)

    ax.set_xlabel("Theme", color=HOLOGRAPHIC_PEARL)
    ax.set_ylabel("Adaptation Rate (%)", color=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="x", labelcolor=HOLOGRAPHIC_PEARL, rotation=45)
    ax.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    plt.setp(ax.get_xticklabels(), ha="right")
    ax.spines["bottom"].set_color(TITANIUM_FOG)
    ax.spines["top"].set_color(VOID_BLACK)
    ax.spines["left"].set_color(TITANIUM_FOG)
    ax.spines["right"].set_color(VOID_BLACK)
    ax.grid(True, alpha=0.15, color=TITANIUM_FOG, axis="y")

    ax.set_title('Book-to-Screen Adaptation Rate by Theme\n(% of commissioned titles tagged "based on novel or book")', color=HOLOGRAPHIC_PEARL)
    fig.tight_layout()
    return fig

def build_adaptation_decade_chart():
    df = adaptation_by_decade.copy()
    overall_rate = adaptation_by_theme["adapted_count"].sum() / adaptation_by_theme["total_count"].sum() * 100

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(VOID_BLACK)
    ax.set_facecolor(VOID_BLACK)

    labels = [str(int(d)) + "s" for d in df["decade"]]
    bars = ax.bar(labels, df["adaptation_rate"] * 100, color=SYNTH_MAGENTA)

    ax.axhline(y=overall_rate, color=TITANIUM_FOG, linestyle="--", alpha=0.6)
    ax.text(len(df) - 1, overall_rate + 0.5, "Overall average: " + str(round(overall_rate, 1)) + "%",
             ha="right", fontsize=9, color=TITANIUM_FOG)

    for bar, n in zip(bars, df["total_titles"]):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, "n=" + str(int(n)),
                 ha="center", fontsize=8, color=HOLOGRAPHIC_PEARL)

    ax.set_xlabel("Decade", color=HOLOGRAPHIC_PEARL)
    ax.set_ylabel("Adaptation Rate (%)", color=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="x", labelcolor=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    ax.spines["bottom"].set_color(TITANIUM_FOG)
    ax.spines["top"].set_color(VOID_BLACK)
    ax.spines["left"].set_color(TITANIUM_FOG)
    ax.spines["right"].set_color(VOID_BLACK)
    ax.grid(True, alpha=0.15, color=TITANIUM_FOG, axis="y")

    ax.set_title("Book-to-Screen Adaptation Rate Over Time, by Decade", color=HOLOGRAPHIC_PEARL)
    fig.tight_layout()
    return fig

def build_stacked_chart():
    fig, ax = plt.subplots(figsize=(13, 7))
    fig.patch.set_facecolor(VOID_BLACK)
    ax.set_facecolor(VOID_BLACK)

    ax.stackplot(
        genre_market_share.index,
        [genre_market_share[g] for g in genre_order],
        labels=[scope_labels.get(g, g) for g in genre_order],
        colors=[genre_colors[g] for g in genre_order]
    )

    ax.set_xlabel("Year", color=HOLOGRAPHIC_PEARL)
    ax.set_ylabel("% Share of Total Commissioning Volume", color=HOLOGRAPHIC_PEARL)
    ax.set_ylim(0, 100)
    ax.tick_params(axis="x", labelcolor=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    ax.spines["bottom"].set_color(TITANIUM_FOG)
    ax.spines["top"].set_color(VOID_BLACK)
    ax.spines["left"].set_color(TITANIUM_FOG)
    ax.spines["right"].set_color(VOID_BLACK)

    ax.set_title("Full Genre Composition of Total Commissioning, 1950-2025", color=HOLOGRAPHIC_PEARL)
    legend = ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=8,
                         facecolor=VOID_BLACK, edgecolor=TITANIUM_FOG, labelcolor=HOLOGRAPHIC_PEARL)
    fig.tight_layout()
    return fig

def build_comparison_line_chart():
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(VOID_BLACK)
    ax.set_facecolor(VOID_BLACK)

    for genre in COMPARISON_GENRES:
        lw = 2.5 if genre in ["Science Fiction", "Sci-Fi & Fantasy"] else 2
        ax.plot(genre_market_share.index, genre_market_share[genre], label=scope_labels.get(genre, genre),
                 linewidth=lw, color=genre_colors[genre])

    ax.set_xlabel("Year", color=HOLOGRAPHIC_PEARL)
    ax.set_ylabel("% Share of Total Commissioning Volume", color=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="x", labelcolor=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    ax.spines["bottom"].set_color(TITANIUM_FOG)
    ax.spines["top"].set_color(VOID_BLACK)
    ax.spines["left"].set_color(TITANIUM_FOG)
    ax.spines["right"].set_color(VOID_BLACK)
    ax.grid(True, alpha=0.15, color=TITANIUM_FOG)

    ax.legend(facecolor=VOID_BLACK, edgecolor=TITANIUM_FOG, labelcolor=HOLOGRAPHIC_PEARL)
    ax.set_title("Science Fiction Share vs. Genre-Adjacent Comparisons, 1950-2025", color=HOLOGRAPHIC_PEARL)
    fig.tight_layout()
    return fig

def build_decade_comparison_chart():
    decades = genre_decade_summary.index.tolist()
    x = np.arange(len(decades))
    width = 0.15

    fig, ax = plt.subplots(figsize=(13, 7))
    fig.patch.set_facecolor(VOID_BLACK)
    ax.set_facecolor(VOID_BLACK)

    for i, genre in enumerate(COMPARISON_GENRES):
        offset = (i - len(COMPARISON_GENRES) / 2) * width + width / 2
        ax.bar(x + offset, genre_decade_summary[genre], width, label=scope_labels.get(genre, genre), color=genre_colors[genre])

    ax.set_xlabel("Decade", color=HOLOGRAPHIC_PEARL)
    ax.set_ylabel("Average % Share of Total Commissioning Volume", color=HOLOGRAPHIC_PEARL)
    ax.set_xticks(x)
    ax.set_xticklabels([str(int(d)) + "s" for d in decades], color=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    ax.spines["bottom"].set_color(TITANIUM_FOG)
    ax.spines["top"].set_color(VOID_BLACK)
    ax.spines["left"].set_color(TITANIUM_FOG)
    ax.spines["right"].set_color(VOID_BLACK)
    ax.grid(True, alpha=0.15, color=TITANIUM_FOG, axis="y")

    ax.legend(facecolor=VOID_BLACK, edgecolor=TITANIUM_FOG, labelcolor=HOLOGRAPHIC_PEARL)
    ax.set_title("Sci-Fi vs. Genre-Adjacent Comparisons - Average Share by Decade", color=HOLOGRAPHIC_PEARL)
    fig.tight_layout()
    return fig

def build_lag_chart():
    df = lag_by_theme.dropna(subset=["best_lag_years"]).sort_values("best_lag_years")
    labels = [str(t).replace("_", " ").title() for t in df["theme"]]
    colors_list = [ELECTRIC_COBALT if v > 0 else (SYNTH_MAGENTA if v < 0 else PHOSPHOR_GREEN) for v in df["best_lag_years"]]

    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(VOID_BLACK)
    ax.set_facecolor(VOID_BLACK)

    bars = ax.barh(labels, df["best_lag_years"], color=colors_list)

    for bar, corr in zip(bars, df["correlation"]):
        x_pos = bar.get_width()
        ha = "left" if x_pos >= 0 else "right"
        offset = 0.2 if x_pos >= 0 else -0.2
        ax.text(x_pos + offset, bar.get_y() + bar.get_height()/2, "r=" + str(round(corr, 2)),
                 va="center", ha=ha, fontsize=8, color=HOLOGRAPHIC_PEARL)

    ax.axvline(x=0, color=TITANIUM_FOG, linewidth=0.8)
    ax.set_xlabel("Best-Fit Lag (years)\n<- Commissioning leads          Commissioning trails ->", color=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="x", labelcolor=HOLOGRAPHIC_PEARL)
    ax.tick_params(axis="y", labelcolor=HOLOGRAPHIC_PEARL)
    ax.spines["bottom"].set_color(TITANIUM_FOG)
    ax.spines["top"].set_color(VOID_BLACK)
    ax.spines["left"].set_color(TITANIUM_FOG)
    ax.spines["right"].set_color(VOID_BLACK)

    ax.set_title("Publishing vs. Commissioning: Best-Fit Lag by Theme\n(1950-2020, cross-correlation; r = correlation strength)", color=HOLOGRAPHIC_PEARL)
    fig.tight_layout()
    return fig

st.sidebar.header("Navigate")
view = st.sidebar.radio(
    "Choose a view",
    ["Welcome", "Theme Comparison", "Recent Signal", "Adaptation Rate", "Market Share", "Lag Analysis"]
)

if view == "Welcome":
    hero_style = (
        "background-image: linear-gradient(rgba(6,7,10,0.3), rgba(6,7,10,0.4)), "
        "url('data:image/jpeg;base64," + hero_img_b64 + "');"
    )
    st.markdown(
        '<div class="hero-banner" style="' + hero_style + '">'
        '<div class="hero-title">PAGE TO SCREEN</div>'
        '<div class="hero-subtitle-line">An open-data proxy for literary scouting:</div>'
        '<div class="hero-subtitle-line">Sci-fi publishing vs. streaming commissioning trends</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="business-question-box">'
        '<div class="main-q">Is streaming/film sci-fi commissioning tracking what\'s being published in sci-fi literature, or running on its own agenda?</div>'
        '<div class="sub-q">When a theme trends in books (e.g. climate collapse, AI anxiety), does the screen pick it up later, ignore it, or is there no relationship at all?</div>'
        '<div class="audience">For streaming/studio content strategists deciding what sci-fi IP to option or greenlight next - and for working and aspiring sci-fi authors curious how literary trends do or don\'t translate to screen.</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="key-finding-box">'
        '<div class="label">Key Findings</div>'
        '<ul>'
        '<li><b>Robots/AI</b> is the only theme where publishing and commissioning move in perfect sync - zero lag, the strongest correlation of any theme (r=0.83) - and it stays the strongest theme on both sides even in the most recent (2021-2025) data.</li>'
        '<li>Most themes show commissioning <b>leading</b> publishing by 1-3 years; only steampunk and aliens show books leading.</li>'
        '<li><b>Cyberpunk, alternate history, alternate universe, and steampunk</b> are consistently under-adapted to screen relative to their book presence.</li>'
        '<li>Sci-fi\'s growth has shifted from film to TV - <b>TV overtook film\'s market share for the first time in the 2020s.</b></li>'
        '<li>High commissioning volume doesn\'t guarantee high adaptation: <b>dystopia adapts most often (21.3%), robots least (6.9%)</b> despite being the most-commissioned theme.</li>'
        '</ul>'
        '</div>',
        unsafe_allow_html=True
    )

    scol1, scol2, scol3, scol4 = st.columns(4)
    with scol1:
        st.markdown('<div class="stat-box"><div class="stat-number">14,700+</div><div class="stat-label">Sci-Fi Books Analyzed</div></div>', unsafe_allow_html=True)
    with scol2:
        st.markdown('<div class="stat-box"><div class="stat-number">4,100+</div><div class="stat-label">Films & TV Titles Tracked</div></div>', unsafe_allow_html=True)
    with scol3:
        st.markdown('<div class="stat-box"><div class="stat-number">75</div><div class="stat-label">Years of Trend Data</div></div>', unsafe_allow_html=True)
    with scol4:
        st.markdown('<div class="stat-box"><div class="stat-number">11</div><div class="stat-label">Sci-Fi Sub-Genres Compared</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="precedent-line">Modeled on literary scouting - the real, quadrupling industry function of tracking which books are worth optioning for screen.</div>', unsafe_allow_html=True)

    st.markdown("")
    st.markdown(
        "**Explore the analysis using the sidebar** - Theme Comparison, Recent Signal, "
        "Adaptation Rate, Market Share, and Lag Analysis."
    )

    exp_col1, exp_col2 = st.columns(2)
    with exp_col1:
        with st.expander("Why This Exists"):
            st.markdown('''
            <div class="precedent-box">
                <p style="color:#F5F7FF;">This is a lightweight, open-data version of a function the entertainment industry already pays for.</p>
                <ul>
                    <li><b>Literary scouts are a real, formal role in the adaptation pipeline.</b> One scout described streamers as "optioning quite aggressively," and reported that the volume of scouting business has quadrupled since streaming platforms entered the market - driven largely by the sheer number of new books being published each year. <span class="source">[CNN / News Channel 3, Mar 2026]</span></li>
                    <li><b>Streamers explicitly use cross-platform trend data - not just bestseller lists - to decide what to option.</b> Book sales, social trends, and search interest all factor into acquisition decisions. <span class="source">[readers.life, Mar 2026]</span></li>
                    <li><b>Commercial platforms exist specifically to track this.</b> Services like Vitrina Business Network are built around helping industry professionals identify which books are trending and how to secure adaptation rights, including genre-specific and regional adaptation opportunities. <span class="source">[Vitrina, Nov 2024]</span></li>
                    <li><b>The industry frames this as a data problem.</b> Streaming platforms are described as providing data-driven insights that help studios select books with strong viewer engagement potential. <span class="source">[Vitrina, Nov 2024]</span></li>
                </ul>
                <p class="closer">This project builds an open-source proxy for the trend-tracking work literary scouts and platforms like Vitrina already do commercially - using public datasets and a free API instead of proprietary sales and engagement data. It won't match the precision of a paid industry tool, but it demonstrates the same underlying logic a streaming acquisitions team or literary scout would actually use.</p>
            </div>
            ''', unsafe_allow_html=True)
    with exp_col2:
        with st.expander("About This Data & Methodology"):
            st.markdown(
                "- **Publishing data (1950-2020)**: a Kaggle sci-fi sub-genre dataset (~14,700 books), "
                "supplemented for 2021-2025 with manually theme-tagged Hugo, Nebula, and Arthur C. Clarke "
                "Award finalists (~125 titles) - a different sampling method than the core dataset, so "
                "recent years are flagged separately rather than blended in as directly comparable.\n"
                "- **Commissioning data (1950-2025)**: pulled live from the TMDb API (film + TV), filtered "
                "to titles with at least 50 ratings as a proxy for real audience reach, theme-tagged via "
                "a full per-title keyword pull mapped to 11 sci-fi sub-genres.\n"
                "- **Known limitations**: TMDb's Sci-Fi & Fantasy TV genre is broader than film's Science "
                "Fiction genre; roughly 55% of commissioned sci-fi titles don't match one of the 11 "
                "content themes (e.g. superhero or kaiju content sharing the same broad genre tag); "
                "cross-theme volume comparisons on the publishing side are affected by the source "
                "dataset's near-equal file sizes.\n"
                "\nFull methodology and data limitations are documented in the project README."
            )

elif view == "Theme Comparison":
    st.title("Page to Screen")
    st.header("Theme Comparison")
    st.markdown(
        "Compare sci-fi book publishing volume against streaming/film commissioning "
        "volume, by theme. Books are scoped to 1950-2020; commissioning is extended "
        "through 2025 (dashed beyond 2020) since commissioning data has no equivalent "
        "coverage gap. The dotted line marks where comparable publishing data ends. "
        "The theme tabs below share the same axis scale so relative theme size is "
        "directly comparable; Total uses its own larger scale since it sums across "
        "all themes."
    )

    tabs = st.tabs(TAB_LABELS)
    theme_keys = ["Total"] + ALL_THEMES

    for tab, theme_key in zip(tabs, theme_keys):
        with tab:
            fig, pub_scoped, comm_full = build_chart(theme_key)
            st.pyplot(fig)

            col1, col2 = st.columns(2)
            with col1:
                if not pub_scoped.empty:
                    peak_pub_year = int(pub_scoped.loc[pub_scoped["book_count"].idxmax(), "Year_published"])
                    peak_pub_count = int(pub_scoped["book_count"].max())
                    st.metric("Peak Publishing Year", str(peak_pub_year), str(peak_pub_count) + " books")
            with col2:
                if not comm_full.empty:
                    peak_comm_year = int(comm_full.loc[comm_full["title_count"].idxmax(), "Year_released"])
                    peak_comm_count = int(comm_full["title_count"].max())
                    st.metric("Peak Commissioning Year", str(peak_comm_year), str(peak_comm_count) + " titles")

            theme_finding = THEME_FINDINGS.get(theme_key, "No specific finding available for this theme.")
            st.markdown(
                '<div class="key-finding-box"><div class="label">Key Finding</div>'
                '<div class="finding-text">' + theme_finding + '</div></div>',
                unsafe_allow_html=True
            )

elif view == "Recent Signal":
    st.title("Page to Screen")
    st.header("Recent Signal")
    st.markdown(
        "How does 2021-2025 award-recognized publishing (Hugo, Nebula, and Arthur C. Clarke "
        "Award finalists) compare to recent commissioning, by theme? This is a smaller, "
        "curated sample - not a continuation of the main 1950-2020 trend - so it's shown "
        "separately rather than blended into the Theme Comparison charts. The number above "
        "each bar is its sample size (n); themes with very small counts should be read "
        "directionally, not as confirmed trends."
    )

    tabs = st.tabs(TAB_LABELS)
    theme_keys = ["Total"] + ALL_THEMES

    for tab, theme_key in zip(tabs, theme_keys):
        with tab:
            highlight = None if theme_key == "Total" else theme_key
            fig = build_recent_chart(highlight)
            st.pyplot(fig)

            if theme_key == "Total":
                total_books = int(RECENT_SIGNAL_DF["book_count"].sum())
                total_titles = int(RECENT_SIGNAL_DF["title_count"].sum())
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Books (Award-Tagged)", str(total_books))
                with col2:
                    st.metric("Total Films & TV Commissioned", str(total_titles))
            else:
                theme_books = int(RECENT_SIGNAL_DF.loc[theme_key, "book_count"]) if theme_key in RECENT_SIGNAL_DF.index else 0
                theme_titles = int(RECENT_SIGNAL_DF.loc[theme_key, "title_count"]) if theme_key in RECENT_SIGNAL_DF.index else 0
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Books (Award-Tagged)", str(theme_books))
                with col2:
                    st.metric("Films & TV Commissioned", str(theme_titles))

            finding_text = RECENT_FINDINGS.get(theme_key, "No specific finding available for this theme.")
            st.markdown(
                '<div class="key-finding-box"><div class="label">Key Finding</div>'
                '<div class="finding-text">' + finding_text + '</div></div>',
                unsafe_allow_html=True
            )

elif view == "Adaptation Rate":
    st.title("Page to Screen")
    st.header("Adaptation Rate")
    st.markdown(
        "How often is commissioned sci-fi a direct book adaptation, versus original "
        "screenplay? Measured via TMDb's \"based on novel or book\" keyword tag, "
        "across all 4,105 commissioned titles."
    )

    st.subheader("By Theme")
    st.pyplot(build_adaptation_theme_chart())
    st.markdown(
        '<div class="key-finding-box"><div class="label">Key Finding</div>'
        '<div class="finding-text">Dystopia has the strongest reliable above-average adaptation rate (21.3%, n=394) - '
        'more than double the overall baseline. Robots has the LOWEST adaptation rate (6.9%, n=404) despite being the '
        'most heavily and consistently commissioned theme - meaning high commissioning volume does not imply high '
        'adaptation. Steampunk shows the highest raw rate (30.8%) but on a small sample (n=39) and should be read '
        'cautiously.</div></div>',
        unsafe_allow_html=True
    )

    st.subheader("By Decade")
    st.pyplot(build_adaptation_decade_chart())
    st.markdown(
        '<div class="key-finding-box"><div class="label">Key Finding</div>'
        '<div class="finding-text">The 1970s stands out sharply at 20.0% (n=175), more than double every other decade. '
        'After a low point in the 1980s (4.9%), adaptation rate climbs gradually to 10.7% in the 2020s - the '
        'second-highest decade on record - consistent with industry claims that literary scouting activity has '
        'quadrupled since streaming platforms entered the market.</div></div>',
        unsafe_allow_html=True
    )

elif view == "Market Share":
    st.title("Page to Screen")
    st.header("Market Share")
    st.markdown(
        "Where does sci-fi fit in the broader film/TV landscape, not just against sci-fi "
        "publishing? This section pulls total commissioning volume across ALL TMDb "
        "genres to place sci-fi's share of the market in context. Legend entries note "
        "each genre's Film / TV / Film+TV scope, since TMDb's genre taxonomy isn't "
        "consistent between media."
    )

    st.subheader("Full Genre Composition")
    st.pyplot(build_stacked_chart())
    st.markdown(
        '<div class="key-finding-box"><div class="label">Key Finding</div>'
        '<div class="finding-text">Drama and Comedy consistently dominate, together accounting for a third to 40% '
        'of total commissioning volume throughout the entire 75-year window. Sci-fi (the blue and magenta bands) '
        'has never exceeded roughly 5-6% combined share even at its peak - a real, humbling piece of context: even '
        'sci-fi\'s most successful era is a modest slice of an industry Drama and Comedy have owned from the start. '
        'Horror and Action are the two genres that have visibly grown their share the most since the 1980s-90s, at '
        'sci-fi\'s relative expense.</div></div>',
        unsafe_allow_html=True
    )

    st.subheader("Sci-Fi vs. Genre-Adjacent Comparisons")
    st.pyplot(build_comparison_line_chart())
    st.pyplot(build_decade_comparison_chart())
    st.markdown(
        '<div class="key-finding-box"><div class="label">Key Finding</div>'
        '<div class="finding-text">Science Fiction (film) peaked in the 1980s (4.85% average share) and has declined '
        'every decade since (2.79% in the 2020s), while Sci-Fi & Fantasy (TV) has risen in every decade without '
        'exception (0.14% in the 1950s to 3.07% in the 2020s) - overtaking film\'s share for the first time in the '
        '2020s. Sci-fi\'s growth story of the last three decades has happened on television, not film.</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="precedent-line">Note: TMDb\'s genre taxonomy differs between film and TV - Science Fiction, '
        'Fantasy, and Horror exist only as film genres, while Sci-Fi & Fantasy is a TV-only bundle covering what '
        'film treats as two separate categories. Each genre above is labeled by its actual Film / TV / Film+TV '
        'scope rather than treated as uniformly measured across media.</div>',
        unsafe_allow_html=True
    )

elif view == "Lag Analysis":
    st.title("Page to Screen")
    st.header("Lag Analysis")
    st.markdown(
        "How many years apart are publishing and commissioning trends, per theme? "
        "Computed via cross-correlation, testing lags from -10 to +10 years and finding "
        "which lag best aligns each theme's publishing series with its commissioning "
        "series, over the comparable 1950-2020 window."
    )

    st.pyplot(build_lag_chart())

    st.markdown(
        '<div class="key-finding-box"><div class="label">Key Finding</div>'
        '<div class="finding-text">Robots sits at exactly zero lag with the strongest correlation of any theme '
        '(r=0.83) - the tightest synchronization in the dataset. Most themes (apocalyptic, dystopia, space opera, '
        'cyberpunk, time travel) show commissioning leading publishing by 1-3 years. Alternate universe is the '
        'clearest outlier, with commissioning leading by 6 years. Aliens and steampunk are the only two themes '
        'where books lead.</div></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="precedent-line">Caveat: a single best-fit lag can flatten a relationship that shifts '
        'character across eras. Aliens\' result (+5 years, books leading) is dominated by the high-volume '
        '2000s-2010s period and doesn\'t capture the theme\'s actual two-phase history - commissioning led for '
        'decades early on before books later caught up and surged past.</div>',
        unsafe_allow_html=True
    )

else:
    st.title("Page to Screen")
    st.info(view + " section coming soon.")

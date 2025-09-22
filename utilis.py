import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# -------------------
# Data Cleaning / Prep
# -------------------
def clean_missing_values(df, fill_columns=None):
    """
    Fill or drop missing values in specified columns.
    """
    if fill_columns:
        for col in fill_columns:
            df[col] = df[col].fillna("Unknown")
    return df.dropna(subset=['title', 'year'])

def extract_year(df, date_column='publish_time'):
    """
    Convert a column to datetime and extract year.
    """
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    df['year'] = df[date_column].dt.year
    return df

# -------------------
# Text Analysis
# -------------------
def get_top_words(series, n=10):
    """
    Get top n most frequent words from a pandas Series of text.
    """
    text = " ".join(series.dropna().astype(str).tolist())
    words = text.lower().split()
    return Counter(words).most_common(n)

# -------------------
# Visualization
# -------------------
def plot_publications_by_year(df):
    """
    Returns a matplotlib figure of publications by year.
    """
    year_counts = df['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue", ax=ax)
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Papers")
    ax.set_title("Publications by Year")
    return fig

def plot_top_journals(df, top_n=10):
    """
    Returns a matplotlib figure of top N journals by number of papers.
    """
    top_journals = df['journal'].value_counts().head(top_n)
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis", ax=ax)
    ax.set_xlabel("Number of Papers")
    ax.set_ylabel("Journal")
    ax.set_title(f"Top {top_n} Journals")
    return fig

# CORD-19 Data Explorer

## Project Overview
This project explores the **CORD-19 dataset**, which contains metadata of COVID-19 research publications.  
It includes **data cleaning, analysis, visualization**, and an interactive **Streamlit dashboard** for exploring publication trends, top journals, and common keywords in paper titles.

---

## Tools and Technologies
- **Python 3.7+**
- **pandas** – Data manipulation
- **matplotlib / seaborn** – Data visualization
- **collections.Counter** – Word frequency analysis
- **Streamlit** – Interactive dashboard
- **Jupyter Notebook** – Optional for exploration

---

## Project Workflow

### 1. Data Loading & Exploration
- Loaded the `metadata.csv` from the CORD-19 dataset.
- Explored the dataset:
  - Dimensions and column types
  - Missing values
  - Basic statistics

### 2. Data Cleaning & Preparation
- Dropped columns with excessive missing values.
- Filled missing values in `authors`, `journal`, and `abstract`.
- Converted `publish_time` to datetime and extracted the publication year.
- Created `abstract_word_count` for analysis.
- Saved cleaned data as `cord19_metadata_clean.csv`.

### 3. Data Analysis & Visualization
- Counted papers per year and plotted a bar chart.
- Identified **top journals** by publication count.
- Extracted **most frequent words** from paper titles.
- Visualized distribution by journal.

### 4. Streamlit Dashboard
- Interactive **year slider** to filter publications.
- **Journal dropdown** to select a specific journal or view all.
- Visualizations:
  - Publications by year
  - Top journals (bar chart)
  - Top words in titles
- **Sample data table** preview.
- **CSV download button** for filtered data.

### 5. Reflection
- Challenges:
  - Handling missing values and large dataset
  - Virtual environment and package setup
  - Running Streamlit separately from Jupyter
- Learnings:
  - Importance of data cleaning
  - Using pandas, seaborn, matplotlib for analysis
  - Building interactive dashboards with Streamlit
- Future improvements:
  - Word cloud visualization
  - Multi-select journal filter
  - Filters by abstract length or author
  - Deploy dashboard online

---

## Key Findings
- Most papers were published in **2020–2021**.
- Top journals: **Nature, Science, The Lancet, BMJ, JAMA**.
- Frequent title keywords: **COVID-19, vaccine, pandemic, clinical, health**.
- A few journals dominate COVID-19 research publications.

---

## How to Run
1. Clone the repository:
```bash
git https://github.com/abiolalawal14/Python-Frameworks

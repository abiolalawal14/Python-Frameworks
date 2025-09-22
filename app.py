import streamlit as st
import pandas as pd
from utilis import clean_missing_values, extract_year, get_top_words, plot_publications_by_year, plot_top_journals

# -------------------
# Load Data
# -------------------
df = pd.read_csv("https://github.com/abiolalawal14/Python-Frameworks/blob/main/cord19_metadata_clean.csv")

# -------------------
# App Title
# -------------------
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research publications interactively")

# -------------------
# Year Slider
# -------------------
df = extract_year(df)
min_year = int(df['year'].min())
max_year = int(df['year'].max())

year_range = st.slider(
    "Select publication year range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# -------------------
# Journal Dropdown
# -------------------
journals = ["All"] + df['journal'].unique().tolist()
selected_journal = st.selectbox("Select a Journal", journals)

if selected_journal != "All":
    filtered_df = filtered_df[filtered_df['journal'] == selected_journal]

# -------------------
# Top Journals Chart
# -------------------
if selected_journal == "All":
    st.subheader("Top Journals")
    fig = plot_top_journals(filtered_df)
    st.pyplot(fig)

# -------------------
# Publications by Year Chart
# -------------------
st.subheader("Publications by Year")
fig = plot_publications_by_year(filtered_df)
st.pyplot(fig)

# -------------------
# Most Frequent Words
# -------------------
st.subheader("Most Frequent Words in Titles")
top_words = get_top_words(filtered_df['title'], n=10)
for word, count in top_words:
    st.write(f"{word}: {count}")

# -------------------
# Sample Data Table
# -------------------
st.subheader("Sample Papers")
st.dataframe(filtered_df[['title','authors','journal','year']].head(20))

# -------------------
# Download Button
# -------------------
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_cord19_data.csv',
    mime='text/csv'
)

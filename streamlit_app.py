import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="📊")

st.title('📊 Exploratory Data Analysis')

st.info('This demo shows the use of Pandas for loading data as DataFrames and Altair for chart creation.')

st.header('Which Movie Genre performs best at the box office?')

# Load data
df = pd.read_csv('data/movies_genres_summary.csv')

# Input widgets
## Genres selection
genres_list = df.genre.unique()
genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])
df_selection = df[df.genre.isin(genres_selection)]

## Year selection
year_list = df.year.unique()
year_selection = st.slider(year_list.min(), year_list.max(), (year_list[-10], year_list[-1]))
# 0.0, 100.0, (25.0, 75.0)

# Display DataFrame
df_selection

# Display chart
st.line_chart(df_selection, x='year', y='gross', color='genre')

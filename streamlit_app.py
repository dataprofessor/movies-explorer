import streamlit as st
import pandas as pd

st.title('📊 Exploratory Data Analysis')

st.info('This demo shows the use of Pandas for loading data as DataFrames and Altair for chart creation.')

st.header('Which movie Genre performs best at the box office?')

# Load data
df = pd.read_csv('data/movie_genres_summary.csv')

genres_list = df.genre.unique()

# genres_list 
genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])
df_selection = df_genres[df_genres.genre.isin(genres_selection)]

df_selection

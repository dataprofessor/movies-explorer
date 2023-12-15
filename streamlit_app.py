import streamlit as st
import pandas as pd

st.title('📊 Exploratory Data Analysis')

st.info('This demo shows the use of Pandas for loading data as DataFrames and Altair for chart creation.')

st.header('Which movie Genre performs best at the box office?')

# Load data
df = pd.read_csv('data/tmdb_5000_movies_mergedwith_movie_metadata.csv')

genres_list = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 
               'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 
               'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Romance', 
               'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
genres_selection = st.multiselect('Select genres', genres_list, 'Action')
st.write(genres_selection)

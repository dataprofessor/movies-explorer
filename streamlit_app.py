import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="📊")

st.title('📊 Exploratory Data Analysis')

st.info('This demo shows the use of Pandas for loading data as DataFrames and Altair for chart creation.')

st.subheader('Which Movie Genre performs best at the box office?')

# Load data
df = pd.read_csv('data/movies_genres_summary.csv')
df.year = df.year.astype('int')

# Placeholder
placeholder1 = st.empty()
placeholder2 = st.empty()

# Input widgets
## Genres selection
genres_list = df.genre.unique()
genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])
## Year selection
year_list = df.year.unique()
year_selection = st.slider('Select year duration', 1986, 2006, (2012, 2016))
year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

# df.genre.isin(genres_selection)
# df.year.isin(year_selection_list)
df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)

# Display DataFrame
with placeholder1:
    df_editor = st.dataframe(reshaped_df, height=212, use_container_width=True,
                             column_config={"year": st.column_config.TextColumn("Year")})

# Display chart
with placeholder2:
    #st.line_chart(df_selection, x='year', y='gross', color='genre')
    chart = alt.Chart(df_selection).mark_line().encode(
        x=alt.X('year:N', title='Year'),
        y=alt.Y('gross:Q', title='Gross earnings in dollars')
        color='genre:N'
    )
    st.altair_chart(chart, use_container_width=True)


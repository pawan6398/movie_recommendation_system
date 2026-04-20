import streamlit as st
import pickle
import pandas as pd
import requests

# Fetch poster from TMDB
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=dc2526809eeaa8b043757ea00ee85db7".format(movie_id)
    response = requests.get(url)
    data = response.json()

    return "https://image.tmdb.org/t/p/w500" + data.get('poster_path', '')


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommend_movies, recommended_movies_posters


movie_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
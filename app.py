import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_movie_details(movie_id):
    API_KEY = os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            poster_url = "Poster not available"

        overview = data.get("overview", "No overview available.")
        genres_list = data.get("genres", [])
        genres = ", ".join([genre["name"] for genre in genres_list]) if genres_list else "Unknown"
        return {"poster_url": poster_url, "overview": overview, "genres": genres}
    else:
        st.error(f"Failed to retrieve data: {response.status_code}")
        return None


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    similarities = []
    for row in similarity_matrix:
        similarities.append(row[movie_index])
    # Get top 5 recommendations (skip the first one as it is the movie itself)
    finalList = sorted(list(enumerate(similarities)), reverse=True, key=lambda x: x[1])[1:6]

    films = []
    details_list = []
    for index, score in finalList:
        film_title = movies_list.iloc[index].title
        films.append(film_title)
        # Fetch full details from TMDb API (including poster, genres, overview)
        movie_id_val = movies_list.iloc[index].movie_id
        details = fetch_movie_details(movie_id_val)
        details_list.append(details)
    return films, details_list


def display_recommendations(films, details_list):
    """
    Displays the recommended movies in a layout with 5 movies per row.
    In each cell, the poster is shown at the top with movie details (name, genre, overview) below it.
    """
    for i in range(0, len(films), 5):
        row_cols = st.columns(5, gap="medium")
        for j in range(5):
            idx = i + j
            if idx < len(films):
                with row_cols[j]:
                    # Display poster on top
                    st.image(details_list[idx]["poster_url"], width=200)
                    # Then the movie details below the poster
                    st.markdown(f"#### {films[idx]}")
                    st.markdown(
                        f"<span style='font-size:12px;'><strong>Genre:</strong> {details_list[idx]['genres']}</span>",
                        unsafe_allow_html=True)
                    # Optionally truncate the overview to keep it compact
                    short_overview = details_list[idx]['overview'][:150] + "..."
                    st.markdown(short_overview)
        st.write("---")

# Load data
movies_list = pickle.load(open('data/movies.pkl', 'rb'))
similarity_matrix = pickle.load(open('data/similarity_matrix.pkl', 'rb'))

st.set_page_config(page_title="Movie Recommender System", layout="wide")

st.markdown("<h1 style='text-align: center;'>Movie Recommender System</h1>", unsafe_allow_html=True)

with st.container():
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        selected_movie = st.selectbox('Select a Movie', movies_list['title'].values)
        recommend_button = st.button("Recommend")

    if recommend_button:
        if selected_movie.strip() != "":
            films, details_list = recommend(selected_movie)
            display_recommendations(films, details_list)
        else:
            st.warning("Please enter a movie name.")

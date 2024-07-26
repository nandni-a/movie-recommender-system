import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6741f181ff0021d54452cb38349b6339&language=en-us'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append((movies.iloc[i[0]].title))
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')


selected_movie_name = st.selectbox('Select The Movie',movies['title'].values)
if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.markdown(f"<h3 style='text-align: center;'>{names[0]}</h3>", unsafe_allow_html=True)
        st.image(poster[0], use_column_width=True)

    with col2:
        st.markdown(f"<h3 style='text-align: center;'>{names[1]}</h3>", unsafe_allow_html=True)
        st.image(poster[1], use_column_width=True)

    with col3:
        st.markdown(f"<h3 style='text-align: center;'>{names[2]}</h3>", unsafe_allow_html=True)
        st.image(poster[2], use_column_width=True)

    with col4:
        st.markdown(f"<h3 style='text-align: center;'>{names[3]}</h3>", unsafe_allow_html=True)
        st.image(poster[3], use_column_width=True)

    with col5:
        st.markdown(f"<h3 style='text-align: center;'>{names[4]}</h3>", unsafe_allow_html=True)
        st.image(poster[4], use_column_width=True)









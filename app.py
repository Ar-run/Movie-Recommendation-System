import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.markdown(
    """
    <style>
    .stApp {
        background-color: #39b39c;  /* Light Blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)



def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
      
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
        
st.title('🎬 Movie Recommendation System')
st.markdown("<h4 style='text-align: center;'>Type a movie's name or select a movie from the dropdown, and we'll recommend similar movies based on your choice.</h4>", unsafe_allow_html=True)
selected_movie_name = st.selectbox(
    "",
    ["Select a movie"] + list(movies['title'].values)
    #movies['title'].values
    )

if st.button("🔍 Get Recommendations", key="recommend_btn"):
    if selected_movie_name != "Select a movie":  
        recommendations = recommend(selected_movie_name)
        for i in recommendations:
            st.markdown(f"<h5 style='color: black; font-weight: bold;'>{i}</h5>", unsafe_allow_html=True)
    else:
        st.warning("Please select a movie to get recommendations.")

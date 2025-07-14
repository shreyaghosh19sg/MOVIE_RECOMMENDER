import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Set page config at the very top
st.set_page_config(page_title="Netflix Movie Recommender", layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    df = df.dropna(subset=['description'])  # Drop rows with missing descriptions
    return df

df = load_data()

# Compute TF-IDF similarity matrix
@st.cache_data
def compute_similarity(data):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['description'])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

similarity = compute_similarity(df)

# Recommendation function
def recommend(title, df, similarity_matrix, top_n=5):
    title = title.lower()
    matches = df[df['title'].str.lower() == title]
    if matches.empty:
        return []
    idx = matches.index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df.iloc[movie_indices][['title', 'description']]

# UI
st.title("🎬 Netflix Movie Recommender")

movie_list = df['title'].dropna().unique()
selected_movie = st.selectbox("Select a Movie", sorted(movie_list))

if st.button("Recommend"):
    results = recommend(selected_movie, df, similarity)
    if not results.empty:
        st.subheader("🔍 You might also like:")
        for _, row in results.iterrows():
            st.markdown(f"**🎥 {row['title']}**\n\n> {row['description']}")
    else:
        st.warning("No similar titles found.")

# MOVIE_RECOMENDER
# 🎬 Movie Recommender System – Netflix-Style (AI + Streamlit)

A Netflix-style **Movie Recommendation System** built using **Streamlit** and a dataset of movies in CSV format. This project uses **content-based filtering** to recommend similar movies based on user selection.

---

## 📌 Features

- 🔍 Select a movie and get top recommendations instantly
- 🧠 Content-based filtering using similarity scores
- 📄 Uses a dataset of 100+ movies (Netflix-style CSV)
- 🎨 Clean and interactive Streamlit UI
- 📸 Movie posters (optional with TMDB API)
- 💾 Lightweight and easy to deploy

---

## 📂 Dataset

- File: `movies.csv`
- Format: CSV with columns like:
  - `title`
  - `genres`
  - `overview`
  - `tags` or `combined_features` (optional)
  - `movie_id` (optional for API/posters)

> You can customize this to your actual dataset column names.

---

## 🛠️ Tech Stack

- **Python 3.7+**
- **Streamlit**
- **Pandas, Scikit-learn, NumPy**
- (Optional) **Requests** – for fetching posters via API

---

## ▶️ How to Run the App

1. Clone this repository or download the files.
2. Install required dependencies:

```bash
pip install streamlit pandas scikit-learn numpy

# movie_recommendation_system
A content-based Movie Recommendation System built with Python and Streamlit that uses machine learning techniques to suggest similar movies based on user preferences. The system leverages similarity scores computed from movie data and provides an interactive web interface along with movie posters using the TMDB API.
# 🎬 Movie Recommendation System

A **content-based Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.
This application suggests similar movies based on user input and displays posters using the TMDB API.

---

## 🚀 Live Project

👉 https://github.com/pawan6398/movie_recommendation_system

---

## 📌 Overview

This project uses **content-based filtering** to recommend movies.
It analyzes movie features like genres, keywords, and tags, and finds similarity between movies using **cosine similarity**. ([tuhindutta.github.io][1])

---

## ✨ Features

* 🎥 Recommend top 5 similar movies
* 🧠 Machine Learning based (Cosine Similarity)
* 📊 Content-based filtering approach
* 🌐 Fetch movie posters using TMDB API
* ⚡ Interactive UI using Streamlit

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas
* Scikit-learn
* Streamlit
* TMDB API

---

## 📂 Project Structure

```
movie_recommendation_system/
│
├── app.py                  # Streamlit app
├── movie_dict.pkl          # Movie dataset
├── similarity.pkl          # Similarity matrix (optional)
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/pawan6398/movie_recommendation_system.git
cd movie_recommendation_system
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Application

```
streamlit run app.py
```

---

## 🧠 How It Works

1. Load movie dataset
2. Convert text data into vectors
3. Apply cosine similarity
4. Recommend top similar movies

---

## 🌐 API Used

* TMDB (The Movie Database) API for movie posters and details
  👉 https://www.themoviedb.org/

---

## ⚠️ Important Notes

* You need a TMDB API key
* Large `.pkl` files may cause deployment issues
* You can compute similarity at runtime instead of storing it

---

## 📸 Screenshots

(Add screenshots here)

---

## 🙌 Future Improvements

* 🔍 Add search autocomplete
* ⭐ Add ratings & reviews
* 📱 Improve UI/UX
* ☁️ Deploy on cloud (Streamlit Cloud / Render)

---

## 👨‍💻 Author

**Pawan Verma**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

[1]: https://tuhindutta.github.io/Movie-Recommendation-System/?utm_source=chatgpt.com "🎬 Movie Recommendation System | Movie-Recommendation-System"

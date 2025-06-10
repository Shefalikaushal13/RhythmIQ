# 🎧 RhythmIQ

**RhythmIQ** is a Flask-based web application that delivers personalized english song recommendations rooted in nostalgia. Powered by machine learning, it analyzes audio features like tempo, energy, and valence to recommend songs from a pre-2021 collection of 170,000+ tracks — perfect for rediscovering classics that match your vibe.



---


## 🧠 What It Does

- Accepts a user’s favorite song as input.
- Uses **K-Means Clustering** applied to segment a dataset of **170,000+ tracks** into meaningful clusters.
- Uses **KNN** to find musically similar tracks with **over 97% similarity accuracy** based on extracted audio features.
- Cluster count optimized using the **Elbow Method**.
- Renders a responsive web interface for interacting with the model.
- Returns a table of top recommended tracks with artist names and release year.

---

## 🚀 Tech Stack

| Layer       | Technology                    |
|-------------|-------------------------------|
| Language    | Python 3.9                    |
| Web Server  | Flask                         |
| Frontend    | HTML, CSS   |
| ML Algorithms  | KNeighborsClassifier and K-Means |
| Dataset     | Spotify Audio Features (Kaggle) |
| Deployment  | Render (Flask backend)        |

---

## 📊 Dataset Overview

- **Source**: [Kaggle - Spotify Dataset 1921–2020](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset)
- **Size**: ~1,70,000+ songs
- **Key Features Used**:
  - `danceability`
  - `energy`
  - `valence`
  - `tempo`
  - `liveness`
  - `acousticness`
  - `speechiness`
  - `instrumentalness`
- **Target Feature**: Song Name

---

## 🧪 How It Works

1. User enters a song name.
2. The song is matched with its audio features from the dataset.
3. KNN is applied to retrieve the `k` most similar songs.
4. The response is rendered on the webpage as a styled table with track name, artist, and year of release.

---

## 🖥️ Demo
- **Source**: [Live Link](https://rhythmiq-9h5k.onrender.com/)
- ![Screenshot 2025-06-10 102953](https://github.com/user-attachments/assets/38b5c3e9-4276-4e29-83e4-b7e2a745d8a2)
- ![Screenshot 2025-06-10 104739](https://github.com/user-attachments/assets/4674a0cf-9cc6-4c41-b4cd-754e5348f3f3)


  
---

## ✍️ Author
Shefali Kaushal
- [Linkedin](https://www.linkedin.com/in/shefalikaushal/)

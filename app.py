from flask import Flask, render_template,request
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)

df=pd.read_csv("clustered_df.csv")

features = ['valence', 'acousticness', 'danceability', 'energy',
            'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo']

def get_song_recommendations(song_name, top_n=5):
    song_matches = df[df['name'].str.lower() == song_name.lower()]

    if song_matches.empty:
        return []

    df_clean = df.dropna(subset=features)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_clean[features])

    nn_model = NearestNeighbors(n_neighbors=top_n + 1)
    nn_model.fit(X_scaled)

    input_song = song_matches.iloc[0]
    input_vector = input_song[features].values.reshape(1, -1)
    input_scaled = scaler.transform(input_vector)

    distances, indices = nn_model.kneighbors(input_scaled)

    recommendations = df_clean.iloc[indices[0]]
    recommendations = recommendations[recommendations['name'].str.lower() != song_name.lower()]

    result_table = recommendations[['name', 'artists', 'year']].reset_index(drop=True)
    result_table.columns = ['name', 'artists', 'year'] 

    return result_table.to_dict(orient="records")



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/recommend", methods=['POST','GET'])
def recommend():
    recommendations = []
    if request.method == "POST":
        song_name = request.form.get("song_name")
        try:
            recommendations = get_song_recommendations(song_name)
            if not recommendations:
                recommendations = [{'name': 'Not Found', 'artists': 'N/A', 'year': 'N/A'}]
        except Exception as e:
            recommendations = [{'name': 'Error', 'artists': str(e), 'year': 'N/A'}]
    return render_template("index.html", recommendations=recommendations)


if __name__ == "__main__":    #app call
    app.run(debug=True)

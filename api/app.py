from flask import Flask
from flask import request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

model = pickle.load(open('mood_classification.pkl', 'rb'))

@app.route("/")
def hello():
    return "Hey Stranger"

@app.route('/get-lyrics', methods = ['POST'])
def get_lyrics():
    data = request.get_json()
    lyric_pred= data["lyrics"]
    daa=np.array([lyric_pred])
    ser=pd.Series(daa,index=[0])
    y_pred = str(model.predict(ser)[0])
    return {"mood": y_pred}

if __name__ == "__main__":
    app.run()
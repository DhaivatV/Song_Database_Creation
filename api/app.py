from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey Stranger"

@app.route('/get-lyrics', methods = ['POST'])
def get_lyrics():
    data = request.get_json()
    print(data)
    return 0

if __name__ == "__main__":
    app.run()
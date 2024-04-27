from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, static_url_path="/static")


model = pickle.load(open("model.pkl", "rb"))


@app.route("/facialSearch")

@app.route("/predict", methods=["POST"])
def predict():
    
        return


if __name__ == "__main__":
    app.run(debug=True)

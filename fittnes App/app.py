# import the libraries
from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

# This is a simple Flask application that serves a machine learning model for fitness prediction.
app = Flask(__name__)

# Load the model
with open('fitness.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    prediction = model.predict(np.array([data]))
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
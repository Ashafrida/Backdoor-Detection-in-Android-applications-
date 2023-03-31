from flask import Flask, jsonify, request
import sqlite3
from sklearn.externals import joblib

app = Flask(__name__)

@app.before_first_request
def init_db():
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS activities (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
    conn.commit()
    conn.close()
@app.route('/activities', methods=['GET'])
def get_activities():
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM activities')
    rows = cursor.fetchall()
    conn.close()
    return jsonify({'activities': rows})

@app.route('/activities', methods=['POST'])
def add_activity():
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()
    name = request.json['name']
    cursor.execute('INSERT INTO activities (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Activity added successfully'})
clf = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    features = request.json['features']
    prediction = clf.predict(features)
    return jsonify({'prediction': prediction})
if __name__ == '__main__':
    app.run()

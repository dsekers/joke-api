from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything.",
    "What did the zero say to the eight? Nice belt!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why was the computer cold? It left its Windows open.",
    "Parallel lines have so much in common… it’s a shame they’ll never meet."
]

@app.route('/joke', methods=['GET'])
def get_joke():
    return jsonify({"joke": random.choice(jokes)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
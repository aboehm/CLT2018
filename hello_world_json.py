from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    # dict in JSON umwandeln
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    app.run()

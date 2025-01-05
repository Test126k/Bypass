from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'status': 'success', 'message': 'hello'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Use 0.0.0.0 to make it externally accessible

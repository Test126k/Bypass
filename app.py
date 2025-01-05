import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'status': 'success', 'message': 'hello'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use Koyeb's PORT environment variable
    app.run(host='0.0.0.0', port=port)  # Bind to all network interfaces

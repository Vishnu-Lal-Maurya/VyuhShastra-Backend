# app.py
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)



@app.route('/')
def hello_world():
    return "hello world  to me"


# API Endpoint for Hello World
@app.route('/', methods=['POST'])
def hello_world_post():
    return jsonify({
        'message': f"Hello from Flask!"
    })

 



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

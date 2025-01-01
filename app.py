# app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_jwt_extended import jwt_required, get_jwt_identity



from flask import Flask, request, send_from_directory, jsonify
import os




app = Flask(__name__)



# Directory where uploaded files are saved
UPLOAD_FOLDER = 'server/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from models import db, Company, Workspace, File, Report, Dashboard, Chart
import os

from routes.authentication import auth_bp
from routes.workspace import workspace_bp

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'  # Path to store uploaded files
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Ensure upload folder exists
app.secret_key = os.urandom(24)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()


#Register Blueprints here -- 
app.register_blueprint(auth_bp)
app.register_blueprint(workspace_bp)

@app.route('/')
def hello_world():
    return "Hello from Flask!"

# Serve the uploaded files
@app.route('/uploads/<filename>')
@jwt_required()
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created if they don't exist
    app.run(debug=True, host='0.0.0.0', port=5000)



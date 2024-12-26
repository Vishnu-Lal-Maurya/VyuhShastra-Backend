from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, Company
import datetime
import json

# Create a Blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/signup', methods=['POST'])
def signup():
    # Parse JSON request data
    data = request.json

    # Extract data
    name = data.get('companyFullName')
    email = data.get('companyEmail')
    password = data.get('companyPassword')
    website_url = data.get('companyWebsite')

    # Validate input
    if not name or not email or not password:
        return jsonify({"error": "Please fill out all required fields!"}), 400

    # Check if a company with this email already exists
    existing_company = Company.query.filter_by(email=email).first()
    if existing_company:
        return jsonify({"error": "A company with this email already exists!"}), 409

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new Company object
    new_company = Company(
        name=name,
        email=email,
        password=hashed_password,
        website_url=website_url
    )

    try:
        # Add the company to the database
        db.session.add(new_company)
        db.session.commit()
        return jsonify({"message": "Company created successfully!"}), 201
    except Exception as e:
        # Rollback the session on error
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    print("login is hit")
    
    # Extract email and password
    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not email or not password:
        return jsonify({"error": "Please provide both email and password!"}), 400

    # Check if the user exists
    company = Company.query.filter_by(email=email).first()
    if not company or not check_password_hash(company.password, password):
        return jsonify({"error": "Invalid email or password!"}), 401

    # Create a JWT access token
    access_token = create_access_token(
        identity=json.dumps({"id": company.id, "email": company.email}),
        expires_delta=datetime.timedelta(hours=1)
    )

    return jsonify({"message": "Login successful!", "access_token": access_token}), 200


@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access the current user's identity
    current_user = get_jwt_identity()
    return jsonify({"message": "You are authorized!", "user": current_user}), 200
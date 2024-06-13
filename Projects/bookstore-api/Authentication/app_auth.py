from flask import Blueprint, request, jsonify # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore
import jwt # type: ignore
import datetime
from .models import User # type: ignore
from . import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login failed!'}), 401
    token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 
                        'your_secret_key', algorithm='HS256')
    return jsonify({'token': token})

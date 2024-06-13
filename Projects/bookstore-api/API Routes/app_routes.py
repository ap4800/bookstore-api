from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from .models import Book
from . import db
from .utils import token_required

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class BookListResource(Resource):
    @token_required
    def get(self, current_user):
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books])

    @token_required
    def post(self, current_user):
        data = request.get_json()
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201

class BookResource(Resource):
    @token_required
    def get(self, current_user, book_id):
        book = Book.query.get_or_404(book_id)
        return jsonify(book.to_dict())

    @token_required
    def put(self, current_user, book_id):
        data = request.get_json()
        book = Book.query.get_or_404(book_id)
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return jsonify(book.to_dict())

    @token_required
    def delete(self, current_user, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return '', 204

api.add_resource(BookListResource, '/books')
api.add_resource(BookResource, '/books/<int:book_id>')

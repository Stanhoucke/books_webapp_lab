from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import book_repository
from repositories import author_repository
from models.book import Book

# A blueprint is a collection of routes
books_blueprint = Blueprint("books", __name__)

# INDEX
@books_blueprint.route('/books')
def books():
    # Get all the tasks from the db
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)


# NEW
# GET '/books/new'
# @route(/books/new)
# CREATE
# POST '/books'

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>/delete'
@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')


from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository

#Save
def save(book):
    sql = "INSERT INTO books (title, genre, publisher, author_id) values (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.publisher, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

# Delete
def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Select by id
def select(id):
    book = None

    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], result['genre'], result['publisher'], author, result['id'])
    return book

# Select all
def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['publisher'], author, row['id'])
        books.append(book)

    return books


# def select(id):
#     book = None

#     sql = "SELECT * FROM books WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         author = author_repository.select(result['author_id'])
#         book = Book(result['title'], author, result['id'])
#     return book

# def select_all():
#     books = []

#     sql = "SELECT * FROM albums"
#     results = run_sql(sql)
#     for row in results:
#         artist = artist_repository.select(row['artist_id'])
#         album = Album(row['title'], artist, row['genre'], row['id'])
#         albums.append(album)

#     return albums
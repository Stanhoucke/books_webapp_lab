from db.run_sql import run_sql
from models.author import Author
from models.book import Book
# import repositories.book_repository as book_repository

#Delete
def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#Select
def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'] )
        authors.append(author)
    return authors

#Select by id
def select(id):
    author = None

    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['first_name'], result['last_name'], result['id'])

    return author
from db.run_sql import run_sql
from models.author import Author
from models.book import Book
# import repositories.book_repository as book_repository

#DELETE
def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)
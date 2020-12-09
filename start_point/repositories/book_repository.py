from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository

# Delete
def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

# album_repository.delete_all()
# artist_repository.delete_all()

author_1 = Author('Pablo', 'Coelho')
author_repository.save(author_1)

book_1 = Book("The Alchemist",  "Fantasy", "Penguin", author_1)
book_repository.save(book_1)
# album_2 = Album("Another Album", artist_1, "Pop")
# album_repository.save(album_2)

# album_1.genre = "Pop"
# album_repository.update(album_1)

# for album in album_repository.select_all():
#     print(album.__dict__)
class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str, pages: int):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"Книга '{self.title}' успешно взята.")
        else:
            print(f"Книга '{self.title}' уже занята.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Книга '{self.title}' успешно возвращена.")
        else:
            print(f"Книга '{self.title}' уже доступна.")

# Книги
book1 = Book(
    title="Преступление и наказание",
    author="Фёдор Достоевский",
    year=1866,
    isbn="978-5-17-090879-1",
    pages=608
)

book2 = Book(
    title="Мастер и Маргарита",
    author="Михаил Булгаков",
    year=1967,
    isbn="978-5-389-06204-3",
    pages=480
)

print("\n=== КНИГИ ===")
print(f"'{book1.title}' — доступна: {book1.available}")
print(f"'{book2.title}' — доступна: {book2.available}")

# Попробуем взять книгу
book1.borrow_book()
print(f"'{book1.title}' — теперь доступна: {book1.available}")

# Вернём книгу
book1.return_book()
print(f"'{book1.title}' — снова доступна: {book1.available}")
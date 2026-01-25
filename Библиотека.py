class LibraryItem:
    def __init__(self, title: str, author: str, year: int):
        self._title = title
        self._author = author
        self._year = year
        self.__item_id = None
        self.__is_checked_out = False


    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_year(self):
        return self._year

    def is_checked_out(self):
        return self.__is_checked_out

    def set_checked_out(self, value: bool):
        if isinstance(value, bool):
            self.__is_checked_out = value
        else:
            raise ValueError("Значение должно быть True или False")

    def _get_item_id(self):
        return self.__item_id

    def _set_item_id(self, item_id: str):
        self.__item_id = item_id

    def __str__(self):
        status = "Взято" if self.__is_checked_out else "Доступно"
        return f"'{self._title}' ({self._author}, {self._year}) — {status}"


class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, genre: str, page_count: int):
        super().__init__(title, author, year)
        self.genre = genre
        self.__page_count = None
        self.set_page_count(page_count)


    def get_page_count(self):
        return self.__page_count

    def set_page_count(self, value: int):
        if value < 1:
            raise ValueError("Количество страниц не может быть меньше 1")
        self.__page_count = value

    def __str__(self):
        base = super().__str__()
        return f"{base} | Жанр: {self.genre}, Страниц: {self.__page_count}"


class Magazine(LibraryItem):
    def __init__(self, title: str, author: str, year: int, issue_number: int):
        super().__init__(title, author, year)
        self._issue_number = issue_number

    def get_issue_number(self):
        return self._issue_number

    def set_issue_number(self, value: int):
        self._issue_number = value

    def get_magazine_info(self):
        """Свой метод для получения информации о журнале"""
        return f"Журнал '{self._title}', выпуск #{self._issue_number}, {self._year}"

    def __str__(self):
        base = super().__str__()
        return f"{base} | Выпуск: {self._issue_number}"

class DVD(LibraryItem):
    def __init__(self, title: str, author: str, year: int, duration: int, rating: str):
        super().__init__(title, author, year)
        self.__duration = None
        self.__rating = None
        self.set_duration(duration)
        self.set_rating(rating)

    # Геттер и сеттер для __duration
    def get_duration(self):
        return self.__duration

    def set_duration(self, value: int):
        if not (1 <= value <= 300):
            raise ValueError("Продолжительность должна быть от 1 до 300 минут")
        self.__duration = value

    def get_rating(self):
        return self.__rating

    def set_rating(self, value: str):
        valid_ratings = {"G", "PG", "PG-13", "R", "NC-17"}
        if value not in valid_ratings:
            raise ValueError(f"Рейтинг должен быть одним из: {valid_ratings}")
        self.__rating = value

    def __str__(self):
        base = super().__str__()
        return f"{base} | Длительность: {self.__duration} мин, Рейтинг: {self.__rating}"


# Создание объектов
book = Book("Преступление и наказание", "Ф. Достоевский", 1866, "Роман", 608)
magazine = Magazine("Наука и жизнь", "Редакция", 2025, 5)
dvd = DVD("Начало", "Кристофер Нолан", 2010, 148, "PG-13")

# Установка ID 
book._set_item_id("BK-001")
magazine._set_item_id("MZ-001")
dvd._set_item_id("DVD-001")

print("=== БИБЛИОТЕЧНЫЕ ЭЛЕМЕНТЫ ===\n")

print(book)
print(magazine)
print(dvd)

print("\n--- Информация о журнале ---")
print(magazine.get_magazine_info())

print("\n--- Попытка изменить статус выдачи ---")
book.set_checked_out(True)
print(book)

print("\n--- Изменение количества страниц книги ---")
try:
    book.set_page_count(500)
    print(book)
except ValueError as e:
    print(f"Ошибка: {e}")

print("\n--- Изменение рейтинга DVD ---")
try:
    dvd.set_rating("R")
    print(dvd)
except ValueError as e:
    print(f"Ошибка: {e}")
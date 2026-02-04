# === Класс House ===
class House:
    def __init__(self, address: str, area: float, price: float):
        self.address = address
        self._area = area
        self._price = price

    def final_price(self, discount: float) -> float:
        if not (0 <= discount <= 100):
            raise ValueError("Скидка должна быть от 0% до 100%")
        return self._price * (1 - discount / 100)


# === Класс SmallHouse (наследуется от House) ===
class SmallHouse(House):
    def __init__(self, address: str, price: float):
        super().__init__(address, area=40.0, price=price)


# === Класс Human ===
class Human:
    default_name = "Неизвестно"
    default_age = 0

    def __init__(self, name: str = None, age: int = None):
        self.name = name if name is not None else self.default_name
        self.age = age if age is not None else self.default_age
        self.__money = 0.0
        self.__house = None

    def info(self):
        house_info = self.__house.address if self.__house else "Нет дома"
        print(f"Имя: {self.name}, Возраст: {self.age}, Дом: {house_info}, Деньги: {self.__money:.2f} руб.")

    @staticmethod
    def default_info():
        print(f"Стандартное имя: {Human.default_name}, Стандартный возраст: {Human.default_age}")

    def __make_deal(self, house, price: float):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.__money += amount

    def buy_house(self, house, discount_size: float):
        if not isinstance(house, House):
            raise TypeError("Первый аргумент должен быть объектом класса House")

        final_price = house.final_price(discount_size)

        if self.__money < final_price:
            print(f"Недостаточно средств! Требуется {final_price:.2f}, есть {self.__money:.2f}")
            return False

        self.__make_deal(house, final_price)
        print(f"Дом куплен за {final_price:.2f} руб.")
        return True

# 1. Вызов статического метода default_info()
Human.default_info()

# 2. Создание объекта Human
person = Human("Алексей", 28)

# 3. Вывод информации о созданном объекте
person.info()  # → Имя: Алексей, Возраст: 28, Дом: Нет дома, Деньги: 0.00 руб.

# 4. Создание объекта SmallHouse
small_home = SmallHouse("ул. Мира, 42", price=2_000_000.0)

# 5. Попробуем купить дом — должно быть предупреждение
person.buy_house(small_home, discount_size=0)

# 6. Поправим финансовое положение
person.earn_money(2_500_000.0)
print("\nПосле заработка:")
person.info()

# 7. Снова попробуем купить дом
print("\n--- Покупка дома ---")
person.buy_house(small_home, discount_size=10)  # 10% скидка → 1 800 000 руб.

# 8. Посмотрим, как изменилось состояние объекта Human
print("\nПосле покупки:")
person.info()
class BankAccount:
    def __init__(self, account_number: str, holder_name: str, balance: float, currency: str, is_active: bool = True):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.currency = currency
        self.is_active = is_active

    def deposit(self, amount: float):
        if not self.is_active:
            print("Ошибка: Счёт неактивен.")
            return
        if amount <= 0:
            print("Ошибка: Сумма должна быть положительной.")
            return
        self.balance += amount
        print(f"Успешно пополнено {amount} {self.currency}. Новый баланс: {self.balance} {self.currency}")

    def withdraw(self, amount: float):
        if not self.is_active:
            print("Ошибка: Счёт неактивен.")
            return
        if amount <= 0:
            print("Ошибка: Сумма должна быть положительной.")
            return
        if amount > self.balance:
            print(f"Ошибка: Недостаточно средств. Доступно: {self.balance} {self.currency}")
            return
        self.balance -= amount
        print(f"Успешно снято {amount} {self.currency}. Остаток: {self.balance} {self.currency}")


account1 = BankAccount(
    account_number="ACC-001",
    holder_name="Анна Иванова",
    balance=1500.0,
    currency="RUB"
)

account2 = BankAccount(
    account_number="ACC-002",
    holder_name="Дмитрий Петров",
    balance=5000.0,
    currency="USD",
    is_active=False
)

print("=== БАНКОВСКИЕ СЧЁТА ===")

print(f"\nСчёт 1: {account1.holder_name}, Баланс: {account1.balance} {account1.currency}, Активен: {account1.is_active}")
print(f"Счёт 2: {account2.holder_name}, Баланс: {account2.balance} {account2.currency}, Активен: {account2.is_active}")

print("\n--- Попытка операций ---")

# Пополнение первого счёта
account1.deposit(500.0)

# Снятие со второго счёта (неактивного)
account2.withdraw(100.0)

# Снятие с первого счёта
account1.withdraw(200.0)

# Попытка снять больше, чем есть
account1.withdraw(3000.0)
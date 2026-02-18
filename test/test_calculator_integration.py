import unittest
from calculator_with_history import CalculatorWithHistory


class TestCalculatorIntegration(unittest.TestCase):

    def setUp(self):
        """
        Метод setUp запускается перед каждым тестом.
        Мы создаем новый экземпляр CalculatorWithHistory, чтобы
        история операций была чистой для каждого теста.
        """
        self.calculator_app = CalculatorWithHistory()

    def test_addition_success_and_history(self):
        """
        Тест 1: Успешное выполнение операции сложения и сохранение её в истории.
        """
        # Вызовите perform_addition(5, 3)
        result = self.calculator_app.perform_addition(5, 3)

        # Проверьте (assert), что возвращённый результат равен 8
        self.assertEqual(result, 8, "Результат сложения должен быть равен 8")

        # Проверьте, что в истории появилась запись "5 + 3 -> 8"
        history = self.calculator_app.get_operation_history()
        self.assertEqual(len(history), 1, "В истории должна быть 1 запись")
        self.assertEqual(history[0], "5 + 3 -> 8", "Запись в истории не совпадает")

    def test_subtraction_success_and_history(self):
        """
        Тест 2: Успешное выполнение операции вычитания и сохранение её в истории.
        """
        # Вызовите perform_subtraction(10, 4)
        result = self.calculator_app.perform_subtraction(10, 4)

        # Проверьте результат (6)
        self.assertEqual(result, 6, "Результат вычитания должен быть равен 6")

        # и запись в истории ("10 - 4 -> 6")
        history = self.calculator_app.get_operation_history()
        self.assertEqual(len(history), 1, "В истории должна быть 1 запись")
        self.assertEqual(history[0], "10 - 4 -> 6", "Запись в истории не совпадает")

    def test_sequential_operations_history(self):
        """
        Тест 3: История содержит несколько записей после последовательных операций.
        """
        # Выполните perform_addition(1, 1)
        self.calculator_app.perform_addition(1, 1)

        # Выполните perform_subtraction(5, 2)
        self.calculator_app.perform_subtraction(5, 2)

        # Получите всю историю через get_operation_history()
        history = self.calculator_app.get_operation_history()

        # Проверьте, что история содержит ровно 2 записи в правильном порядке
        expected_history = ["1 + 1 -> 2", "5 - 2 -> 3"]

        self.assertEqual(len(history), 2, "В истории должно быть ровно 2 записи")
        self.assertEqual(history, expected_history, "Содержимое истории или порядок записей неверны")


if __name__ == '__main__':
    unittest.main()
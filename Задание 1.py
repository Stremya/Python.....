import math

def euler_method(f, x0, y0, n, h):
    """Метод Эйлера"""
    results = []
    x, y = x0, y0
    for i in range(n):
        y_new = y + h * f(x, y)
        x_new = x + h
        results.append((x_new, y_new))
        x, y = x_new, y_new
    return results

def euler_coshi_method(f, x0, y0, n, h):
    """Метод Эйлера-Коши (улучшенный метод Эйлера)"""
    results = []
    x, y = x0, y0
    for i in range(n):
        y1 = y + h * f(x, y)  # предварительная оценка
        x_new = x + h
        y_new = y + h/2 * (f(x, y) + f(x_new, y1))  # уточнение
        results.append((x_new, y_new))
        x, y = x_new, y_new
    return results

def runge_kutta_4_method(f, x0, y0, n, h):
    """Метод Рунге-Кутта 4-го порядка"""
    results = []
    x, y = x0, y0
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_new = x + h
        results.append((x_new, y_new))
        x, y = x_new, y_new
    return results

def print_results(method_name, results):
    """Вывод результатов в виде таблицы"""
    print(f"\n--- {method_name} ---")
    print(f"{'Шаг':<5} {'x':<10} {'y':<15}")
    print("-" * 30)
    for i, (x, y) in enumerate(results, 1):
        print(f"{i:<5} {x:<10.6f} {y:<15.6f}")

def get_function():
    """Получает функцию f(x, y) от пользователя"""
    print("\nВведите функцию f(x, y) в виде строки.")
    print("Например: 'y', 'x + y', 'math.sin(x) * y'")
    func_str = input("f(x, y) = ").strip()
    # Создаем лямбда-функцию из строки
    try:
        # Безопасное выполнение через eval с ограниченным окружением
        allowed_names = {"math": math}
        code = compile(func_str, "<string>", "eval")
        func = lambda x, y: eval(code, {"__builtins__": {}}, {"x": x, "y": y, **allowed_names})
        # Проверяем, что функция работает
        _ = func(0.0, 1.0)
        return func
    except Exception as e:
        print(f"Ошибка при разборе функции: {e}")
        return None

def main():
    print("=== Программа для решения ОДУ ===\n")

    while True:
        print("\nВыберите действие:")
        print("1. Метод Эйлера")
        print("2. Метод Эйлера-Коши")
        print("3. Метод Рунге-Кутта 4-го порядка")
        print("4. Выход")

        choice = input("Ваш выбор (1-4): ").strip()

        if choice == '4':
            print("Выход из программы.")
            break

        if choice not in ['1', '2', '3']:
            print("Неверный выбор. Попробуйте снова.")
            continue

        # Получаем функцию
        f = get_function()
        if f is None:
            continue

        # Получаем параметры
        try:
            x0 = float(input("Введите начальное значение x0: "))
            y0 = float(input("Введите начальное значение y0: "))
            n = int(input("Введите количество шагов n: "))
            h = float(input("Введите шаг h: "))
        except ValueError:
            print("Ошибка ввода данных. Попробуйте снова.")
            continue

        # Выполняем выбранный метод
        if choice == '1':
            results = euler_method(f, x0, y0, n, h)
            method_name = "Метод Эйлера"
        elif choice == '2':
            results = euler_coshi_method(f, x0, y0, n, h)
            method_name = "Метод Эйлера-Коши"
        else:  # choice == '3'
            results = runge_kutta_4_method(f, x0, y0, n, h)
            method_name = "Метод Рунге-Кутта 4-го порядка"

        # Выводим результаты
        print_results(method_name, results)

        # Дополнительно: проверка на тестовом ОДУ y' = y
        if input("\nХотите сравнить с точным решением для y' = y? (y/n): ").lower() == 'y':
            # Точное решение: y = y0 * e^(x - x0)
            exact_solution = lambda x: y0 * math.exp(x - x0)
            print(f"\nТочное решение: y(x) = {y0} * exp(x - {x0})")
            print(f"{'x':<10} {'Численное':<15} {'Точное':<15} {'Погрешность':<15}")
            print("-" * 60)
            for x, y_num in results:
                y_exact = exact_solution(x)
                error = abs(y_num - y_exact)
                print(f"{x:<10.6f} {y_num:<15.6f} {y_exact:<15.6f} {error:<15.6f}")

if __name__ == "__main__":
    main()
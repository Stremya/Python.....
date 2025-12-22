import math

def runge_kutta_4_system(f1, f2, x0, y0, z0, n, h):
    """
    Метод Рунге-Кутта 4-го порядка для системы двух ОДУ.
    Возвращает список кортежей: [(x1, y1, z1), (x2, y2, z2), ...]
    """
    results = []
    x, y, z = x0, y0, z0

    for i in range(n):
        # Вычисляем коэффициенты k1, L1
        k1 = h * f1(x, y, z)
        L1 = h * f2(x, y, z)

        # k2, L2
        k2 = h * f1(x + h/2, y + k1/2, z + L1/2)
        L2 = h * f2(x + h/2, y + k1/2, z + L1/2)

        # k3, L3
        k3 = h * f1(x + h/2, y + k2/2, z + L2/2)
        L3 = h * f2(x + h/2, y + k2/2, z + L2/2)

        # k4, L4
        k4 = h * f1(x + h, y + k3, z + L3)
        L4 = h * f2(x + h, y + k3, z + L3)

        # Новые значения y и z
        y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        z_new = z + (L1 + 2*L2 + 2*L3 + L4) / 6

        # Новый x
        x_new = x + h

        # Сохраняем результат
        results.append((x_new, y_new, z_new))

        # Обновляем текущие значения для следующей итерации
        x, y, z = x_new, y_new, z_new

    return results

def get_function(prompt):
    """Получает функцию от пользователя в виде строки"""
    print(f"\n{prompt}")
    func_str = input().strip()
    try:
        allowed_names = {"math": math}
        code = compile(func_str, "<string>", "eval")
        func = lambda x, y, z: eval(code, {"__builtins__": {}}, {"x": x, "y": y, "z": z, **allowed_names})
        # Проверка
        _ = func(0.0, 1.0, 1.0)
        return func
    except Exception as e:
        print(f"Ошибка при разборе функции: {e}")
        return None

def print_results(results):
    """Выводит результаты в виде таблицы"""
    print(f"\n{'Шаг':<5} {'x':<10} {'y':<15} {'z':<15}")
    print("-" * 50)
    for i, (x, y, z) in enumerate(results, 1):
        print(f"{i:<5} {x:<10.6f} {y:<15.6f} {z:<15.6f}")

def main():
    print("=== Решение системы двух ОДУ методом Рунге-Кутта 4-го порядка ===\n")

    # Получаем функции f1 и f2
    f1 = get_function("Введите функцию f1(x, y, z) (для y'): ")
    if f1 is None:
        return

    f2 = get_function("Введите функцию f2(x, y, z) (для z'): ")
    if f2 is None:
        return

    # Получаем параметры
    try:
        x0 = float(input("\nВведите начальное значение x0: "))
        y0 = float(input("Введите начальное значение y0: "))
        z0 = float(input("Введите начальное значение z0: "))
        n = int(input("Введите количество шагов n: "))
        h = float(input("Введите шаг h: "))
    except ValueError:
        print("Ошибка ввода данных.")
        return

    # Решаем систему
    results = runge_kutta_4_system(f1, f2, x0, y0, z0, n, h)

    # Выводим результаты
    print_results(results)

    # Дополнительно: пример проверки (если система известна)
    if input("\nХотите сравнить с точным решением? (y/n): ").lower() == 'y':
        print("Пример: система y' = z, z' = -y (гармонический осциллятор)")
        print("Точное решение при y0=1, z0=0: y = cos(x), z = -sin(x)")
        if abs(y0 - 1.0) < 1e-6 and abs(z0) < 1e-6:
            print(f"{'x':<10} {'y числен.':<15} {'y точн.':<15} {'z числен.':<15} {'z точн.':<15}")
            print("-" * 80)
            for x, y_num, z_num in results:
                y_exact = math.cos(x)
                z_exact = -math.sin(x)
                print(f"{x:<10.6f} {y_num:<15.6f} {y_exact:<15.6f} {z_num:<15.6f} {z_exact:<15.6f}")

if __name__ == "__main__":
    main()
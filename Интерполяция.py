import numpy as np
from typing import List, Tuple

def lagrange_interpolation(x_values: List[float], y_values: List[float], x: float) -> float:
    """Вычисление значения по формуле Лагранжа"""
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

def newton_forward_interpolation(x_values: List[float], y_values: List[float], x: float) -> float:
    """Интерполяция по формуле Ньютона (вперед) для равноотстоящих узлов"""
    n = len(x_values)
    h = x_values[1] - x_values[0]
    t = (x - x_values[0]) / h

    # Таблица конечных разностей
    diff_table = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        diff_table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    # Формула Ньютона вперед
    result = diff_table[0][0]
    term = 1.0
    for j in range(1, n):
        term *= (t - j + 1) / j
        result += term * diff_table[0][j]

    return result

def build_lagrange_polynomial(x_values: List[float], y_values: List[float]) -> str:
    """Строит строковое представление многочлена Лагранжа (до 4-й степени)"""
    n = len(x_values)
    terms = []
    for i in range(n):
        coeff = y_values[i]
        basis = []
        for j in range(n):
            if i != j:
                basis.append(f"(x - {x_values[j]:.2f})")
        if not basis:
            terms.append(f"{coeff:.2f}")
        else:
            basis_str = " * ".join(basis)
            terms.append(f"{coeff:.2f} * ({basis_str})")
    poly_str = " + ".join(terms)
    return poly_str

def print_finite_differences(x_values: List[float], y_values: List[float], order: int = 3):
    """Печатает таблицу конечных разностей до указанного порядка"""
    n = len(y_values)
    print("\nТаблица конечных разностей:")
    print(f"{'x':<8} {'F(x)':<8}", end="")
    for k in range(1, order + 1):
        print(f" Δ^{k} ", end="")
    print()

    # Вычисляем разности
    diffs = [y_values[:]]
    for k in range(1, order + 1):
        next_diff = []
        for i in range(len(diffs[k-1]) - 1):
            next_diff.append(diffs[k-1][i+1] - diffs[k-1][i])
        diffs.append(next_diff)

    # Печать
    for i in range(n):
        print(f"{x_values[i]:<8.2f} {y_values[i]:<8.4f}", end="")
        for k in range(1, min(order + 1, n - i)):
            if i < len(diffs[k]):
                print(f" {diffs[k][i]:<6.4f}", end="")
            else:
                print("      ", end="")
        print()

def solve_task_1():
    """Задание 1: Составить многочлены Лагранжа для всех подзадач"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 1: МНОГОЧЛЕНЫ ЛАГРАНЖА")
    print("="*60)

    tasks = [
        ("a", [0.48, 0.83], [-0.32, 0.38]),
        ("б", [0.73, 1.44, 2.12], [2.93, 5.42, 9.78]),
        ("в", [1, 3, 5, 6], [4, 3, 2, -3]),
        ("г", [1, 2, 3, 4, 5], [48, 24, 8, 12, 24])
    ]

    for name, x_vals, y_vals in tasks:
        print(f"\n{nome}: x = {x_vals}, F(x) = {y_vals}")
        # Для проверки — вычислим значение в одном из узлов
        test_x = x_vals[0]
        approx = lagrange_interpolation(x_vals, y_vals, test_x)
        print(f"  Проверка: L({test_x}) = {approx:.6f} (должно быть {y_vals[0]})")
        print(f"  Многочлен (формула): {build_lagrange_polynomial(x_vals, y_vals)}")

def solve_task_2():
    """Задание 2: Вычислить значения функции в точках a) x=1.02; б) x=2.34"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 2: ВЫЧИСЛЕНИЕ ЗНАЧЕНИЙ ПО ЛАГРАНЖУ")
    print("="*60)

    x_vals = [0.27, 0.93, 1.46, 2.11, 2.87]
    y_vals = [2.60, 2.43, 2.06, 0.25, -2.60]

    points = [(1.02, 'a'), (2.34, 'б')]
    for x, label in points:
        result = lagrange_interpolation(x_vals, y_vals, x)
        print(f"  F({x}) = {result:.6f} (точка {label})")

def solve_task_3_and_4():
    """Задание 3 и 4: Программа Лагранжа и её применение"""
    print("\n" + "="*60)
    print("ЗАДАНИЯ 3 и 4: ПРОГРАММА ЛАГРАНЖА И ЕЁ ПРИМЕНЕНИЕ")
    print("="*60)

    x_vals = [0.27, 0.93, 1.46, 2.11, 2.87]
    y_vals = [2.60, 2.43, 2.06, 0.25, -2.60]

    points = [1.02, 0.65, 1.28]
    for x in points:
        result = lagrange_interpolation(x_vals, y_vals, x)
        print(f"  F({x}) = {result:.6f}")

def solve_task_5():
    """Задание 5: Конечные разности и многочлен Ньютона"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 5: КОНЕЧНЫЕ РАЗНОСТИ И МНОГОЧЛЕН НЬЮТОНА")
    print("="*60)

    x_vals = [1.25, 1.30, 1.35, 1.40, 1.45, 1.50]
    y_vals = [1.60, 1.71, 1.81, 1.88, 1.94, 1.98]

    print_finite_differences(x_vals, y_vals, order=3)

    # Проверка значений в точках 1.30 и 1.45
    print(f"\nПроверка: F(1.30) = {newton_forward_interpolation(x_vals, y_vals, 1.30):.6f}")
    print(f"Проверка: F(1.45) = {newton_forward_interpolation(x_vals, y_vals, 1.45):.6f}")

def solve_task_6():
    """Задание 6: Программа Ньютона"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 6: ПРОГРАММА ИНТЕРПОЛЯЦИИ ПО НЬЮТОНУ")
    print("="*60)

    x_vals = [1.25, 1.30, 1.35, 1.40, 1.45, 1.50]
    y_vals = [1.60, 1.71, 1.81, 1.88, 1.94, 1.98]

    points = [1.30, 1.45]
    for x in points:
        result = newton_forward_interpolation(x_vals, y_vals, x)
        print(f"  F({x}) = {result:.6f}")

def solve_task_7():
    """Задание 7: Интерполяция натурального логарифма"""
    print("\n" + "="*60)
    print("ЗАДАНИЕ 7: ИНТЕРПОЛЯЦИЯ НАТУРАЛЬНОГО ЛОГАРИФМА")
    print("="*60)

    x_vals = [1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11]
    y_vals = [0.04879, 0.058269, 0.067659, 0.076961, 0.086178, 0.09531, 0.10436]

    print_finite_differences(x_vals, y_vals, order=3)

    points = [1.065, 1.083]
    for x in points:
        result = newton_forward_interpolation(x_vals, y_vals, x)
        true_value = np.log(x)  # Используем numpy для сравнения
        print(f"  ln({x}) ≈ {result:.6f} (по Ньютону), истинное значение: {true_value:.6f}")

# Основной блок
if __name__ == "__main__":
    print("РЕШЕНИЕ ВСЕХ ЗАДАНИЙ ПО ИНТЕРПОЛЯЦИИ")

    solve_task_1()
    solve_task_2()
    solve_task_3_and_4()
    solve_task_5()
    solve_task_6()
    solve_task_7()

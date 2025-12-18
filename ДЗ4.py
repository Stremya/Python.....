# Программа для вычисления интеграла по формуле Гаусса-Лежандра
# Реализация по блок-схеме и примеру

import math

def main():
    print("Программа приближённого вычисления интеграла")
    print("по формуле Гаусса-Лежандра (с автоматическим выбором числа узлов)\n")

    a = float(input("Введите нижний предел a: "))
    b = float(input("Введите верхний предел b: "))
    epsilon = float(input("Введите точность ε: "))

    print("Задайте функцию f(x). Например: x**2, sin(x), exp(x)")
    func_str = input("Введите f(x) в виде строки (например, 'x**2'): ")

    def f(x):
        return eval(func_str, {"x": x, "sin": math.sin,
                               "cos": math.cos,
                               "exp": math.exp,
                               "log": math.log,
                               "pi": math.pi})

    gauss_nodes_weights = {
        2: ([-1/math.sqrt(3), 1/math.sqrt(3)], [1.0, 1.0]),
        4: ([-math.sqrt(3/7 + 2/7*math.sqrt(6/5)), math.sqrt(3/7 + 2/7*math.sqrt(6/5)),
             -math.sqrt(3/7 - 2/7*math.sqrt(6/5)), math.sqrt(3/7 - 2/7*math.sqrt(6/5))],
            [(18 + math.sqrt(30))/36, (18 + math.sqrt(30))/36,
             (18 - math.sqrt(30))/36, (18 - math.sqrt(30))/36]),
    }

    n = 2
    S1 = 0.0

    while True:
        if n not in gauss_nodes_weights:
            n = 4

        nodes, weights = gauss_nodes_weights[n]

        h = (b - a) / 2.0
        integral_sum = 0.0
        for i in range(n):
            x_i = a + h * (1 + nodes[i])
            integral_sum += weights[i] * f(x_i)

        S2 = h * integral_sum

        if abs(S2 - S1) <= 15 * epsilon:
            break

        S1 = S2
        n = 2 * n

    print(f"\nИнтеграл ∫_{a}^{b} f(x) dx ≈ {S2:.8f}")
    print(f"Число узлов: {n}")
    print(f"Оценка погрешности d = |S1 - S2| / 15 = {abs(S1 - S2)/15:.2e}")

if __name__ == "__main__":
    main()
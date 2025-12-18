# Программа для вычисления интеграла по формуле Симпсона с автоматическим выбором шага
# Реализация по блок-схеме Рис. 12.7

def main():
    print("Программа приближённого вычисления интеграла")
    print("по формуле Симпсона с автоматическим выбором шага (Рис. 12.7)\n")

    a = float(input("Введите нижний предел a: "))
    b = float(input("Введите верхний предел b: "))
    epsilon = float(input("Введите точность ε: "))

    print("Задайте функцию f(x). Например: x**2, sin(x), exp(x)")
    func_str = input("Введите f(x) в виде строки (например, 'x**2'): ")

    def f(x):
        return eval(func_str, {"x": x, "sin": __import__('math').sin,
                               "cos": __import__('math').cos,
                               "exp": __import__('math').exp,
                               "log": __import__('math').log})

    n = 2
    S1 = 0.0

    while True:
        h = (b - a) / n
        S = 0.0
        x = a

        N2 = n // 2

        for k in range(N2):
            x1 = x
            x2 = x + h
            x3 = x + 2 * h

            S += (h / 3.0) * (f(x1) + 4 * f(x2) + f(x3))

            x = x3

        if abs(S - S1) <= epsilon:
            break

        S1 = S
        n = 2 * n

    print(f"\nИнтеграл ∫_{a}^{b} f(x) dx ≈ {S:.8f}")
    print(f"Число разбиений: {n}")
    print(f"Точность достигнута: |S - S1| = {abs(S - S1):.2e} ≤ ε = {epsilon}")


if __name__ == "__main__":
    main()
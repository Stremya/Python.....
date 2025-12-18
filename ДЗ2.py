# Программа для вычисления интеграла по формуле левых прямоугольников
# Реализация по блок-схеме Рис. 2.4.2

def main():
    print("Программа приближённого вычисления интеграла")
    print("по формуле левых прямоугольников (Рис. 2.4.2)\n")

    # Ввод данных
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

    n = 5
    I0 = 0.0
    I1 = float('inf')

    while abs(I1 - I0) > epsilon:
        I0 = I1
        n = 2 * n
        h = (b - a) / n

        sum_f = 0.0
        for i in range(n):
            x = a + i * h
            sum_f += f(x)

        I1 = h * sum_f

    print(f"\nИнтеграл ∫_{a}^{b} f(x) dx ≈ {I1:.8f}")
    print(f"Число разбиений: {n}")
    print(f"Точность достигнута: |I1 - I0| = {abs(I1 - I0):.2e} ≤ ε = {epsilon}")

if __name__ == "__main__":
    main()
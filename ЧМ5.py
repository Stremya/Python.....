import math

# Уравнение: (0.2x)^3 - cos(x) = 0
def f(x):
    return (0.2 * x) ** 3 - math.cos(x)

# Метод половинного деления
def bisection(a, b, eps=1e-6):
    if f(a) * f(b) >= 0:
        print("Корня на отрезке нет")
        return None
    while (b - a) > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Метод простых итераций: x = arccos(0.008 * x^3)
def phi(x):
    return math.acos(0.008 * x ** 3)

def simple_iter(x0, eps=1e-6):
    x = x0
    for _ in range(50):
        x_new = phi(x)
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    return x

# Решаем
root1 = bisection(1.5, 1.6, 1e-6)
root2 = simple_iter(1.5, 1e-6)

print(f"Половинное деление: {root1:.6f}")
print(f"Простые итерации:   {root2:.6f}")
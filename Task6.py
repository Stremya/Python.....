import math

def f(x):
    return 2 * x - 5 * math.log(x) - 3

def df(x):
    return 2 - 5 / x

def combined_method(a, b, eps=1e-6):
    if f(a) * f(b) >= 0:
        print("На отрезке нет корня или их несколько")
        return None
    iter_count = 0
    print(f"{'Итерация':<10} {'a':<15} {'b':<15} {'x_h':<15} {'x_t':<15}")
    while abs(b - a) > eps:
        # Хорда
        x_h = a - f(a) * (b - a) / (f(b) - f(a))
        # Касательная
        x_t = b - f(b) / df(b)

        iter_count += 1
        print(f"{iter_count:<10} {a:<15.8f} {b:<15.8f} {x_h:<15.8f} {x_t:<15.8f}")

        # Обновляем границы
        if f(a) * f(x_h) < 0:
            b = x_h
        else:
            a = x_h

        if f(b) * f(x_t) < 0:
            a = x_t
        else:
            b = x_t

    return (a + b) / 2

root = combined_method(0.5, 1.0, 1e-6)
print(f"\nКорень: {root:.8f}")
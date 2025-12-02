import math

def f(x):
    return 2*x - 5*math.log(x) - 3

def chord_method(a, b, eps=1e-3):
    if f(a) * f(b) >= 0:
        print("На отрезке нет корня или их несколько")
        return None
    iter_count = 0
    print(f"{'Итерация':<10} {'x_n':<15} {'f(x_n)':<15} {'|x_n - x_{n-1}|':<15}")
    while True:
        x = a - f(a) * (b - a) / (f(b) - f(a))
        fx = f(x)
        iter_count += 1
        diff = abs(b - a) if iter_count == 1 else abs(x - prev_x)
        print(f"{iter_count:<10} {x:<15.8f} {fx:<15.8f} {diff:<15.8f}")
        if abs(b - a) < eps:
            break
        if f(a) * fx < 0:
            b = x
        else:
            a = x
        prev_x = x
    return x

root = chord_method(0.5, 1.0, 1e-3)
print(f"\nКорень: {root:.8f}")
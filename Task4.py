import math

def f(x):
    return 2*x - 5*math.log(x) - 3

def df(x):
    return 2 - 5/x

def newton_method(x0, eps=1e-6):
    x = x0
    iter_count = 0
    print(f"{'Итерация':<10} {'x_n':<15} {'f(x_n)':<15} {'|x_n - x_{n-1}|':<15}")
    while True:
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            print("Производная близка к нулю!")
            break
        x_new = x - fx / dfx
        diff = abs(x_new - x)
        iter_count += 1
        print(f"{iter_count:<10} {x_new:<15.8f} {f(x_new):<15.8f} {diff:<15.8f}")
        if diff < eps:
            break
        x = x_new
    return x_new

# Начальное приближение
root = newton_method(1.0, 1e-6)
print(f"\nКорень: {root:.8f}")
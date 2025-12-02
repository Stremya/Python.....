import math

def phi(x):
    return x - 0.4 * (x * math.sin(x) - 1)

def simple_iteration(x0, eps=1e-5, max_iter=100):
    print(f"{'Итер':<5} {'x_n':<12} {'|x_n - x_prev|':<15}")
    x_prev = x0
    for i in range(1, max_iter + 1):
        x_new = phi(x_prev)
        diff = abs(x_new - x_prev)
        print(f"{i:<5} {x_new:<12.8f} {diff:<15.8f}")
        if diff < eps:
            return x_new
        x_prev = x_new
    print("Достигнуто макс. число итераций")
    return x_prev

root = simple_iteration(1.1, 1e-5)
print(f"\nКорень ≈ {root:.6f}")
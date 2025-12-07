import numpy as np


def simple_iteration(A, b, eps=1e-4, max_iter=100):
    n = len(b)
    # Проверка диагонального преобладания (упрощённо)
    D = np.diag(np.diag(A))
    R = A - D
    B = -np.linalg.inv(D) @ R
    c = np.linalg.inv(D) @ b

    x = np.zeros(n)
    for i in range(max_iter):
        x_new = B @ x + c
        if np.linalg.norm(x_new - x) < eps:
            return x_new, i + 1
        x = x_new
    print("Не сошлось за", max_iter, "итераций")
    return x, max_iter


# Пример для задания 1
A = np.array([[16.63, -0.24, -6.10],
              [-3.45, -23.13, 1.1],
              [3.76, -8.72, -27.01]])
b = np.array([7.29, -3.41, -8.19])

x, iters = simple_iteration(A, b, 1e-4)
print(f"Корни: {x.round(4)}, итераций: {iters}")
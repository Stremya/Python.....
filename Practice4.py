import numpy as np

def gauss_solve(A, b):
    n = len(b)
    Ab = np.column_stack((A.astype(float), b.astype(float)))
    for i in range(n):
        # Поиск максимального элемента в столбце
        max_row = i
        for k in range(i+1, n):
            if abs(Ab[k,i]) > abs(Ab[max_row,i]):
                max_row = k
        Ab[[i, max_row]] = Ab[[max_row, i]]
        # Обнуление ниже
        for k in range(i+1, n):
            factor = Ab[k,i] / Ab[i,i]
            Ab[k,i:] -= factor * Ab[i,i:]
    # Обратный ход
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i,-1] - np.dot(Ab[i,i+1:n], x[i+1:n])) / Ab[i,i]
    return x

def det_gauss(A):
    n = len(A)
    A = A.astype(float).copy()
    det = 1.0
    for i in range(n):
        max_row = i
        for k in range(i+1, n):
            if abs(A[k,i]) > abs(A[max_row,i]):
                max_row = k
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            det *= -1
        for k in range(i+1, n):
            factor = A[k,i] / A[i,i]
            A[k,i:] -= factor * A[i,i:]
    for i in range(n):
        det *= A[i,i]
    return det

def inverse_gauss(A):
    n = len(A)
    I = np.eye(n)
    AI = np.column_stack((A.astype(float), I))
    for i in range(n):
        max_row = i
        for k in range(i+1, n):
            if abs(AI[k,i]) > abs(AI[max_row,i]):
                max_row = k
        AI[[i, max_row]] = AI[[max_row, i]]
        for k in range(i+1, n):
            factor = AI[k,i] / AI[i,i]
            AI[k,i:] -= factor * AI[i,i:]
    # Обратный ход
    for i in range(n-1, -1, -1):
        AI[i,i:] /= AI[i,i]
        for k in range(i):
            AI[k,i:] -= AI[k,i] * AI[i,i:]
    return AI[:,n:]

# Пример использования:

# Задание 1а
A1a = np.array([[8.39, -8.99, -1.29],
                 [-1.05, 1.89, 4.91],
                 [-6.38, 8.36, 0.48]])
b1a = np.array([8.86, 4.20, -5.06])
x1a = gauss_solve(A1a, b1a)
print("Задание 1а:", x1a.round(3))

# Задание 2а
A2a = np.array([[6.44, 1.90, 0.35],
                 [6.64, 5.24, -8.02],
                 [1.39, -1.00, -0.20]])
det2a = det_gauss(A2a)
print("Задание 2а:", round(det2a, 3))

# Задание 3а
A3a = np.array([[8.47, 4.22, 4.07],
                 [1.49, 6.92, 5.82],
                 [2.42, -0.88, -5.24]])
inv3a = inverse_gauss(A3a)
print("Задание 3а:\n", np.round(inv3a, 4))

# И так далее...
# Программа по интерполяции кубическим сплайном
# Реализует алгоритм из блок-схем Рис. 2.3.4, 2.3.5, 2.3.6

def main():
    n = int(input("Введите количество узлов n (минимум 3): "))
    if n < 3:
        print("Ошибка: n должно быть >= 3")
        return

    print(f"Введите {n} значений x (по возрастанию):")
    x = []
    for i in range(n):
        xi = float(input(f"x[{i}] = "))
        x.append(xi)

    print(f"Введите {n} значений y:")
    y = []
    for i in range(n):
        yi = float(input(f"y[{i}] = "))
        y.append(yi)

    x0 = float(input("Введите точку x0, в которой нужно найти значение сплайна: "))
    h = []
    for i in range(n - 1):
        h.append(x[i + 1] - x[i])

    b = []
    for j in range(n - 2):
        term1 = (y[j + 2] - y[j + 1]) / h[j + 1]
        term2 = (y[j + 1] - y[j]) / h[j]
        b.append(3.0 * (term1 - term2))

    z = [[0.0 for _ in range(n - 2)] for _ in range(n - 2)]
    for j in range(n - 2):
        if j == 0:
            z[0][0] = 2 * (h[0] + h[1])
            if n - 2 > 1:
                z[0][1] = h[1]
        elif j == n - 3:
            z[j][j - 1] = h[j - 1]
            z[j][j] = 2 * (h[j - 1] + h[j])
        else:
            z[j][j - 1] = h[j]
            z[j][j] = 2 * (h[j] + h[j + 1])
            if j + 1 < n - 2:
                z[j][j + 1] = h[j + 1]

    if n == 3:
        t = [b[0] / z[0][0]]
    else:
        alpha = []
        beta = []
        gamma = []
        for i in range(n - 2):
            beta.append(z[i][i])
            if i == 0:
                alpha.append(0.0)
            else:
                alpha.append(z[i][i - 1])
            if i == n - 3:
                gamma.append(0.0)
            else:
                gamma.append(z[i][i + 1])

        c = [0.0] * (n - 2)
        d = [0.0] * (n - 2)
        c[0] = -gamma[0] / beta[0]
        d[0] = b[0] / beta[0]
        for i in range(1, n - 2):
            denom = alpha[i] * c[i - 1] + beta[i]
            if abs(denom) < 1e-12:
                print("Ошибка: система вырождена")
                return
            if i == n - 3:
                c[i] = 0.0
            else:
                c[i] = -gamma[i] / denom
            d[i] = (b[i] - alpha[i] * d[i - 1]) / denom

        t = [0.0] * (n - 2)
        t[n - 3] = d[n - 3]
        for i in range(n - 4, -1, -1):
            t[i] = c[i] * t[i + 1] + d[i]

    t_full = [0.0] + t + [0.0]  # длина = n

    t_coeff = []
    for i in range(n - 1):
        t3 = t_full[i]
        if i < n - 2:
            t4 = (t_full[i + 1] - t_full[i]) / (3.0 * h[i])
        else:
            t4 = 0.0
        t2 = (y[i + 1] - y[i]) / h[i] + h[i] * (t3 - h[i] * h[i] * t4)
        t1 = y[i + 1]
        t_coeff.append([t1, t2, t3, t4])

    k = n - 2
    for i in range(n - 1):
        if x[i] <= x0 <= x[i + 1]:
            k = i
            break
    if x0 < x[0]:
        k = 0
    if x0 > x[n - 1]:
        k = n - 2

    dx = x0 - x[k + 1]
    y0 = (
        t_coeff[k][0]
        + t_coeff[k][1] * dx
        + t_coeff[k][2] * (dx ** 2)
        + t_coeff[k][3] * (dx ** 3)
    )

    print(f"\nЗначение сплайна в точке x0 = {x0} равно: {y0:.6f}")


if __name__ == "__main__":
    print("Программа интерполяции кубическим сплайном")
    print("Реализация по блок-схемам Рис. 2.3.4, 2.3.5, 2.3.6\n")
    main()
    print("\n Готово!")
import numpy as np
import matplotlib.pyplot as plt


def p(x):
    return x ** 5 - 29 * x ** 4 / 20 + 29 * x ** 3 / 36 - 31 * x ** 2 / 144 + x / 36 - 1 / 720


def Newton_findRoot(f, x_0):
    x_cur = x_0
    dx = 1e-10
    while True:
        k = (f(x_cur + dx) - f(x_cur)) / dx
        x_cur = x_cur - f(x_cur) / k
        if abs(f(x_cur)) < 1e-10:
            break
    print("Find root: x = {}".format(x_cur))
    return x_cur


def Secant_findRoot(f, x_0, x_1):
    x_cur = x_1
    x_last = x_0
    while True:
        x_new = x_cur - f(x_cur) * (x_cur - x_last) / (f(x_cur) - f(x_last))
        x_last = x_cur
        x_cur = x_new
        if abs(f(x_cur)) < 1e-10:
            print("Find root: x = {}".format(x_cur))
            return x_cur


def drawPx():
    x = np.linspace(0, 1, 10000)
    plt.plot(x, p(x), 'g')
    plt.title('$The\ graph\ of\ p(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$p(x)$')
    plt.ylim(-1e-5, 1e-5)
    y = [0 for _ in range(10000)]
    plt.plot(x, y, 'blue')
    plt.savefig('Nonlinear/p(x).png')
    plt.show()


def part_1():
    drawPx()


def part_2():
    Newton_findRoot(p, 0.45)


def part_3():
    Secant_findRoot(p, 0, 0.45)


def Main():
    part_2()
    part_3()


if __name__ == '__main__':
    Main()

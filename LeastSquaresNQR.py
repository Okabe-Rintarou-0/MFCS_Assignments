import numpy as np
import matplotlib.pyplot as plt
import LinearAlgebra


def func(x):
    return 1 / (1 + x ** 2)


def check(x, f, A, c, title):
    colors = ["red", "blue", "green"]
    plt.plot(x, f, colors[0], label="predict")
    plt.plot(x, np.dot(A, c), colors[1], label="real")
    M, N = A.shape
    if title == 'F':
        F = LinearAlgebra.formFourierMatrix(M, x)
        c_F = LinearAlgebra.LU_solve(F, f)
        plt.plot(x, np.dot(F, c_F), colors[2], label="interpolation")
    else:
        if title == 'V':
            V = np.vander(x, increasing=True)
            c_V = LinearAlgebra.LU_solve(V, f)
            plt.plot(x, np.dot(V, c_V), colors[2], label="interpolation")
    plt.legend()
    plt.title('$M = {}, N = {}$, Using QR Factorization'.format(M, N))
    plt.savefig('QR/M={}N={}{}'.format(M, N, title))
    plt.show()


def QR_solve(A, f):
    Q, R = np.linalg.qr(A)
    c = np.dot(np.dot(np.linalg.inv(R), np.transpose(Q)), f)
    r = np.dot(A, c) - f
    print("When N = {}:".format(A.shape[1]))
    print("c = ", c)
    print("Residual N2 norm = ", np.linalg.norm(r, ord=2))
    return c


def formV(x, N):
    return np.vander(x, increasing=True)[:, :N]


def formF(M, N, x):
    F = np.zeros((M, N))
    half = N // 2
    for i in range(M):
        for j in range(1, half + 1):
            F[i][j - 1] = np.sin(j * np.pi * x[i])
        for j in range(half + 1, N + 1):
            F[i][j - 1] = np.cos((j - half) * np.pi * x[i])
    return F


def part_1():
    M = 16
    Ns = [4, 8]
    for N in Ns:
        x = np.linspace(0, 1, M)
        f = func(x)
        V = formV(x, N)
        F = formF(M, N, x)
        print("For V:")
        c_V = QR_solve(V, f)
        check(x, f, V, c_V, 'V')
        print("For F:")
        c_F = QR_solve(F, f)
        check(x, f, F, c_F, 'F')


def Main():
    part_1()


if __name__ == '__main__':
    Main()

import numpy as np
from scipy import linalg
from prettytable import PrettyTable
# I choose to use this module to print pretty table
import matplotlib.pyplot as plt


def func(x):
    return 1 / (1 + x ** 2)


def formFourierMatrix(N, x):
    F = np.zeros((N, N))
    half = N // 2
    for i in range(N):
        for j in range(1, half + 1):
            F[i][j - 1] = np.sin(j * np.pi * x[i])
        for j in range(half + 1, N + 1):
            F[i][j - 1] = np.cos((j - half) * np.pi * x[i])
    return F


def LU_solve(A, f):
    P, L, U = linalg.lu(A, permute_l=False)
    b = np.dot(np.linalg.inv(P), f)
    y = np.linalg.solve(L, b)
    c = np.linalg.solve(U, y)
    r = np.dot(A, c) - f
    print("When N = {}:".format(A.shape[0]))
    print("c = ", c)
    print("Residual N2 norm = ", np.linalg.norm(r, ord=2))
    return c


def part_1():
    Ns = [8, 16]
    for N in Ns:
        x = np.linspace(0, 1, N)
        f = func(x)
        V = np.vander(x, increasing=True)
        print("For Vc = f")
        LU_solve(V, f)
        print("For Fc = f")
        F = formFourierMatrix(N, x)
        LU_solve(F, f)


def part_2():
    Ns = [2 * i + 4 for i in range(15)]
    Xs = [np.linspace(0, 1, N) for N in Ns]
    Vs = [np.vander(x, increasing=True) for x in Xs]
    Fs = [formFourierMatrix(Ns[i], Xs[i]) for i in range(15)]
    condVs = [np.linalg.cond(V) for V in Vs]
    condFs = [np.linalg.cond(F) for F in Fs]
    print(condVs)
    print(condFs)
    plt.plot(Ns, condVs, "green", label="$cond(V)$")
    plt.plot(Ns, condFs, "blue", label="$cond(F)$")
    plt.legend()
    plt.yscale('log')
    plt.savefig('./linear algebra/cond.png')
    plt.show()


def Gram(A):  # Transform a matrix A into a Gram Matrix
    return np.dot(np.transpose(A), A)


def is_pos_def(A):
    return np.all(np.linalg.eigvals(A) > 0)


def printRow(row: list):
    for column in row:
        print(column, end="  ")
    print()


def part_3():
    Ns = [2 * i + 4 for i in range(15)]
    Xs = [np.linspace(0, 1, N) for N in Ns]
    Vs = [np.vander(x, increasing=True) for x in Xs]
    Fs = [formFourierMatrix(Ns[i], Xs[i]) for i in range(15)]
    A_Vs = [Gram(V) for V in Vs]
    A_Fs = [Gram(F) for F in Fs]
    tableColumns = ["N", "isposdef(A_V)", "isposdef(A_F)", "cond(V)", "cond(F)"]
    table = PrettyTable(tableColumns)
    tableContents = [[Ns[i], is_pos_def(A_Vs[i]), is_pos_def(A_Fs[i]), np.linalg.cond(Vs[i]), np.linalg.cond(Fs[i])] for
                     i in range(15)]
    table.add_rows(tableContents)
    for row in tableContents:
        printRow(row)
    print(table)


def Cholesky_solve(A, f):
    G = Gram(A)
    b = np.dot(np.transpose(A), f)
    L = np.linalg.cholesky(G)
    y = np.linalg.solve(L, b)
    c = np.linalg.solve(np.transpose(L), y)
    r = np.dot(A, c) - f
    print("When N = {}:".format(A.shape[0]))
    print("c = ", c)
    print("Residual N2 norm = ", np.linalg.norm(r, ord=2))


def part_4():
    N = 8
    x = np.linspace(0, 1, N)
    f = func(x)
    V = np.vander(x, increasing=True)
    F = formFourierMatrix(N, x)
    print("Testing V...")
    print("When using LU Factorization...")
    LU_solve(V, f)
    print("When using Cholesky Factorization...")
    Cholesky_solve(V, f)

    print("Testing F...")
    print("When using LU Factorization...")
    LU_solve(F, f)
    print("When using Cholesky Factorization...")
    Cholesky_solve(F, f)


def Main():
    part_1()
    part_2()
    part_3()
    part_4()
    pass


if __name__ == '__main__':
    Main()

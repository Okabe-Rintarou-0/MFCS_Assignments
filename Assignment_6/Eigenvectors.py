import numpy as np
import matplotlib.pyplot as plt


def formM(N):
    h_minus2 = (N + 1) ** 2
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i][j] = -2
            else:
                if abs(i - j) == 1:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
    return h_minus2 * A


def fi_1(x):
    return np.sqrt(2) * np.sin(np.pi * x)


def Main():
    N = 99
    x = np.linspace(0.01, 0.99, N)
    M = formM(N)
    y = fi_1(x)
    y_2diff = np.dot(M, y)
    kSquarey = -np.pi ** 2 * y
    plt.plot(x, y_2diff, "b.", label="$y''$")
    plt.plot(x, kSquarey, "g.", label=r"$-\pi^2y$")
    plt.legend()
    plt.savefig('Eigenvectors/Helmholtz.png')
    plt.show()


if __name__ == '__main__':
    Main()

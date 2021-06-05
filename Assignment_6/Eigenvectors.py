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


def phi_n(x, n):
    return np.sqrt(2) * np.sin(np.pi * n * x)


def part_1():
    N = 99
    x = np.linspace(0.01, 0.99, N)
    M = formM(N)
    y = phi_n(x, 1)
    y_2diff = np.dot(M, y)
    kSquarey = -np.pi ** 2 * y
    plt.plot(x, y_2diff, "b.", label="$y''$")
    plt.plot(x, kSquarey, "g.", label=r"$-\pi^2y$")
    plt.legend()
    plt.savefig('Eigenvectors/Helmholtz.png')
    plt.show()


def drawPhi(x, vector, phi, phi_expr, save_name, color: str):
    plt.plot(x, phi, color='red', label='${}$'.format(phi_expr))
    plt.plot(x, vector, color, label="$eigenvector$")
    k = np.round(np.mean(phi / vector), 2)
    plt.title(r'$\psi_{{n}}\approx {}eigenvector$'.format(k))
    plt.legend()
    plt.savefig('Eigenvectors/{}'.format(save_name))
    plt.show()


def part_2():
    N = 99
    x = np.linspace(0.01, 0.99, N)
    M = formM(N)
    eigen_values, eigen_vectors = np.linalg.eig(M)
    eigen_vectors = np.transpose(eigen_vectors)
    value_vector_pairs = [(eigen_values[i], eigen_vectors[i]) for i in range(len(eigen_values))]
    sortedPairs = sorted(value_vector_pairs, key=lambda x: (x[0]), reverse=True)
    three_smallest = sortedPairs[0:3]
    phi_expr = '\sqrt{{2}}\sin{{\pi {}x}}'
    colors = ['blue', 'green', 'cyan']
    for i in range(3):
        value, vector = three_smallest[i]
        print("eigenvalue: {}\n".format(value))
        print("eigenvector: {}\n".format(vector))
        if i == 0:
            expr = '\sqrt{2}\sin{\pi x}'
        else:
            expr = phi_expr.format(i + 1)
        drawPhi(x, vector, phi_n(x, i + 1), expr, 'eigen_vector{}'.format(i + 1), colors[i])


def Main():
    part_1()
    part_2()


if __name__ == '__main__':
    Main()

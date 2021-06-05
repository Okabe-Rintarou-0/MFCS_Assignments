import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import cv2


def getImg():
    org = cv2.imread('lena/Lenna.png')
    org_grey = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
    return org_grey


def part_1():
    org_grey = getImg()
    cv2.imshow('origin', org_grey)
    print(org_grey)
    S = np.linalg.svd(org_grey, compute_uv=False)
    print(S)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


def saveImgForDifferentK(k, U, S, V_T):
    out_2 = (U[:, 0:k]).dot(np.diag(S[0:k])).dot(V_T[0:k, :])
    cv2.imwrite('SVD/k = {}.png'.format(k), out_2)
    cv2.waitKey(0)


def part_2():
    org_grey = getImg()
    # cv2.imshow('origin', org_grey)
    U, S, V_T = np.linalg.svd(org_grey)
    ks = [2, 4, 8, 16, 32, 64, 128, len(S)]
    for k in ks:
        saveImgForDifferentK(k, U, S, V_T)
    x = [i for i in range(len(S))]
    x_major_locator = MultipleLocator(50)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.plot(x, S, 'green')
    plt.title('$Singular\ values$')
    plt.ylabel('$value$')
    plt.xlabel('$index$')
    plt.savefig('SVD/singular.png')
    plt.show()


def Main():
    part_2()


if __name__ == '__main__':
    Main()

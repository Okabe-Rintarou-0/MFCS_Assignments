import numpy as np
import matplotlib.pyplot as plt


def gaussianFunc(x, mu, sigma):
    Z = np.sqrt(2 * np.pi) * sigma
    return np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / Z


def drawGaussianDistribution(mu: float, sigma: float, index: int):
    delta = 3 * sigma
    x = np.linspace(mu - delta, mu + delta, 10000)
    y = gaussianFunc(x, mu, sigma)
    plt.plot(x, y, "go")
    plt.savefig('./gaussian/{}.png'.format(index))
    plt.show()


def drawGaussianDistributionTogether(mu: list, sigma: list):
    color = ["red", "green", "blue", "cyan"]
    for i in range(4):
        delta = 3 * sigma[i]
        x = np.linspace(mu[i] - delta, mu[i] + delta, 10000)
        y = gaussianFunc(x, mu[i], sigma[i])
        plt.plot(x, y, color[i], label='$\mu={},\sigma={}$'.format(mu[i], sigma[i]))
    plt.legend()
    plt.savefig('./gaussian/together.png')
    plt.show()


def calcIntegral(begin: float, end: float, mu: float, sigma: float, step: int):
    assert end >= begin
    lengthPerStep = (end - begin) / step
    x = np.linspace(begin, end, step)
    y = gaussianFunc(x, mu, sigma)
    integral = 0.0
    for i in range(step - 1):
        trapezoidArea = lengthPerStep * (y[i] + y[i + 1]) / 2
        integral += trapezoidArea
    print("The integral of this function (mu = {},sigma = {}) is: ".format(mu, sigma), integral)


def Main():
    mu = [0, 1, 5, 10]
    sigma = [1, 2, 0.5, 4]
    for i in range(4):
        drawGaussianDistribution(mu[i], sigma[i], i)
        calcIntegral(mu[i] - 4 * sigma[i], mu[i] + 4 * sigma[i], mu[i], sigma[i], 100000)
    drawGaussianDistributionTogether(mu, sigma)


if __name__ == '__main__':
    Main()

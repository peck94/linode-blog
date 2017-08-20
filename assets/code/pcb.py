import matplotlib.pyplot as plt
from scipy.misc import comb
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def error(N, p, q):
    """
    Compute error probability of the PCB testing algorithm.
    :param N Number of nets in the PCB
    :param p Net probability
    :param q Inter-net probability
    :return Error probability
    """

    p1 = sum([comb(N, i) * math.pow(1-p, i) * math.pow(p, N-i) for i in range(1, N+1)])
    t = int(N*(N-1)/2.0)
    p2 = sum([comb(t, i) * math.pow(1-q, i) * math.pow(q, t-i) for i in range(1, t+1)])

    return p1 + p2

def success(N, p, q):
    return 1 - error(N, p, q)

def plot(N, size=100):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    s = np.linspace(0, 1, size)
    xs, ys, zs = [], [], []
    for p in s:
        for q in s:
            xs.append(p)
            ys.append(q)
            zs.append(success(N, p, q))
    ax.set_xlabel('p')
    ax.set_ylabel('q')
    ax.set_zlabel('success')
    ax.scatter(xs, ys, zs)
    plt.show()

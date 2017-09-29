import numpy as np
from io import StringIO


def get_data():

    with open("tests/test_1") as f:

        K, N = f.readline()[2:-2].split(',')
        K, N = int(K), int(N)

        Q = ''
        for _ in range(K):
            Q += f.readline()
        Q = np.loadtxt(StringIO(Q))

        G = np.empty((N-1, K, K))
        for i in range(N-1):
            f.readline()
            G_str = ''
            for _ in range(K):
                G_str += f.readline()
            G[i] = np.loadtxt(StringIO(G_str))

    return Q, G


Q, G = get_data()
print(Q)
print(G)

import numpy as np
from io import StringIO

import mark_up


def get_data(data_path):

    with open(data_path) as f:

        input_data = f.readline().split(';')[:-1]
        N, K = int(input_data[0][-1]), int(input_data[1][-1])
        gen_add, gen_mult = input_data[2].strip().split(',')

        f.readline()
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

        if gen_add == '+':
            gen_add = np.sum
        elif gen_add == 'or':
            gen_add = np.any
        elif gen_add == 'max':
            gen_add = np.max
        elif gen_add == 'min':
            gen_add = np.min

        if gen_mult == '*':
            gen_mult = np.multiply
        elif gen_mult == '+':
            gen_mult = np.add
        elif gen_mult == 'and':
            gen_mult = np.logical_and
        elif gen_mult == 'min':
            gen_mult = np.minimum
        elif gen_mult == 'max':
            gen_mult = np.maximum

    return gen_add, gen_mult, Q, G


gen_add, gen_mult, Q, G = get_data("tests/test_(max,+)")
# print(gen_add, gen_mult, Q, G, sep='\n')
print(mark_up.mark_up(gen_add, gen_mult, Q, G))

gen_add, gen_mult, Q, G = get_data("tests/test_(or,and)")
print(mark_up.mark_up(gen_add, gen_mult, Q, G))

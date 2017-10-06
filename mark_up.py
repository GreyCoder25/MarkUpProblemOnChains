import numpy as np


def gen_matrix_vector_prod(A, x, gen_add, gen_mult):

    return gen_add(gen_mult(A, x), axis=1)


def mark_up(gen_add, gen_mult, Q, G, Adj_list):

    """
    Parameters
    ----------
    gen_mult : arithmetic function
    Operation that will replace generalized multiplication in current markup task.

    gen_add : arithmetic function
    Operation that will replace generalized addition in current markup task.

    Q : 2-D array
    Matrix of weights of the vertices.

    G : 3-D array
    Array of G-matrices(matrix of the weights of edges between two neighboring objects).

    Adj_list : array of arrays
    Neighborhood structure.

    Returns
    -------
    Generalized sum of all markings.
    """

    n = Q.shape[1]                                              # length of the chain
    for i in range(0, n-1):                              # iterating over objects from n - 1 to 0
        for index, v in enumerate(Adj_list[i]):
            Q[:, v] = gen_mult(Q[:, v], gen_matrix_vector_prod(np.transpose(G[i, index]), Q[:, i], gen_add, gen_mult))
            print(Q[:, v])

    return gen_add(Q[:, n-1])

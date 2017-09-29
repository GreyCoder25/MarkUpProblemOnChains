

def gen_matrix_vector_prod(A, x, gen_add, gen_mult):

    return gen_add(gen_mult(A, x), axis=1)


def mark_up(gen_add, gen_mult, Q, G):

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

    Returns
    -------
    Generalized sum of all markings.
    """

    n = Q.shape[1]                                              # length of the chain
    for i in range(n - 2, -1, -1):                              # iterating over objects from n - 1 to 0
        Q[:, i] = gen_mult(Q[:, i], gen_matrix_vector_prod(G[i], Q[:, i+1], gen_add, gen_mult))
        print(Q[:, i])

    return gen_add(Q[:, 0])

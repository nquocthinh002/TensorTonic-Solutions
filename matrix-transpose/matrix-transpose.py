import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.asarray(A)
    m, n = A.shape
    AT = np.zeros((n, m), dtype=A.dtype)
    for i in range(m):
        for j in range(n):
            AT[j, i] = A[i, j]
    return AT
# extremum_Cython.pyx
import numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def cy_extremum_v3(double[:] x, int side):
    cdef double[:] vec = np.copy(x)
    cdef int n = len(vec)
    cdef int i, j
    cdef double temp, res

    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if vec[j + 1] < vec[j]:
                temp = vec[j + 1]
                vec[j + 1] = vec[j]
                vec[j] = temp

    res = vec[0] if side == 0 else vec[n - 1]
    return res

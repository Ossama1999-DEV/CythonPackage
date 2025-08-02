# extremum.py

import numpy as np

def py_extremum(x, side):
    vec = np.copy(x)
    n = len(vec)

    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if vec[j + 1] < vec[j]:
                temp = vec[j + 1]
                vec[j + 1] = vec[j]
                vec[j] = temp

    res = vec[0] if side == 0 else vec[n - 1]
    return res

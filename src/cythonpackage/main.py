import numpy as np
import time

import sys
import os

import cythonpackage.extremum
from .extremum import cy_extremum_v3, py_extremum

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    # Générer les données
    n = 3000
    rng = np.random.default_rng(seed=2024)
    v = rng.random(size=n)

    # Vérifier que les deux fonctions retournent la même valeur
    py_result = py_extremum(v, 0)
    cy_result = cy_extremum_v3(v, 0)
    print(f"py_extremum result: {py_result}")
    print(f"cy_extremum_v3 result: {cy_result}")

    # Comparer les temps d'exécution
    n_runs = 1000

    start = time.perf_counter()
    for _ in range(n_runs):
        py_extremum(v, 0)
    py_time = (time.perf_counter() - start) / n_runs

    start = time.perf_counter()
    for _ in range(n_runs):
        cy_extremum_v3(v, 0)
    cy_time = (time.perf_counter() - start) / n_runs

    print(f"py_extremum average time: {py_time*1e6:.2f} µs")
    print(f"cy_extremum_v3 average time: {cy_time*1e6:.2f} µs")

if __name__ == "__main__":
    main()

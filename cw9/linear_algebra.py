#!/bin/python3

import numpy as np
import sys
from typing import Tuple
from numpy._typing import NDArray


class matrix:
    m = np.eye(1)

    def __init__(self, m: NDArray[np.float64] = np.eye(2)):
        self.m = m

    def __getitem__(self, pos: Tuple[int, int]) -> float:
        return self.m[pos[0], pos[1]]

    def __add__(self, b: "matrix") -> "matrix":
        D = np.einsum("ik,jk->ik", self.m, b.m)
        # D = np.einsum("...ik,jk->...ik", self.m, b.m) #elipsys
        # ("ik,jl->ijkl") # Kronecker
        return matrix(D)

    def __at__(self):
        pass


if __name__ == "__main__":
    n = int(sys.argv[1])
    A = np.random.randn(n, n) + 1j * np.random.randn(n, n)
    print(A)

    m = matrix()
    print(m[1, 1])

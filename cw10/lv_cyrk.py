#!/bin/python3
# %%
import numpy as np
from CyRK import nbsolve_ivp
import matplotlib.pyplot as plt
from numba import njit


@njit
def f(t, vector, *args) -> np.ndarray:
    """
    dx/dt = v
    dv/dt = -G/L
    """
    x = vector[0]
    y = vector[1]
    a, b, c, d = args

    return np.array([(a - b * y) * x, (-c + d * x) * y], dtype=np.float64)


def simulate(a=0.5, b=0.02, c=0.4, d=0.01, x0=50, y0=3, t_max=140, n_eval=1000):
    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, n_eval)
    sol = nbsolve_ivp(
        f,
        t_span=t_span,
        y0=np.array([x0, y0]),
        args=(a, b, c, d),
        t_eval=t_eval,
        warnings=False,
    )

    x = sol.y[0]
    v = sol.y[1]

    # Plot results
    plt.plot(sol.t, x, label="x(t)")
    plt.plot(sol.t, v, label="y(t)")
    plt.xlabel("t")
    plt.ylabel("Solution")
    plt.legend()
    plt.grid()
    plt.show()


# simulate()

# %%
import sys

if __name__ == "__main__":
    if len(sys.argv) < 7:
        simulate()
    else:
        arg = (
            float(sys.argv[1]),
            float(sys.argv[2]),
            float(sys.argv[3]),
            float(sys.argv[4]),
            int(sys.argv[5]),
            int(sys.argv[6]),
            int(sys.argv[7]),
            int(sys.argv[8]),
        )

        simulate(*arg)
# %%

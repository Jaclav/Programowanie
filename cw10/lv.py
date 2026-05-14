#!/bin/python3
# %%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import scipy.constants as cs


def simulate(a=1.44, b=0.3, c=0.5, d=0.5, x0=1, y0=1, t_max=100, n_eval=10000):
    def f(t, vector):
        """
        dx/dt = v
        dv/dt = -G/L
        """
        x = vector[0]
        y = vector[1]

        return [(a - b * y) * x, (-c + d * x) * y]

    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, n_eval)
    sol = solve_ivp(f, t_span, [x0, y0], method="RK45", t_eval=t_eval)

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

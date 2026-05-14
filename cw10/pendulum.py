#!/bin/python3
# %%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import scipy.constants as cs


def simulate(
    l: float = 1,
    theta_0: float = np.deg2rad(5),
    omega_0: float = np.deg2rad(5),
    t_max: float = 10,
    n_max: int = 100,
    method: str = "RK45",
):
    g = cs.g
    print(l, theta_0, omega_0, t_max, n_max)

    def f(t, vector):
        """
        dx/dt = v
        dv/dt = -G/L
        """
        x = vector[0]
        v = vector[1]

        return [v, -g / l * np.sin(x)]

    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, n_max)
    sol = solve_ivp(f, t_span, [theta_0, omega_0], method=method, t_eval=t_eval)

    x = sol.y[0]
    v = sol.y[1]

    # Plot results
    plt.plot(sol.t, x, label="x(t)")
    plt.plot(sol.t, v, label="v(t)")
    plt.xlabel("t")
    plt.ylabel("Solution")
    plt.legend()
    plt.grid()
    plt.show()


# simulate()

# %%
import sys

if __name__ == "__main__":
    l, theta_0, omega_0, t_max, n_max = (
        float(sys.argv[1]),
        float(sys.argv[2]),
        float(sys.argv[3]),
        float(sys.argv[4]),
        int(sys.argv[5]),
    )

    print(l, theta_0, omega_0, t_max, n_max)
    if len(sys.argv) > 6:
        method = sys.argv[6]
        simulate(l, theta_0, omega_0, t_max, n_max, method)
    else:
        simulate(l, theta_0, omega_0, t_max, n_max)
# %%

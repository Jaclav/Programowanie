import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

T0 = [70, 70, 70, 0]

plate = np.zeros((50, 50))
plate[:, 0] = T0[0]
plate[:, -1] = T0[2]
plate[0, :] = T0[3]
plate[-1, :] = T0[1]

fig, ax = plt.subplots()
line = ax.imshow(plate.T, "hot")
fig.colorbar(line)


def new_laplace(tab):
    return tab[2:, 1:-1] + tab[:-2, 1:-1] + tab[1:-1, 2:] + tab[1:-1, :-2]


def update(frame):
    global plate

    flat = new_laplace(plate)
    plate[1:-1, 1:-1] = 0.25 * flat

    ax.set_title(str(frame))
    line.set_data(plate.T)

    return line


ani = animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=30)  # type: ignore
plt.show()

#!/bin/python3
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-s", "--square", type=float, metavar="A", help="Kwadrat o boku A")
group.add_argument(
    "-r",
    "--rectangle",
    type=int,
    metavar=("A", "B"),
    help="Prostokąt o bokach A, B",
    nargs=2,
)
group.add_argument(
    "-e",
    "--elipse",
    type=int,
    metavar=("A", "B"),
    help="Elipsa o półosiach A, B",
    nargs=2,
)

parser.add_argument(
    "-m",
    "--matrix-size",
    type=int,
    metavar=("A", "B"),
    help="wymiary macierzy",
    nargs=2,
    required=True,
)

parser.add_argument(
    "-c",
    "--color",
    type=int,
    metavar=("R", "G", "B"),
    help="kolor",
    nargs=3,
    required=True,
)

parser.add_argument(
    "-n",
    "--filter-size",
    type=int,
    metavar=("n"),
    help="kolor",
    required=True,
)


class Shape:
    matrix_size = [0, 0]

    def __init__(self, m):
        self.matrix_size = m

    def draw(self, x, y):
        raise NotImplemented


class Square(Shape):
    a: int

    def __init__(self, m, a):
        super().__init__(m)
        self.a = a

    def draw(self, x, y):
        return ((x - self.matrix_size[0] // 2) ** 2 <= (self.a // 2) ** 2) * (
            (y - self.matrix_size[1] // 2) ** 2 <= (self.a // 2) ** 2
        )


class Rectangle(Shape):
    pass


class Ellipse(Shape):
    pass


args = parser.parse_args()
print(args)
plain = np.zeros((args.matrix_size[0], args.matrix_size[1]))

if args.square is not None:
    sh = Square(args.matrix_size, args.square)
    plain = np.fromfunction(sh.draw, plain.shape, dtype=float)


def color_shape(shape_matrix, color, n):

    sum = np.zeros(shape_matrix.shape)

    sum += np.roll(shape_matrix, n, axis=0)
    sum += np.roll(shape_matrix, n, axis=1)

    sum /= (2 * n) ** 2
    # print(sum)
    C = np.einsum("ij,k->ijk", sum, color)
    print(C)

    return C.astype(np.uint8)


plt.imshow(color_shape(plain, args.color, args.filter_size))
plt.show()

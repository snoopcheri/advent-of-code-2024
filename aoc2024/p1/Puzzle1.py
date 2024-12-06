import numpy as np
from aoc2024.common import FileUtils as fu


def solve():
    data = fu.read_matrix("p1/input.txt")

    col1 = data[:, 0]
    col1.sort()

    col2 = data[:, 1]
    col2.sort()

    diff = np.absolute(col1 - col2)
    sum = np.sum(diff)

    print(sum)

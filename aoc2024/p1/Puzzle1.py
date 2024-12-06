import numpy as np
from aoc2024.common import FileUtils as fu


def solve1():
    data = fu.read_matrix("p1/input.txt")

    col1 = np.sort(data[:, 0])
    col2 = np.sort(data[:, 1])

    diff = np.absolute(col1 - col2)
    result = np.sum(diff)

    print(result)


def solve2():
    data = fu.read_matrix("p1/input.txt")

    col1 = data[:, 0]
    col2 = data[:, 1]

    result = 0
    for n in np.nditer(col1):
        result += n * np.where(col2 == n)[0].size

    print(result)

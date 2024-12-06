import numpy
import numpy as np
from numpy import ndarray

from aoc2024.common import FileUtils as fu

def solve1():
    reports = fu.read_irregular_matrix("p2/input.txt")
    print(reports)

    # Axis 0 is vertical, axis 1 is horizontal
    result = np.apply_along_axis(is_safe, 1, reports).sum()
    print(result)

def is_safe(report: ndarray):
    report = report[~numpy.isnan(report)].astype(int)

    increasing = np.sort(report)
    decreasing = increasing[::-1]

    if not np.array_equal(report, increasing) and not np.array_equal(report, decreasing):
        return False

    diffs = np.absolute(np.diff(report))
    if np.min(diffs) < 1 or np.max(diffs) > 3:
        return False

    return True

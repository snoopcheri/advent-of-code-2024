from aoc2024.common import FileUtils as fu

import numpy as np
import re

def solve1():
    lines = fu.read_lines("p3/input.txt")

    result = sum([evalLine(line) for line in lines])
    print(result)


def evalLine(line: str) -> int:
    pattern = re.compile('mul\\(\\d{1,3},\\d{1,3}\\)')
    matches = pattern.findall(line)

    return sum([evalExpr(match) for match in matches])


def evalExpr(expr: str) -> int:
    mul_expr = re.compile('mul\\((\\d{1,3}),(\\d{1,3}).*')
    match = mul_expr.match(expr)

    a = int(match.group(1))
    b = int(match.group(2))

    return a * b

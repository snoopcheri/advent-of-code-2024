from aoc2024.common import FileUtils as fu

import re

def solve1():
    lines = fu.read_lines("p3/input.txt")
    result = sum([eval_line(line) for line in lines])
    print(result)


def eval_line(line: str) -> int:
    pattern = re.compile('mul\\(\\d{1,3},\\d{1,3}\\)')
    matches = pattern.findall(line)

    return sum([eval_expr(match) for match in matches])


def eval_expr(expr: str) -> int:
    mul_expr = re.compile('mul\\((\\d{1,3}),(\\d{1,3}).*')
    match = mul_expr.match(expr)

    a = int(match.group(1))
    b = int(match.group(2))

    return a * b


def solve2():
    lines = fu.read_lines("p3/input.txt")

    result = 0
    do_eval = True
    for line in lines:
        val = eval_line_sophisticated(line, do_eval)
        result += val[0]
        do_eval = val[1]

    print(result)

def eval_line_sophisticated(line: str, do_eval_initially: bool) -> (int, bool):
    pattern = re.compile('(mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don\'t\\(\\))')
    matches = pattern.findall(line)

    sum = 0
    do_eval = do_eval_initially

    for match in matches:
        if match == "do()":
            do_eval = True
        elif match == "don't()":
            do_eval = False
        else:
            if do_eval:
                sum += eval_expr(match)

    return sum, do_eval
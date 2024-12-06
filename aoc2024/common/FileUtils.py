import numpy as np
from typing import List


def read_lines(file_name: str) -> List[str]:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def read_matrix(file_name: str) -> np.ndarray:
    return np.loadtxt(file_name, dtype=int)

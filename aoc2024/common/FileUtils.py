import numpy as np
from typing import List
import pandas as pd


def read_lines(file_name: str) -> List[str]:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


def read_matrix(file_name: str) -> np.ndarray:
    return np.loadtxt(file_name, dtype=int)


# The function returns a proper NxN matrix, but contains `None` for missing values
# at the end of each row. Additionally, the values are stored as floats.
def read_irregular_matrix(file_name: str) -> np.ndarray:
    df = pd.DataFrame([line.strip().split() for line in open(file_name, 'r')])
    return df.to_numpy().astype(float)

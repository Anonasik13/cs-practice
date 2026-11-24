import numpy as np


def make_table(rows: int, columns: int) -> list[list[int]]:
    arr = np.arange(rows * columns).reshape(rows, columns)
    return arr.tolist()


def rectangle(matrix: list[list[float]], row_start: int, row_stop: int,
              column_start: int, column_stop: int) -> list[list[float]]:
    arr = np.asarray(matrix, dtype=float)
    return arr[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int,
                      column_start: int, column_stop: int,
                      value: float) -> list[list[float]]:
    arr = np.asarray(matrix, dtype=float).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()


def matrix_vector_product(matrix: list[list[float]],
                          vector: list[float]) -> list[float]:
    arr = np.asarray(matrix, dtype=float)
    vec = np.asarray(vector, dtype=float)
    return (arr @ vec).tolist()


def matrix_multiply(left: list[list[float]],
                    right: list[list[float]]) -> list[list[float]]:
    left_arr = np.asarray(left, dtype=float)
    right_arr = np.asarray(right, dtype=float)
    return (left_arr @ right_arr).tolist()


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    arr = np.asarray(matrix, dtype=float)
    return arr.T.tolist()


def solve_system(matrix: list[list[float]],
                 vector: list[float]) -> list[float]:
    arr = np.asarray(matrix, dtype=float)
    vec = np.asarray(vector, dtype=float)
    solution = np.linalg.solve(arr, vec)
    return [round(float(value), 6) for value in solution]


def tensor_channel_mean(tensor: list) -> list:
    arr = np.asarray(tensor, dtype=float)
    return arr.mean(axis=-1).tolist()


def point_distance(first: list[float], second: list[float]) -> float:
    first_arr = np.asarray(first, dtype=float)
    second_arr = np.asarray(second, dtype=float)
    distance = np.linalg.norm(first_arr - second_arr)
    return round(float(distance), 6)

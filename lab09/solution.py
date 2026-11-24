"""Lab09: NumPy vectors — slices, one mask, vectorized arithmetic."""

import numpy as np


def make_hours() -> list[int]:
    """Vector of hours: 0 to 21 with step 3."""
    return np.arange(0, 22, 3).tolist()


def vector_report(values: list[float]) -> dict:
    """Third element, last element, slice 2:6, every second, reversed."""
    arr = np.asarray(values, dtype=float)
    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }


def change_vector(values: list[float]) -> list[float]:
    """Copy: indices 2-4 -> 99, then every second element -> -1."""
    arr = np.asarray(values, dtype=float).copy()
    arr[2:5] = 99
    arr[::2] = -1
    return arr.tolist()


def cap_above(values: list[float], limit: float) -> list[float]:
    """One mask: everything above limit becomes limit."""
    arr = np.asarray(values, dtype=float).copy()
    arr[arr > limit] = limit
    return arr.tolist()


def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    """Whole vector at once: C * 9 / 5 + 32."""
    arr = np.asarray(values, dtype=float)
    return (arr * 9 / 5 + 32).tolist()

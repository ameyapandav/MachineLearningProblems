import numpy as np


def smoothed_probabilities(counts: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    """
    Add-alpha smoothing. Returns an array of the same shape whose rows
    each sum to 1: (counts + alpha) / (row total + alpha * V).
    """
    # TODO: Add alpha, then normalise each row.

    smoothed = counts + alpha

    row_sums = smoothed.sum(axis=1, keepdims = True)
    return smoothed / row_sums
    pass

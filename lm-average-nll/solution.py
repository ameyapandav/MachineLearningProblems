import numpy as np


def average_nll(words: list[str], probs: np.ndarray, itos: list[str]) -> float:
    """
    Mean negative log-probability (natural log) of every adjacent pair of
    the words, each wrapped as '.' + word + '.'.
    """
    # TODO: Collect row/column indices of all pairs, look up probs, average.

    stoi = {s: i for i, s in enumerate(itos)}

    rows = []
    cols = []

    for word in words:
        wrapped = "." + word + "."

        for ch1, ch2 in zip(wrapped, wrapped[1:]):
            rows.append(stoi[ch1])
            cols.append(stoi[ch2])

    pair_probs = probs[rows, cols]

    nll = -np.log(pair_probs)
    return float(np.mean(nll))
    
    pass

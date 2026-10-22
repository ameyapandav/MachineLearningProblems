import numpy as np


def bigram_counts(words: list[str]) -> tuple[np.ndarray, list[str]]:
    """
    Returns (counts, itos). `itos` is ['.'] plus the sorted distinct
    characters of all words. counts[i, j] is how often itos[j] directly
    followed itos[i] when every word is wrapped as '.' + word + '.'.
    """
    # TODO: Build itos and a symbol -> index map.
    # TODO: Walk the adjacent pairs of each wrapped word and count them.

    chars = sorted(list(set("".join(words))))

    itos = ["."] + chars
    stoi = {s: i for i, s in enumerate(itos)}
    V = len(itos)

    counts = np.zeros((V,V), dtype=int)

    for w in words:
        wrapped = "." + w + "."
        for ch1, ch2 in zip(wrapped, wrapped[1:]):
            i = stoi[ch1]
            j = stoi[ch2]
            counts[i,j] += 1

    return counts, itos;        
    pass

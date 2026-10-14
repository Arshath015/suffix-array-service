import numpy as np
from typing import List

def build_suffix_array(s: str) -> np.ndarray:
    """Construct the suffix array of *s* using the O(n log n) doubling algorithm.

    Parameters
    ----------
    s: str
        Input string (treated as a sequence of characters).

    Returns
    -------
    np.ndarray
        1‑D array of start indices of suffixes in lexicographic order.
    """
    n = len(s)
    if n == 0:
        return np.array([], dtype=np.int32)
    # initial ranking by single character
    rank = np.fromiter((ord(c) for c in s), dtype=np.int32)
    tmp = np.empty_like(rank)
    sa = np.arange(n, dtype=np.int32)
    k = 1
    while True:
        # key: (rank[i], rank[i+k] if i+k < n else -1)
        key2 = np.where(sa + k < n, rank[sa + k], -1)
        # stable sort by second key then first key
        idx = np.lexsort((key2, rank[sa]))
        sa = sa[idx]
        tmp[sa[0]] = 0
        for i in range(1, n):
            prev, cur = sa[i - 1], sa[i]
            prev_key = (rank[prev], rank[prev + k] if prev + k < n else -1)
            cur_key = (rank[cur], rank[cur + k] if cur + k < n else -1)
            tmp[cur] = tmp[prev] + (prev_key != cur_key)
        rank, tmp = tmp, rank
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa

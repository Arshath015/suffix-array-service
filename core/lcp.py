import numpy as np
from typing import List

def build_lcp_array(s: str, sa: np.ndarray) -> np.ndarray:
    """Compute the LCP array for *s* given its suffix array *sa* using Kasai's algorithm.

    Parameters
    ----------
    s: str
        Original string.
    sa: np.ndarray
        Suffix array as returned by ``build_suffix_array``.

    Returns
    -------
    np.ndarray
        LCP array where lcp[i] = longest common prefix length of suffixes
        sa[i] and sa[i-1]; lcp[0] is defined as 0.
    """
    n = len(s)
    if n == 0:
        return np.array([], dtype=np.int32)
    rank = np.empty(n, dtype=np.int32)
    for i, suffix_idx in enumerate(sa):
        rank[suffix_idx] = i
    lcp = np.zeros(n, dtype=np.int32)
    h = 0
    for i in range(n):
        r = rank[i]
        if r == 0:
            h = 0
            continue
        j = sa[r - 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[r] = h
        if h > 0:
            h -= 1
    return lcp

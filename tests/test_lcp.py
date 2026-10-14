import numpy as np
from core.sa import build_suffix_array
from core.lcp import build_lcp_array

def test_lcp_basic():
    s = "banana"
    sa = build_suffix_array(s)
    lcp = build_lcp_array(s, sa)
    expected = np.array([0, 1, 3, 0, 0, 2], dtype=np.int32)
    assert np.array_equal(lcp, expected)

def test_lcp_edge_cases():
    # empty string
    assert build_lcp_array("", np.array([], dtype=np.int32)).size == 0
    # single character
    sa = build_suffix_array("a")
    lcp = build_lcp_array("a", sa)
    assert np.array_equal(lcp, np.array([0], dtype=np.int32))

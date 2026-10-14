import numpy as np
from core.sa import build_suffix_array

def test_sa_basic():
    s = "banana"
    expected = np.array([5, 3, 1, 0, 4, 2], dtype=np.int32)
    assert np.array_equal(build_suffix_array(s), expected)

def test_sa_empty():
    assert build_suffix_array("").size == 0

def test_sa_single_char():
    assert np.array_equal(build_suffix_array("a"), np.array([0], dtype=np.int32))

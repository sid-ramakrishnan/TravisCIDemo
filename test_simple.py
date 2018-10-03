from __future__ import division
import numpy as np
import io
import os


def test_simple():
    assert(2/8 == 0.25 and np.array([2])/np.array([8])==np.array([0.25]))
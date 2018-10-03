from __future__ import division
import numpy as np
import io
import os


def test_simple_division():
    assert(2/8 == 0.25) 

def test_numpy_division():
	assert np.array([2])/np.array([8]) == 0.25


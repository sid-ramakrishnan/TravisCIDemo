from __future__ import division
import numpy as np
import io
import os


def test_simple_division():
    assert (2/8 == 0.25)

def test_input_size():
    f=open("input.txt","rb")
    char=f.readline().strip().decode("utf-8")
    assert len(char)==6

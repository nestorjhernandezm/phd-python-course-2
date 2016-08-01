# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:00:39 2016

@author: nestor
"""

import scipy as sp
import matplotlib.pyplot as plt


def linear_mapping(c, I=100, threshold=10):
    z = 0
    for i in range(I):
        z = z ** 2 + c
        if (abs(z) > threshold):
            return float(i + 1) / I

    return 1

x = sp.arange(-2, 1, 0.1)
y = sp.arange(-1.5, 1.5, 0.1)
Real_c, Imaginary_c = sp.meshgrid(x, y, sparse=True)

for re, im in Real_c, Imaginary_c:
    print re, im
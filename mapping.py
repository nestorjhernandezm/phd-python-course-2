# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:00:39 2016

@author: nestor
"""

import scipy as sp


def linear_mapping(c, I=100, threshold=10):
    z = 0
    for i in range(I):
        z = z ** 2 + c
        if (abs(z) > threshold):
            return float(i + 1) / I

    return 1

points = 10
xmin = -2
xmax = 1
ymin = -1.5
ymax = 1.5

x = sp.linspace(xmin, xmax, points)
y = sp.linspace(ymin, ymax, points)
Real_c, Imaginary_c = sp.meshgrid(x, y, sparse=True)
z = [linear_mapping(complex(re, im)) for re in x for im in y]

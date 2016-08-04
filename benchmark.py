# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:44:57 2016

@author: nestor
"""

"""
Code to call all our different functions and a basis for possible
profiling

"""

import numpy as np
import time

import mandelbrot as mnb

methods = ['mnb.mandelbrot_set_naive(Re_c, Im_c)',
           'mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)',
            ]

points = 500

# Real and imaginary axis
Re_c = np.linspace(-2, 1, points)  # (xmin, xmax, points)
Im_c = np.linspace(-1.5, 1.5, points)  # (ymin, ymax, points)
Real_c, Imaginary_c = np.meshgrid(Re_c, Im_c)

print('Points per axis = {}'.format(points))
for m in methods:
    tic = time.time()
    y = eval(m)
    toc = time.time() - tic

    print('{:30s} : {:10.2e} [s]'.format(m, toc))

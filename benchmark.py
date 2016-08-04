# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:44:57 2016

@author: nestor
"""

"""
Code to call all our different functions and a basis for possible
profiling

"""

import scipy as sp
import time

import mandelbrot as mnb

methods = ['mnb.mandelbrot_set_naive(Re_c, Im_c)',
           'mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)']

# Input parameters
points = 1000
xmin = -2
xmax = 1
ymin = -1.5
ymax = 1.5

# Real and imaginary axis
Re_c = sp.linspace(xmin, xmax, points)
Im_c = sp.linspace(ymin, ymax, points)
Real_c, Imaginary_c = sp.meshgrid(Re_c, Im_c)

print('Points per axis = {}'.format(points))
for m in methods:
    tic = time.time()
    y = eval(m)
    toc = time.time() - tic

    print('{:30s} : {:10.2e} [s]'.format(m, toc))

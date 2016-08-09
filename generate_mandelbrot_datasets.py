# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 18:58:40 2016

@author: nestor
"""
import sys
from mandelbrot_c import mandelbrot_set_cython
import numpy as np
import mandelbrot as mnb

# Input parameters
points = 5000

# Real and imaginary axis
Re_c = np.linspace(-2, 1, points)  # (xmin, xmax, points)
Im_c = np.linspace(-1.5, 1.5, points)  # (ymin, ymax, points)
Real_c, Imaginary_c = np.meshgrid(Re_c, Im_c)

# Mandelbrot set computations
M_naive = mnb.mandelbrot_set_naive(Re_c, Im_c)
print 'Naive implementation computed'
M_vectorized = mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)
print 'Vectorized implementation computed'
M_cython = mandelbrot_set_cython(Real_c + 1j * Imaginary_c)
print 'Cython implementation computed'
M_numba = mnb.mandelbrot_set_numba(Re_c, Im_c)
print 'Numba implementation computed'

cores = int(sys.argv[1])
M_multiprocessing = mnb.mandelbrot_set_multiprocessing(Real_c, Imaginary_c,
                                                       cores)
print 'Multiprocessing implementation computed'

datasets = {'naive': M_naive,
            'vectorized': M_vectorized,
            'cython': M_cython,
            'numba': M_numba,
            'multiprocessing': M_multiprocessing
            }

print 'Saving data...'
np.savez('./mandelbrot_axis.npz', Real_c=Real_c, Imaginary_c=Imaginary_c)

for implementation in datasets.keys():
    np.savez('./mandelbrot_' + implementation + '_data.npz',
             M=datasets[implementation])
print 'Data saved'

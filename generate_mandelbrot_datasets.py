# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:58:40 2016

@author: nestor
"""

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
M_vectorized = mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)
M_cython = mandelbrot_set_cython(Real_c + 1j * Imaginary_c)
#M_numba = mnb.mandelbrot_set_numba(Re_c, Im_c)

cores = 2
M_multiprocessing = mnb.mandelbrot_set_multiprocessing(Real_c, Imaginary_c,
                                                       cores)

np.savez('./mandelbrot_datasets.npz',
         Re_c=Re_c, Im_c=Im_c, Real_c=Real_c, Imaginary_c=Imaginary_c,
         M_naive=M_naive, M_vectorized=M_vectorized, M_cython=M_cython,
#         M_numba=M_numba, M_multiprocessing=M_multiprocessing)
         M_multiprocessing=M_multiprocessing)

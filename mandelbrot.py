# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:00:39 2016

@author: nestor
"""

import numpy as np
from numba import jit


def naive_mapping(c, I=100, threshold=10):
    z = 0

    for i in range(I):
        z = z ** 2 + c
        if (abs(z) > threshold):
            return float(i + 1) / I

    return 1


#@profile
def mandelbrot_set_naive(Re_c, Im_c):
    Re_c_size = len(Re_c)
    Im_c_size = len(Im_c)
    M = np.zeros([Re_c_size, Im_c_size])

    for i in range(Re_c_size):
        for j in range(Im_c_size):
            M[i, j] = naive_mapping(complex(Re_c[i] + 1j * Im_c[j]))

    return M.T  # Just to plot properly later


#@profile
def mandelbrot_set_vectorized(C, I=100, threshold=10):
    iterations = np.zeros(C.shape)
    z = np.zeros(C.shape, np.complex64)

    for i in range(I):
        not_done = z.real ** 2 + z.imag ** 2 < threshold ** 2
        iterations[not_done] = i
        z[not_done] = z[not_done] ** 2 + C[not_done]

    iterations = (iterations + 1) / I
    iterations[iterations == I] = 0
    return iterations


@jit
def numba_mapping(c, I=100, threshold=10):
    z = 0

    for i in range(I):
        z = z ** 2 + c
        if (abs(z) > threshold):
            return float(i + 1) / I

    return 1


@jit
def mandelbrot_set_numba(Re_c, Im_c):
    Re_c_size = len(Re_c)
    Im_c_size = len(Im_c)
    M = np.zeros([Re_c_size, Im_c_size])

    for i in range(Re_c_size):
        for j in range(Im_c_size):
            M[i, j] = numba_mapping(complex(Re_c[i] + 1j * Im_c[j]))

    return M.T  # Just to plot properly later

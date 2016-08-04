# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:06:35 2016

@author: nestor
"""

# miniproject_mandelbrot.pyx
import numpy as np
cimport cython


def mandelbrot_set_cython(C, I=100, threshold=10):
    """
    Calculate the Mandelbrot set in a vectorized manner

    Input:
    C: Set of complex64 numbers for which the Mandelbrot set is going
    to be computed

    Output:
    M: Array of values indicating the stability of the calculated points
    """
    iterations = np.zeros(C.shape)
    z = np.zeros(C.shape, np.complex64)

    for i in range(I):
        not_done = z.real ** 2 + z.imag ** 2 < threshold ** 2
        iterations[not_done] = i
        z[not_done] = z[not_done] ** 2 + C[not_done]

    iterations = (iterations + 1) / I
    iterations[iterations == I] = 0
    return iterations

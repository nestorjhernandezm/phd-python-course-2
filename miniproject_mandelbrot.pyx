# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:06:35 2016

@author: nestor
"""

# miniproject_mandelbrot.pyx
import numpy as np
cimport numpy as np
cimport cython
ctypedef np.complex_t dtype_t


@cython.boundscheck(False)
@cython.wraparound(False)
def mandelbrot_set_cython(np.ndarray[dtype_t, ndim=2] C):
    """
    Calculate the Mandelbrot set in a vectorized manner

    Input:
    C: Set of complex numbers for which the Mandelbrot set is going
    to be computed

    Output:
    iterations: Array of double values indicating the stability of the
    calculated points
    """
    cdef int I = 100
    cdef int threshold = 10
    cdef int n = C.shape[0]
    cdef np.ndarray[double, ndim=2] iterations = np.zeros((n, n))
    cdef np.ndarray[dtype_t, ndim=2] z = np.zeros((n, n), dtype=np.complex)
    cdef int i = 0

    for i in range(I):
        not_done = z.real ** 2 + z.imag ** 2 < threshold ** 2
        iterations[not_done] = i
        z[not_done] = z[not_done] ** 2 + C[not_done]

    iterations = (iterations + 1) / I
    iterations[iterations == I] = 0
    return iterations

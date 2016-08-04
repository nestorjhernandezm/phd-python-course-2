# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:00:39 2016

@author: nestor
"""

import scipy as sp
import matplotlib.pyplot as plt


def naive_mapping(c, I=100, threshold=10):
    z = 0

    for i in range(I):
        z = z ** 2 + c
        if (abs(z) > threshold):
            return float(i + 1) / I

    return 1


def mandelbrot_set_naive(Re_c, Im_c):
    Re_c_size = len(Re_c)
    Im_c_size = len(Im_c)
    M = sp.zeros([Re_c_size, Im_c_size])

    for i in xrange(Re_c_size):
        for j in xrange(Im_c_size):
            M[i, j] = naive_mapping(complex(Re_c[i] + 1j * Im_c[j]))

    return M.T  # Just to plot properly


def mandelbrot_set_vectorized(C, I=100, threshold=10):
    iterations = sp.zeros(C.shape)
    z = sp.zeros(C.shape, sp.complex64)

    for i in range(I):
        not_done = z.real ** 2 + z.imag ** 2 < threshold ** 2
        iterations[not_done] = i
        z[not_done] = z[not_done] ** 2 + C[not_done]

    iterations = (iterations + 1) / I
    iterations[iterations == I] = 0
    return iterations


def plot_mandelbrot_set(Real_c, Imaginary_c, Mandelbrot_c, implementation):
    plt.figure()
    plt.pcolor(Real_c, Imaginary_c, Mandelbrot_c, cmap=plt.cm.hot)
    plt.xlabel(r'$\mathcal{R}(c)$')
    plt.ylabel(r'$\mathcal{I}(c)$')
    plt.title(r'$Mandelbrot\ set\ \mathcal{M}(c),\ Implementation\colon\ $' +
              '$' + implementation + '.$')


## Input parameters
#points = 1000
#xmin = -2
#xmax = 1
#ymin = -1.5
#ymax = 1.5
#
## Real and imaginary axis
#Re_c = sp.linspace(xmin, xmax, points)
#Im_c = sp.linspace(ymin, ymax, points)
#Real_c, Imaginary_c = sp.meshgrid(Re_c, Im_c)
#
## Mandelbrot set computations
#M_naive = mandelbrot_set_naive(Re_c, Im_c)
#M_vectorized = mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)
#
## Plotting
#plot_mandelbrot_set(Real_c, Imaginary_c, M_naive, 'Naive')
#plot_mandelbrot_set(Real_c, Imaginary_c, M_vectorized, 'Vectorized')

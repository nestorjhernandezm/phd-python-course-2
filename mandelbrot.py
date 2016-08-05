# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:00:39 2016

@author: nestor
"""

from mandelbrot_c import mandelbrot_set_cython
import numpy as np
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
    M = np.zeros([Re_c_size, Im_c_size])

    for i in xrange(Re_c_size):
        for j in xrange(Im_c_size):
            M[i, j] = naive_mapping(complex(Re_c[i] + 1j * Im_c[j]))

    return M.T  # Just to plot properly later


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


def plot_mandelbrot_set(Real_c, Imaginary_c, Mandelbrot_c, implementation):
    plt.figure()
    plt.pcolor(Real_c, Imaginary_c, Mandelbrot_c, cmap=plt.cm.hot)
    plt.xlabel(r'$\mathcal{R}(c)$')
    plt.ylabel(r'$\mathcal{I}(c)$')
    plt.title(r'$Mandelbrot\ set\ \mathcal{M}(c),\ Implementation\colon\ $' +
              '$' + implementation + '.$')
    plt.savefig('Mandelbrot_' + implementation + '.pdf')

if __name__ == '__main__':
    # Input parameters
    points = 500

    # Real and imaginary axis
    Re_c = np.linspace(-2, 1, points)  # (xmin, xmax, points)
    Im_c = np.linspace(-1.5, 1.5, points)  # (ymin, ymax, points)
    Real_c, Imaginary_c = np.meshgrid(Re_c, Im_c)

    # Mandelbrot set computations
#    M_naive = mandelbrot_set_naive(Re_c, Im_c)
#    M_vectorized = mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)
    M_cython = mandelbrot_set_cython(Real_c + 1j * Imaginary_c)

    # Plotting
#    plot_mandelbrot_set(Real_c, Imaginary_c, M_naive, 'Naive')
#    plot_mandelbrot_set(Real_c, Imaginary_c, M_vectorized, 'Vectorized')
#    plot_mandelbrot_set(Real_c, Imaginary_c, M_vectorized, 'Cython')

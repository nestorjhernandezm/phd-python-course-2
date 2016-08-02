# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 21:00:39 2016

@author: nestor
"""

import scipy as sp
import matplotlib.pyplot as plt


def mandelbrot_mapping(c, I=100, threshold=10):
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
            M[i, j] = mandelbrot_mapping(complex(Re_c[i] + 1j * Im_c[j]))

    return M


def plot_mandelbrot_set(Re_c, Im_c, M):
    Real_c, Imaginary_c = sp.meshgrid(Re_c, Im_c)
    plt.pcolor(Real_c, Imaginary_c, M_naive.T, cmap=plt.cm.hot)
    plt.xlabel(r'$\mathcal{R}(c)$')
    plt.ylabel(r'$\mathcal{I}(c)$')


# Input parameters
points = 1000
xmin = -2
xmax = 1
ymin = -1.5
ymax = 1.5

# Real and imaginary axis
Re_c = sp.linspace(xmin, xmax, points)
Im_c = sp.linspace(ymin, ymax, points)

# Mandelbrot set computations
M_naive = mandelbrot_set_naive(Re_c, Im_c)

# Plotting
plot_mandelbrot_set(Re_c, Im_c, M_naive)

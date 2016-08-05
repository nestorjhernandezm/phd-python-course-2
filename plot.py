# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:31:12 2016

@author: nestor
"""

from mandelbrot_c import mandelbrot_set_cython
import numpy as np
import matplotlib.pyplot as plt

import mandelbrot as mnb


def plot_mandelbrot_set(Real_c, Imaginary_c, Mandelbrot_c, implementation):
    plt.figure()
    plt.pcolor(Real_c, Imaginary_c, Mandelbrot_c, cmap=plt.cm.hot)
    plt.xlabel(r'$\mathcal{R}(c)$')
    plt.ylabel(r'$\mathcal{I}(c)$')
    plt.title(r'$Mandelbrot\ set\ \mathcal{M}(c),\ Implementation\colon\ $' +
              '$' + implementation + '.$')
#    plt.savefig('Mandelbrot_' + implementation + '.pdf')


# Input parameters
points = 500

# Real and imaginary axis
Re_c = np.linspace(-2, 1, points)  # (xmin, xmax, points)
Im_c = np.linspace(-1.5, 1.5, points)  # (ymin, ymax, points)
Real_c, Imaginary_c = np.meshgrid(Re_c, Im_c)

# Mandelbrot set computations
#M_naive = mnb.mandelbrot_set_naive(Re_c, Im_c)
M_vectorized = mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)
M_cython = mandelbrot_set_cython(Real_c + 1j * Imaginary_c)

# Plotting
#plot_mandelbrot_set(Real_c, Imaginary_c, M_naive, 'Naive')
plot_mandelbrot_set(Real_c, Imaginary_c, M_vectorized, 'Vectorized')
plot_mandelbrot_set(Real_c, Imaginary_c, M_cython, 'Cython')

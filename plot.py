# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:31:12 2016

@author: nestor
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_mandelbrot_set(Real_c, Imaginary_c, Mandelbrot_c, implementation):
    plt.figure()
    plt.pcolor(Real_c, Imaginary_c, Mandelbrot_c, cmap=plt.cm.hot)
    plt.xlabel(r'$\mathcal{R}(c)$')
    plt.ylabel(r'$\mathcal{I}(c)$')
    plt.title(r'$Mandelbrot\ set\ \mathcal{M}(c),\ Implementation\colon\ $' +
              '$' + implementation + '.$')
    plt.savefig('Mandelbrot_' + implementation + '.pdf')


dataset = np.load('./mandelbrot_datasets.npz')

Real_c = dataset['Real_c']
Imaginary_c = dataset['Imaginary_c']

# Plotting
plot_mandelbrot_set(Real_c, Imaginary_c, dataset['M_naive'], 'Naive')
plot_mandelbrot_set(Real_c, Imaginary_c, dataset['M_vectorized'], 'Vectorized')
plot_mandelbrot_set(Real_c, Imaginary_c, dataset['M_cython'], 'Cython')

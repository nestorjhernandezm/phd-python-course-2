# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 17:31:12 2016

@author: nestor
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_mandelbrot_set(Mandelbrot_c, implementation):
    plt.figure()
    plt.imshow(Mandelbrot_c, cmap="hot", extent=[-2, 1, -1.5, 1.5], aspect=1)
    plt.xlabel(r'$\mathcal{R}(c)$')
    plt.ylabel(r'$\mathcal{I}(c)$')
    plt.title(r'$Mandelbrot\ set\ \mathcal{M}(c),\ Implementation\colon\ $' +
              '$' + implementation + '.$')
    plt.savefig('Mandelbrot_' + implementation + '.pdf', dpi=400)
    plt.close()

datasets = ['naive', 'vectorized', 'cython', 'numba', 'multiprocessing']

for implementation in datasets:
    data = np.load('./mandelbrot_' + implementation + '_data.npz')
    plot_mandelbrot_set(data['M'], implementation)

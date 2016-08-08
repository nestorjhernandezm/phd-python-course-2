# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:44:57 2016

@author: nestor
"""

"""
Code to call all our different functions and a basis for possible
profiling

"""
import numpy as np
import time
import matplotlib.pyplot as plt

from mandelbrot_c import mandelbrot_set_cython
import mandelbrot as mnb

methods = ['mnb.mandelbrot_set_naive(Re_c, Im_c)',
           'mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)',
           'mandelbrot_set_cython(Real_c + 1j * Imaginary_c)',
           'mnb.mandelbrot_set_numba(Re_c, Im_c)',
           'mnb.mandelbrot_set_multiprocessing(Real_c, Imaginary_c, 2)']

points = 2000

# Real and imaginary axis
Re_c = np.linspace(-2, 1, points)  # (xmin, xmax, points)
Im_c = np.linspace(-1.5, 1.5, points)  # (ymin, ymax, points)
Real_c, Imaginary_c = np.meshgrid(Re_c, Im_c)

vectorized = 0
print('Points per axis = {}'.format(points))
for m in methods:
    if (m == methods[4]):
        print "Cores for Multiprocessing Benchmark: 2"

    tic = time.time()
    y = eval(m)
    toc = time.time() - tic

    if (m == methods[1]):
        vectorized = toc  # Store time to compare later with multiprocessing

    print('{:30s} : {:10.2e} [s]'.format(m, toc))

# Multiprocessing plot
print "Speed Gain Computation"
max_cores = 8
cores = np.arange(1, max_cores + 1)
gains = np.zeros((max_cores, 1))

for core in cores:
    m = 'mnb.mandelbrot_set_multiprocessing(Real_c, Imaginary_c, ' + \
        str(core) + ')'
    tic = time.time()
    y = eval(m)
    toc = time.time() - tic
    print('Cores for Multiprocessing, {:30s}  : {:10.2e} [s]'.format(
        str(core), toc))
    gains[core - 1] = vectorized / toc

plt.plot(cores, gains, )
plt.grid('on')
plt.xlabel('Number of Cores for Multiprocessing')
plt.ylabel('Computation Speed Gain')
plt.title('Multiprocessing Gain')
plt.savefig('multiprocessing_gain.pdf')

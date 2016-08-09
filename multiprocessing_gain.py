# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:37:12 2016

@author: nestor
"""
import numpy as np
import time
import matplotlib.pyplot as plt

from mandelbrot_c import mandelbrot_set_cython
import mandelbrot as mnb

points = 3000

# Real and imaginary axis
Re_c = np.linspace(-2, 1, points)  # (xmin, xmax, points)
Im_c = np.linspace(-1.5, 1.5, points)  # (ymin, ymax, points)
Real_c, Imaginary_c = np.meshgrid(Re_c, Im_c)

vectorized_method = 'mnb.mandelbrot_set_vectorized(Real_c + 1j * Imaginary_c)'
tic = time.time()
y = eval(vectorized_method)
toc = time.time() - tic
vectorized = toc
print('{:30s} : {:10.2e} [s]'.format(vectorized_method, toc))

# Multiprocessing plot
print "Speed Gain Computation"
max_cores = 1
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

plt.plot(cores, gains, marker='.')
plt.grid('on')
plt.xlabel('Number of Cores for Multiprocessing')
plt.ylabel('Computation Speed Gain')
plt.title('Multiprocessing Gain')
plt.savefig('multiprocessing_gain.pdf')

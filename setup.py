# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:20:54 2016

@author: nestor
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension('mandelbrot_c', ["miniproject_mandelbrot.pyx"],
                           include_dirs=[numpy.get_include()])]
)

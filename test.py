# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:47:47 2016

@author: nestor
"""

"""
Uses unittest.

This will be our test to make sure we don not make a faster but erroneous
function!

"""

import unittest
from mandelbrot_c import mandelbrot_set_cython
import numpy as np
import mandelbrot as mnb


class TestMandelbrot(unittest.TestCase):

    def setUp(self):
        # This will contain a list of the methods we will test
        self.methods = ['mnb.mandelbrot_set_vectorized(' +
                        'self.Real_c + 1j * self.Imaginary_c)',
                        'mandelbrot_set_cython(' +
                        'self.Real_c + 1j * self.Imaginary_c)',
                        'mnb.mandelbrot_set_numba(self.Re_c, self.Im_c)']
        # Input parameters
        self.points = 100
        self.error_percentage = 5  # Tolerance for error percentage

        # Real and imaginary axis
        self.Re_c = np.linspace(-2, 1, self.points)  # (xmin, xmax, points)
        self.Im_c = np.linspace(-1.5, 1.5, self.points)  # (ymin, ymax, points)
        self.Real_c, self.Imaginary_c = np.meshgrid(self.Re_c, self.Im_c)
        self.M_naive = mnb.mandelbrot_set_naive(self.Re_c, self.Im_c)

    def correct_percentage(self, index):
        M = eval(self.methods[index])
        abs_error = abs((M - self.M_naive) / self.M_naive)
        total_correct = len(np.where(abs_error < self.error_percentage)[0])

        return float(total_correct / (self.points ** 2))

    # Ensure for each method that the computation returns at least
    # 99.99% correct points in the plane for the given regions in setUp
    # The reason why doing each test separately (and not one with all the
    # methods) is to observe if a method could be problematic.
    def test_mandelbrot_vectorized(self):
        self.assertTrue(np.isclose(self.correct_percentage(0), 1, atol=1e-3))

    def test_mandelbrot_cython(self):
        self.assertTrue(np.isclose(self.correct_percentage(1), 1, atol=1e-3))

    def test_mandelbrot_numba(self):
        self.assertTrue(np.isclose(self.correct_percentage(2), 1, atol=1e-3))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMandelbrot)
    unittest.TextTestRunner(verbosity=2).run(suite)

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
import numpy as np
import mandelbrot as mnb


class TestMandelbrot(unittest.TestCase):

    def setUp(self):
        # This will contain a list of the methods we will test
        self.methods = ['mnb.mandelbrot_set_vectorized(' +
                        'self.Real_c + 1j * self.Imaginary_c)']
        # Input parameters
        self.points = 500
        self.error_percentage = 5  # Tolerance for error percentage

        # Real and imaginary axis
        Re_c = np.linspace(-2, 1, self.points)  # (xmin, xmax, points)
        Im_c = np.linspace(-1.5, 1.5, self.points)  # (ymin, ymax, points)
        self.Real_c, self.Imaginary_c = np.meshgrid(Re_c, Im_c)
        self.M_naive = mnb.mandelbrot_set_naive(Re_c, Im_c)

    def test_mandelbrot_vectorized(self):

        M = eval(self.methods[0])
        abs_error = abs((M - self.M_naive) / self.M_naive)
        total_correct = len(np.where(abs_error < self.error_percentage)[0])

        # Ensure that at least 99.99% of the computed values in the set
        # are correct
        self.assertTrue(np.allclose(
            float(total_correct / (self.points ** 2)), 1, atol=1e-3))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMandelbrot)
    unittest.TextTestRunner(verbosity=2).run(suite)

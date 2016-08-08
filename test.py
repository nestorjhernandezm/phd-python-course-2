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
        # Number of cores for the multiprocessing test
        self.cores = '2'

        # This will contain a list of the methods to be tested
        self.methods = ['mnb.mandelbrot_set_vectorized(' +
                        'self.Real_c + 1j * self.Imaginary_c)',
                        'mandelbrot_set_cython(' +
                        'self.Real_c + 1j * self.Imaginary_c)',
                        'mnb.mandelbrot_set_numba(self.Re_c, self.Im_c)',
                        'mnb.mandelbrot_set_multiprocessing(' +
                        'self.Real_c, self.Imaginary_c, ' + self.cores + ')']

        # Real and imaginary axis
        self.points = 1000  # (for both the real and imaginary axes)
        self.Re_c = np.linspace(-2, 1, self.points)  # (xmin, xmax, points)
        self.Im_c = np.linspace(-1.5, 1.5, self.points)  # (ymin, ymax, points)
        self.Real_c, self.Imaginary_c = np.meshgrid(self.Re_c, self.Im_c)

        # The considered reference for the errors is the naive implementation
        self.M_naive = mnb.mandelbrot_set_naive(self.Re_c, self.Im_c)

        # Error parameters
        # point_tolerance: Tolerance for point error in percentage value.
        # A Mandelbrot computed stability point is considered correct
        # if the computed value of a given method its respective relative
        # percentual error against the naive implementation is within
        # (point_tolerance)%. Here we set this tolerance arbitrarily to 5%
        # only for showing purposes.
        self.point_tolerance = 5

        # test_tolerance: Tolerance for test error in percentage value.
        # A Mandelbrot method is considered correct if we have at least
        # (100 - test_tolerance)% correct points in the plane for the given
        # regions in setUp. If the test result is below
        # (100 - test_tolerance)%, the test fails. Here we set this tolerance
        # arbitrarily to 0.05% only for showing purposes.
        self.test_tolerance = 5e-2

    def correct_percentage(self, index):
        M = eval(self.methods[index])
        abs_error = 100 * abs((M - self.M_naive) / self.M_naive)
        total_correct = len(np.where(abs_error < self.point_tolerance)[0])

        return 100 * (float(total_correct) / (self.points ** 2))

    # The reason for doing each test separately (and not one with all the
    # methods) is to observe if a method could be problematic.
    def test_mandelbrot_vectorized(self):
        r = self.correct_percentage(0)
        print str(r) + "% of correct values"
        self.assertTrue(np.isclose(r, 100, atol=self.test_tolerance))

    def test_mandelbrot_cython(self):
        r = self.correct_percentage(1)
        print str(r) + "% of correct values"
        self.assertTrue(np.isclose(r, 100, atol=self.test_tolerance))

    def test_mandelbrot_numba(self):
        r = self.correct_percentage(2)
        print str(r) + "% of correct values"
        self.assertTrue(np.isclose(r, 100, atol=self.test_tolerance))

    def test_mandelbrot_multiprocessing(self):
        r = self.correct_percentage(3)
        print "Cores for test: " + self.cores + ". " + str(r) + \
              "% of correct values"
        self.assertTrue(np.isclose(r, 100, atol=self.test_tolerance))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMandelbrot)
    unittest.TextTestRunner(verbosity=2).run(suite)

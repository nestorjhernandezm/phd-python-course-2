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
import scipy as sp
import mandelbrot as mnb


class TestMandelbrotNaive(unittest.TestCase):

    def setUp(self):
        # This will contain a list of the methods we will test
        self.methods = ['mnb.mandelbrot_set_vectorized(' +
                        'Real_c + 1j * Imaginary_c)']

    def test_mandelbrot(self):
        # Input parameters
        points = 1000

        # Real and imaginary axis
        Re_c = sp.linspace(-2, 1, points)  # (xmin, xmax, points)
        Im_c = sp.linspace(-1.5, 1.5, points)  # (ymin, ymax, points)
        M_naive = mnb.mandelbrot_set_naive(Re_c, Im_c)

        Real_c, Imaginary_c = sp.meshgrid(Re_c, Im_c)
        for m in self.methods:
            M = eval(m)
            self.assertTrue(sp.allclose(M, M_naive))


if __name__ == '__main__':
    unittest.main()

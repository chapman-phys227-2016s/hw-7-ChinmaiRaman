#! /usr/bin/env python

"""
File: Polynomial
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: 7.27
Date: April 14th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Regular Polynomial class
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from unittest import TestCase

class Polynomial:
    
    def __init__(self, coefficients):
        self.coeff = coefficients
        
    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeffi*x**i
        return s
    
    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)
    
    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = np.zeros(M + N + 1)
        for i in range(0, M + 1):
            for j in range(0, N + 1):
                result_coeff[i + j] += c[i]*d[j]
        return Polynomial(result_coeff)
    
class Test_Polynomial(TestCase):
    def test_Polynomial(self):
        p1 = Polynomial([1.0, -1])
        p2 = Polynomial([0.0, 1, 0, 0, -6, -1])

        p3 = p1 + p2
        p3_exact = Polynomial([1.0, 0, 0, 0, -6, -1])
        assert p3.coeff == p3_exact.coeff

        p4 = p1 * p2
        p4_exact = Polynomial([0.0, 1, -1, 0, -6, 5, 1])
        assert np.allclose(p4.coeff, p4_exact.coeff, rtol = 1e-14)
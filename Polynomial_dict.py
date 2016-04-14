#! /usr/bin/env python

"""
File: Polynomial_vec
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: 7.27
Date: April 9th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Vectorizes the Polynomial class
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from unittest import TestCase

class Polynomial:

    def __init__(self, coefficients):
        if isinstance(coefficients, dict):
            self.coeff = coefficients
        else:
            print "error, provide an argument of the type dict"

    def __call__(self, x):
        sum = 0
        for key in self.coeff:
            sum += self.coeff[key] * x**key
        return sum

    def __add__(self, other):
        result_coeff = {}
        for i in range(max(max(self.coeff.keys()), max(other.coeff.keys())) + 1):
            if i in self.coeff.keys() and i in other.coeff.keys():
                result_coeff[i] = self.coeff[i] + other.coeff[i]
            elif i in self.coeff.keys() and not i in other.coeff.keys():
                result_coeff[i] = self.coeff[i]
            elif i in other.coeff.keys() and not i in self.coeff.keys():
                result_coeff[i] = other.coeff[i]
            else:
                continue
        for i in result_coeff.keys():
            if result_coeff[i] == 0:
                del result_coeff[i]
        return Polynomial(result_coeff)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        result_coeff = np.zeros(max(c.keys()) + max(d.keys()) + 1)
        for i in c.keys():
            for j in d.keys():
                result_coeff[i + j] += c[i] * d[j]
        final_result = {}
        for i, _ in enumerate(result_coeff):
            final_result[i] = result_coeff[i]
        for i in final_result.keys():
            if final_result[i] == 0:
                del final_result[i]
        return Polynomial(final_result)

    def make_array(self):
        lst = np.zeros(max(self.coeff.keys()) + 1)
        for i in self.coeff.keys():
            lst[i] = self.coeff[i]
        return lst

class Test_Polynomial(TestCase):
    def test_polynomial(self):
        p1 = Polynomial({1:1, 100:-3})
        p2 = Polynomial({1:-1, 20:1, 100:4})

        p3 = p1 + p2
        p3_exact = Polynomial({20:1, 100:1})
        assert np.all(p3.coeff == p3_exact.coeff)

        p4 = p1 * p2
        p4_exact = Polynomial({2:-1.0,21:1.0,101:7.0,120:-3.0,200:-12.0})
        assert np.allclose(p4.make_array(), p4_exact.make_array(), rtol = 1e-14)
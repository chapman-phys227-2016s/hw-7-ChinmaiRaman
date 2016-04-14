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
        if isinstance(coefficients, np.ndarray):
                self.coeff = coefficients
        else:
            print "error, provide an argument of the type numpyarray"
            raise TypeError

    def __call__(self, x):
        p = np.zeros_like(self.coeff)
        for i, _ in enumerate(p):
            p[i] = i
        p = x**p
        sum = 0
        for elem in self.coeff * p:
            sum += elem
        return sum

    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = np.copy(other.coeff)
            for i in range(len(result_coeff)):
                result_coeff[i] += self.coeff[i]
            result_coeff = np.concatenate((result_coeff, self.coeff[len(other.coeff):]))
        else:
            result_coeff = np.copy(self.coeff)
            for i in range(len(result_coeff)):
                result_coeff[i] += other.coeff[i]
            result_coeff = np.concatenate((result_coeff, other.coeff[len(self.coeff):]))
        return Polynomial(result_coeff)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = np.zeros(M + N + 1)
        for i in range(0, M + 1):
            for j in range(0, N + 1):
                result_coeff[i + j] += c[i] * d[j]
        return Polynomial(result_coeff)

    def differentiate(self):
        n = len(self.coeff)
        self.coeff[:-1] = np.linspace(1, n - 1, n - 1) * self.coeff[1:]
        self.coeff = self.coeff[:-1]

    def derivative(self):
        dpdx = Polynomial(self.coeff[:])
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ''
        for i in range(len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('*1', '')
        s = s.replace('x^1 ', 'x ')
        if s[0:3] == ' + ':
            s = s[3:]
        if s[0:3] == ' - ':
            s = '-' + s[3:]
        return s

class Test_Polynomial(TestCase):
    def test_Polynomial(self):
        p1 = Polynomial(np.array([1, -1]))
        p2 = Polynomial(np.array([0, 1, 0, 0, -6, -1]))

        print p1.coeff.dtype
        print p2.coeff.dtype

        p3 = p1 + p2
        p3_exact = Polynomial(np.array([1, 0, 0, 0, -6, -1]))
        assert np.all(p3.coeff == p3_exact.coeff)

        p4 = p1 * p2
        p4_exact = Polynomial(np.array([0, 1, -1, 0, -6, 5, 1]))
        assert np.allclose(p4.coeff, p4_exact.coeff, rtol = 1e-14)

        p5 = p2.derivative()
        p5_exact = Polynomial(np.array([1, 0, 0, -24, -5]))
        assert np.all(p5.coeff == p5_exact.coeff)

        p6 = Polynomial(np.array([0, 1, 0, 0, -6, -1]))
        p6.differentiate()
        p6_exact = p5_exact
        assert np.all(p6.coeff == p6_exact.coeff)
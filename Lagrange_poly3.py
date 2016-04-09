#! /usr/bin/env python

"""
File: Lagrange_poly3
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: 7.8
Date: April 8th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Implements Lagrange's interpolation formula
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

class LagrangeInterpolation:

    def __init__(self, xp, yp):
        self.xp, self.yp = xp, yp

    def L_k(self, x, k):
        """
        Returns the product that is used in calculating Lagrange's interpolation formula
        """
        product = 1.0
        for i in xrange(len(self.xp)):
            if i == k:
                continue
            product *= (x - self.xp[i]) / float(self.xp[k] - self.xp[i])
        return product

    def plot(self, resolution = 1001):
        """
        Plots the interpolation points and the continuous function that goes through all the points
        """
        fig = plt.figure(1)
        xinter = np.linspace(self.xp[0], self.xp[-1], resolution)
        yinter = np.array([self.__call__(x) for x in xinter])
        plt.plot(self.xp, self.yp, 'ro')
        plt.plot(xinter, yinter, 'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis([self.xp[0], self.xp[-1], min(self.xp) - 0.3, max(self.yp) + 0.3])
        plt.title('f(x) and interpolation points')
        plt.show(fig)

    def __call__(self, x):
        """
        Returns the polynomial pL(x), known as Lagrange's interpolation formula
        """
        summation = 0.0
        for k in xrange(len(self.yp)):
            summation += self.L_k(x, k) * self.yp[k]
        return summation

def test_p_L():
    xp = np.linspace(0, np.pi, 5)
    yp = np.sin(xp)
    p_L = LagrangeInterpolation(xp, yp)
    x = 1.2
    for i in xrange(len(p_L.yp)):
        assert(abs(p_L(p_L.xp[i]) - p_L.yp[i]) < 1e-3), 'bug in class LagrangeInterpolation'
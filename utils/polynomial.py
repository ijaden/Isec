# -*- coding: utf-8 -*-

from random import randint
from utils.tools import *
import numpy as np
import galois


class poly:
    # the functions are defined over F_p
    module =0
    coefficients = []

    def __init__(self,coefficients,module):
        self.module = module
        self.coefficients = [x % module for x in coefficients]

    @property
    def coef(self):
        return self.coefficients
    @coef.setter
    def coef(self, coef):
        self.coefficients =[x % self.module for x in coef]

    @staticmethod
    def random_polynomial(degree, intercept, module):
        """ Generates a random polynomial with positive coefficients.
        """
        if degree < 0:
            raise ValueError('Degree must be a non-negative number.')
        coefficients = [intercept % module]
        for i in range(degree):
            random_coeff = randint(0, module-1)
            coefficients.append(random_coeff)
        return coefficients

    @staticmethod
    def get_polynomial_points(coefficients, x, module):
        """ Return the value on x
            [ (x, f(x))]
        """
        y = coefficients[0]
        for i in range(1, len(coefficients)):
            exponentiation = (x ** i) % module
            term = (coefficients[i] * exponentiation) % module
            y = (y + term) % module
        return y


    @staticmethod
    def lagrange_interpolation_x(points, module, x):
        """
        module should be a prime!!
        points= [(x1,f(x1)),(x2,f(x2))...]
        :return: f_x
        """
        x_values,y_values = zip(*points)
        n = len(points)
        f_x = 0
        for i in range(n):
            numerator, denominator = 1, 1
            for j in range(n):
                if i == j:
                    continue
                numerator = (numerator * (x - x_values[j])) % module
                denominator = (denominator * (x_values[i] - x_values[j])) % module
            lagrange_polynomial = numerator * mod_inverse(denominator, module)
            f_x = (module + f_x + (y_values[i] * lagrange_polynomial)) % module
        return f_x

# The following funcs use lib which are slow.
    @staticmethod
    def lagrange_interpolation(points,module):
        """
        :param points: points= [(x1,f(x1)),(x2,f(x2))...]
        :param module: a prime
        :return: coef(list)
        """
        gf = galois.GF(module)
        x_values,y_values = zip(*points)
        a = galois.lagrange_poly(gf(x_values), gf(y_values))
        print("the poly is :"+str(a))
        return a.coefficients(order="asc").tolist()

    @staticmethod
    def NTT(coef, size=None, module=None):
        """
        The Number-Theoretic Transform (NTT) is a specialized Discrete Fourier Transform (DFT) over a finite field.
        :input: coef
        size = N  the degree of coef. Has the form N = 2^k
            for g(x)*f(x) , N>= deg(g)+deg(f)+1
        module = m * N + 1
        :return: values

        """
        return galois.ntt(coef,size,module).tolist()

    @staticmethod
    def INTT(values,size=None, module=None):
        """
        Computes the Inverse Number-Theoretic Transform (INTT)
        :input: values
        :return: coef
        """
        return galois.intt(values,size,module).tolist()


#-------Operations for polynomial ring are below------------
    @staticmethod
    def modpoly_inverse(cof,modpoly):
        pass
    @staticmethod
    def mod_poly(poly1,poly2,module):
        """
        :param poly1:
        :param poly2:
        :param module:
        :return:
        """
        pass
        # return cof,poly(cof,module)

#


if __name__ == "__main__":



    points_a = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    # points_b = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    mod = 131
    print(poly.lagrange_interpolation_x(points_a,mod,8))
    # a = poly.lagrange_interpolation(points_a,mod)
    # b = poly.lagrange_interpolation(points_b, mod)
    # print(a)
    # print(b)

    # a = [6,0,10,7,2]
    # mod = 6*16+1
    # a_ntt = poly.NTT(a)
    # print(a_ntt)
    #
    # b = [1,0,0,0,1]
    # b_ntt = poly.NTT(b)
    # print(b_ntt)
    # c_ntt = []
    # for i in range(len(a_ntt)):
    #     c_ntt.append(a_ntt[i]*b_ntt[i] % 11)
    # print(c_ntt)
    # print(poly.INTT(c_ntt))



#!/usr/bin/env python3

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary

    def __add__(self, no):
        re = self.re + no.re
        im = self.im + no.im
        return Complex(re,im)

    def __sub__(self, no):
        re = self.re - no.re
        im = self.im - no.im
        return Complex(re,im)

    def __mul__(self, no):
        re = self.re*no.re - self.im * no.im
        im = self.re * no.im + self.im * no.re
        return Complex(re,im)

    def __truediv__(self, no):
        re = (self.re*no.re + self.im*no.im) / (no.re**2 + no.im**2)
        im = (-self.re*no.im + self.im*no.re) / (no.re**2 + no.im**2)
        return Complex(re,im)

    def mod(self):
        mod = pow(self.re**2+self.im**2,0.5)
        return Complex(mod,0.0)

    def __str__(self):
        if self.im == 0:
            result = "%.2f+0.00i" % (self.re)
        elif self.re == 0:
            if self.im >= 0:
                result = "0.00+%.2fi" % (self.im)
            else:
                result = "0.00-%.2fi" % (abs(self.im))
        elif self.im > 0:
            result = "%.2f+%.2fi" % (self.re, self.im)
        else:
            result = "%.2f-%.2fi" % (self.re, abs(self.im))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

#!/usr/bin/env python3

import numpy

coeffs = list(map(float,input().split()))
x = float(input())

fvalue = numpy.polyval(coeffs,x)
print(fvalue)

# others:
# numpy.pols(): coefficients
# numpy.roots(): roots
# numpy.polyint(): indefinite integral
# numpy.polyder(): derivative
# numpy.polyval(): evaluation at position
# numpy.polyfit(): fit with least-squares

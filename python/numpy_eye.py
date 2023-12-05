#!/usr/bin/python3

import numpy
numpy.set_printoptions(legacy='1.13')

dim_n,dim_m = list(map(int,input().split()))

# eye: entries 1 along central body diagonal (k=0) or 
# along upper body diagonal (k>0)/lower body diagonal (k<0)

print(numpy.eye(dim_n,dim_m,k=0))

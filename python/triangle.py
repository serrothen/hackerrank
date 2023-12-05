#!/usr/bin/env python3

import math

len_ab = float( input() )
len_bc = float( input() )

len_ac = math.sqrt(len_ab**2 + len_bc**2)
len_mc = len_ac/2.0
height = len_ab/2.0
len_m2c = math.sqrt(len_mc**2-height**2)

angle = math.atan( height/(len_bc-len_m2c) )

print(f"{round(angle/(2.*math.pi)*360.0)}{chr(176)}")

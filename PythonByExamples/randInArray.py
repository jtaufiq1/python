#!/usr/bin/python3

# Random number with a range and step size

import random
from array import *

randInts = array('i', [])
for i in range(0,5):
    randInt = random.randint(1,(2**16)-1)
    randInts.append(randInt)

randInts = sorted(randInts)
randInts.reverse()
for j in randInts:
    print(j)

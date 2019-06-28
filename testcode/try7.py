#!/usr/bin/env python3

import math, random

def calcCirm(radius):
    return math.pi * 2 * radius

class Circle:
    pass

circles = []

for i in range(0,10):
    c = Circle()
    c.radius = random.uniform(1.1, 9.5)
    c.circmf = calcCirm(c.radius)
    circles.append(c)

for c in circles:
    print(c.radius, c.circmf)

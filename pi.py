import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

i = 1
circle = 0.0
total = 0.0

for i in range(1,10000000):
    x = random.random()
    y = random.random()
    r = x**2 + y**2
    i += 1
    if r <= 1:
        circle += 1
        total += 1
        next
    else:
        total += 1
        next

pi = 4*circle/total

print pi
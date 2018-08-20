#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1000, 0, 1])

maxn=0

while 1==1:
    x = np.random.random()
    y = np.random.random()
    if x>maxn:
	maxn=x
	plt.axis([0, maxn, 0, 1])
    plt.scatter(x, y)
    plt.pause(0.05)

plt.show()
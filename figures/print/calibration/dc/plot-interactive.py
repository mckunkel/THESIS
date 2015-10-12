#!/usr/bin/env python

import numpy
from matplotlib import rc
from matplotlib import pyplot

rc('text', usetex=True)
rc('font', family='serif')

d = numpy.loadtxt('DCsmall.dat', unpack=True, skiprows=1)

fig = pyplot.figure(figsize=(6,4), dpi=100, facecolor = '#FFFFFF')
ax = fig.add_subplot(111)

ax.plot(d[0], d[7], 'o')
ax.plot(d[0], d[8], 'o')

pyplot.show()

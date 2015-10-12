#!/usr/bin/env python

import numpy
from matplotlib import rc, pyplot, mlab
from math import sqrt

rc('text', usetex=True)
rc('font', family='serif')

x = numpy.loadtxt('trig_I_study.txt', unpack=True)

fig = pyplot.figure(figsize=(6,4), dpi=100)
ax = fig.add_subplot(111)
ax.plot(numpy.arange(0.,80.), 25.*numpy.arange(0.,80.), 'r-', linewidth=2)
ax.plot(numpy.arange(0.,80.), 1.28*numpy.arange(0.,80.)**2, 'g--', linewidth=2)
ax.plot(x[0],x[15], 'o', markersize=8)

ax.set_title(r'production trigger (bit 8)')
ax.set_xlabel(r'beam current (nA)')
ax.set_ylabel(r'rate (Hz)')

pyplot.show()


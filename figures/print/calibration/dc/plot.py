#!/usr/bin/env python

import numpy

from matplotlib import rc
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

rc('text', usetex=True)
rc('font', family='serif')

d = numpy.loadtxt('DCsmall.dat', unpack=True, skiprows=1)

fig = Figure(figsize=(8,4), dpi=100, facecolor = '#FFFFFF')
ax = fig.add_subplot(111)

pl = []
for i in numpy.arange(1,7):
    pl += ax.plot(d[0], d[i])

for p in pl:
    p.set_marker('o')
    p.set_markersize(5)

ax.set_xlabel(r'run number')
ax.set_xlim(56350,57323)

ax.set_ylabel(r'\texttt{DC} residual mean (\textmu m)')
ax.set_ylim(-150,150)

legend_labels = []
for i in numpy.arange(1,7):
    legend_labels += [i]

lgd = fig.legend(pl, legend_labels, title=r'superlayer', loc='right')
lgd.draw_frame(False)

fig.subplots_adjust(right=0.85)

can = FigureCanvas(fig)
can.print_figure('dc_resid_mean.eps')



fig = Figure(figsize=(8,4), dpi=100, facecolor = '#FFFFFF')
ax = fig.add_subplot(111)

pl = []
for i in numpy.arange(7,13):
    pl += ax.plot(d[0], d[i])

for p in pl:
    p.set_marker('o')
    p.set_markersize(5)

ax.set_xlabel(r'run number')
ax.set_xlim(56350,57323)

ax.set_ylabel(r'\texttt{DC} residual standard deviation (\textmu m)')
ax.set_ylim(250,400)

legend_labels = []
for i in numpy.arange(1,7):
    legend_labels += [i]

lgd = fig.legend(pl, legend_labels, title=r'superlayer', loc='right')
lgd.draw_frame(False)

fig.subplots_adjust(right=0.85)

can = FigureCanvas(fig)
can.print_figure('dc_resid_sigma.eps')

#!/usr/bin/env python

import numpy
from matplotlib import rc, pyplot, mlab
from math import sqrt

rc('text', usetex=True)
rc('font', family='serif')

data = numpy.loadtxt('harp_tagger_04-04-08_17:19:51.txt')

## data[0] vs. data[14]

x = []
xcounts = []
xerr = []

y = []
ycounts = []
yerr = []

xback = 16.853
xamp = 1950.0
xmean = 27.97
xsigma = 0.115

yback = 16.853
yamp = 2050.0
ymean = 54.66
ysigma = 0.105

step = 0.02

for i in data:
    if i[0] > 25 and i[0] < 31:
        x += [i[0]]
        xcounts += [i[14]]
        xerr += [sqrt(i[14])]
    if i[0] > 52 and i[0] < 57:
        y += [i[0]]
        ycounts += [i[14]]
        yerr += [sqrt(i[14])]

fig1 = pyplot.figure(1, figsize=(10,5))
fig1.subplots_adjust(wspace=0.1)

ax1_1 = fig1.add_subplot(121)
ax1_1.errorbar(x, xcounts, xerr, linestyle='none', marker='_')

ax1_1.set_yscale('log')

ax1_1.set_title(r'$x$ profile')
ax1_1.set_xlabel(r'\emph{harp} position (mm)')
ax1_1.set_ylabel(r'counts')

xgaus = mlab.normpdf(numpy.arange(25,31,step), xmean, xsigma)
ax1_1.plot(numpy.arange(25,31,step), xamp * xgaus + xback, color='orange', dashes=[10,3], linewidth=1)


ax1_2 = fig1.add_subplot(122, sharey=ax1_1)
ax1_2.errorbar(y, ycounts, yerr, linestyle='none', marker='_')

ax1_2.set_title(r'$y$ profile')
ax1_2.set_xlabel(r'\emph{harp} position (mm)')

pyplot.setp(ax1_2.get_yticklabels(), visible=False)

ygaus = mlab.normpdf(numpy.arange(52,57,step), ymean, ysigma)
ax1_2.plot(numpy.arange(52,57,step), yamp * ygaus + yback, color='orange', dashes=[10,3], dash_joinstyle='round', linewidth=1)

ax1_1.set_ylim(5,10000)

pyplot.show()


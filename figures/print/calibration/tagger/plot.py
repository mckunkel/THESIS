#!/usr/bin/env python

import numpy
from matplotlib import rc
from matplotlib import pyplot

rc('text', usetex=True)
rc('font', family='serif')

d = numpy.loadtxt('tagger_energies.dat', unpack=True)

fig = pyplot.figure(figsize=(4,3), dpi=100, facecolor = '#FFFFFF')
ax = fig.add_subplot(111)

res = []
for i in numpy.arange(len(d)-1):
    res += [d[i+1] - d[i]]
res += [res[-1]]

arun = []
ares = []

l = 10
for i in numpy.arange(l,len(d),l):
    arun += [numpy.average(d[i-l:i])]
    ares += [1000.*numpy.average(res[i-l:i])]

print numpy.average(ares)

ax.plot(arun,ares)

ax.set_xlim(1,5.5)
ax.set_ylim(3,8)

ax.set_xlabel(r'$E_{\mathrm{beam}}$ (GeV)')
ax.set_ylabel(r'$\delta E_{\mathrm{beam}}$ (MeV)')

fig.subplots_adjust(bottom=0.2)

fig.savefig('tagger_energies.ps')

pyplot.show()

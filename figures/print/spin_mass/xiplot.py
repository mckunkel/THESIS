#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from pdg_listing import *

def pdg_bar(ax, particle, color, alpha, subcolumn=(1,1)):
    mass, width, parity, spin = particle
    ncols, thiscol = subcolumn

    bot = mass - width

    width_min = mass / 100.

    if width < width_min:
        hei = width_min
    else:
        hei = width

    if not spin:
        spin = 0.5
    elif type(spin) is str and spin[0] == '>':
        spin = spin[1:].split('/')
        spin = (float(spin[0]) + 2.) / float(spin[1])

    if parity == -1:
        lef = -1 * spin - 0.5
    else:
        lef = spin - 0.5

    wid = 1. / ncols
    lef = lef + (thiscol - 1.) * wid
    wid -= 0.01

    return ax.bar(
        left = lef,
        height = hei,
        width = wid,
        bottom = bot,
        color = color,
        alpha = alpha,
        linewidth = 0 )

def half_int_xaxis_labels(ax):
    xinvl = ax.xaxis.get_view_interval()

    locs = []
    for x in np.arange(xinvl[0],xinvl[1],0.5):
        locs += [x]
    locs += [xinvl[1]]

    ax.set_xlim(locs[0], locs[-1])
    ax.xaxis.set_ticks(locs)

    loc = locs[0]
    labels = []
    for tick in ax.xaxis.get_major_ticks():
        numerator = (loc * 2)
        if abs(numerator) % 2 == 1:
            # tick loc is half integer
            # no tick but have label
            tick.tick1On = False
            tick.tick2On = False
            if numerator < 0:
                label = r'$-'
            else:
                label = r'$+'
            label += r'\frac{'
            label += str(int(abs(numerator)))
            label += r'}{2}$'
            labels += [label]
        else:
            # tick loc is integer
            # keep tick but have no label
            tick.label1On = False
            labels += ['']
        loc = loc + 0.5

    ax.xaxis.set_ticklabels(labels)




fig_n_xi = plt.figure(0)
ax_n_xi = fig_n_xi.add_subplot(1,1,1)
for m, merp, merm, w, werp, werm, i, g, j, p, c, a, mc, q, r, s, name, quarks in pdg:
    part = (m, w, p, j)
    if r > 2:
        if r == 4:
            alp = 1.
        else:
            alp = 0.25
        if name[:1] == 'N':
            print m, w
            x = pdg_bar(ax_n_xi, part, 'orange', alp, (2,1))
            if r == 4:
                part_N = x
        elif name[:5] == 'Delta':
            print m, w
            x = pdg_bar(ax_n_xi, part, 'red', alp, (2,2))
            if r == 4:
                part_Delta = x
    if name[:2] == 'Xi' and not name[:4] in ['Xi(c', 'Xi(b']:
        print m, w
        x = pdg_bar(ax_n_xi, part, 'blue', (r/4.), (1,1))
        if r == 4:
            part_Xi = x
ax_n_xi.set_xlabel(r'parity times spin ($P \times J$)')
ax_n_xi.set_ylabel(r'mass (MeV)')
ax_n_xi.legend([part_N[0], part_Delta[0], part_Xi[0]], ['N',r'$\Delta$', r'$\Xi$'], loc=0)
half_int_xaxis_labels(ax_n_xi)


fig_sigma_xi = plt.figure(1)
ax_sigma_xi = fig_sigma_xi.add_subplot(1,1,1)
for m, merp, merm, w, werp, werm, i, g, j, p, c, a, mc, q, r, s, name, quarks in pdg:
    part = (m, w, p, j)
    if r > 2:
        if r == 4:
            alp = 1.
        else:
            alp = 0.25
        if name[:5] == 'Sigma' and not name[:7] in ['Sigma(c', 'Sigma(b']:
            print m, w
            x = pdg_bar(ax_sigma_xi, part, 'green', alp, (2,1))
            if r == 4:
                part_Sigma = x
    if name[:2] == 'Xi' and q == -1 and not name[:4] in ['Xi(c', 'Xi(b']:
        print m, w
        x = pdg_bar(ax_sigma_xi, part, 'blue', (r/4.), (2,2))
        if r == 4:
            part_Xi = x
ax_sigma_xi.set_xlabel(r'parity times spin ($P \times J$)')
ax_sigma_xi.set_ylabel(r'mass (MeV)')
ax_sigma_xi.legend([part_Sigma[0], part_Xi[0]], [r'$\Sigma$', r'$\Xi$'], loc=0)
half_int_xaxis_labels(ax_sigma_xi)


fig_n_sigma_xi_offset = plt.figure(2)
ax_n_sigma_xi_offset = fig_n_sigma_xi_offset.add_subplot(1,1,1)
for m, merp, merm, w, werp, werm, i, g, j, p, c, a, mc, q, r, s, name, quarks in pdg:
    part = [m, w, p, j]
    if r > 2:
        if r == 4:
            alp = 1.
        else:
            alp = 0.25
        if name[:1] == 'N' or name[:5] == 'Delta':
            part[0] -= 938.
            part[1] = 10.
            x = pdg_bar(ax_n_sigma_xi_offset, part, 'red', alp, (3,1))
            if r == 4:
                part_N = x
        if name[:5] == 'Sigma' and not name[:7] in ['Sigma(c', 'Sigma(b']:
            part[0] -= 1189.
            #part[1] = 10.
            x = pdg_bar(ax_n_sigma_xi_offset, part, 'green', alp, (3,2))
            if r == 4:
                part_Sigma = x
    if name[:2] == 'Xi' and not name[:4] in ['Xi(c', 'Xi(b']:
        part[0] -= 1314.
        #part[1] = 10.
        x = pdg_bar(ax_n_sigma_xi_offset, part, 'blue', (r/4.), (3,3))
        if r == 4:
            part_Xi = x
ax_n_sigma_xi_offset.set_xlabel(r'parity times spin ($P \times J$)')
ax_n_sigma_xi_offset.set_ylabel(r'mass (MeV)')
ax_n_sigma_xi_offset.legend([part_N[0], part_Sigma[0], part_Xi[0]], ['N', r'$\Sigma$', r'$\Xi$'], loc=0)
half_int_xaxis_labels(ax_n_sigma_xi_offset)

plt.show()

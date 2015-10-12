#!/usr/bin/env python

from sys import exit
from os import path
from numpy import loadtxt, array, sqrt, arange
from matplotlib import rc, pyplot

#rc('text', usetex=True)
#rc('text.latex', preamble='\usepackage{yfonts},\usepackage[T1]{fontenc},\usepackage[latin1]{inputenc},\usepackage{txfonts},\usepackage{lmodern},\usepackage{blindtext}')
#rc('font', family='serif')

xi1320 = {
    'erg' : [2.5162499999999999, 2.7487499999999998, 2.9812499999999997, 3.2137499999999997, 3.4462499999999996, 3.6787499999999995, 3.9112499999999994, 4.1437499999999998, 4.3762499999999998, 4.6087499999999997, 4.8412499999999996, 5.0737499999999995, 5.3062499999999995],
    'tslope' : [6.0270400000000004, 5.6648300000000003, 3.8778000000000001, 3.4485100000000002, 2.9444900000000001, 2.5550999999999999, 1.8367500000000001, 1.5403199999999999, 1.72525, 1.5794299999999999, 1.78322, 1.5954999999999999],
    'tslopeerr' : [0.81749300000000003, 0.50601300000000005, 0.134436, 0.084252499999999994, 0.047793700000000001, 0.044403900000000003, 0.035148100000000002, 0.038067200000000002, 0.052113899999999998, 0.053545700000000002, 0.054790199999999997, 0.070069699999999999],
    'ymass' : [0,1.9216500000000001, 1.94716, 1.9828600000000001, 2.00691, 2.02901, 2.0342500000000001, 2.0600800000000001, 2.0765799999999999, 2.08541, 2.1249500000000001, 2.1414800000000001],
    'ymasserr' : [0,0.0022151499999999999, 0.0042508499999999996, 0.00281416, 0.0028210000000000002, 0.0035924799999999999, 0.0051918399999999996, 0.0066638699999999997, 0.0054127400000000001, 0.0063350899999999998, 0.0074598599999999996, 0.0069192799999999999],
    'ywidth' : [0,0.042700000000000002, 0.074769299999999997, 0.083129599999999998, 0.10706499999999999, 0.13011500000000001, 0.16043099999999999, 0.188864, 0.18759500000000001, 0.197742, 0.2243, 0.209816],
    'ywidtherr' : [0,0.00162477, 0.0029572600000000002, 0.0023556900000000001, 0.0021623499999999999, 0.0025099499999999999, 0.0041728700000000004, 0.0053336700000000004, 0.0041649800000000004, 0.0039287599999999999, 0.0050503900000000001, 0.0060937400000000003],
    }
xi1530 = {
    'erg_tslope' : [2.59375, 2.9812500000000002, 3.3687500000000004, 3.7562500000000005, 4.1437500000000007, 4.53125, 4.9187500000000011, 5.3062500000000004],
    'erg_y' : [2.6333333333333333, 3.1000000000000001, 3.5666666666666669, 4.0333333333333332, 4.5000000000000009, 4.9666666666666677],
    'tslope' : [2.6986500000000002, 2.55803, 1.8661700000000001, 2.4791799999999999, 1.8906400000000001, 1.3927],
    'tslopeerr' : [0.32059300000000002, 0.156586, 0.147568, 0.097313899999999995, 0.125717, 0.12431399999999999],
    'ymass' : [2.10053, 2.12547, 2.1817000000000002, 2.2158199999999999, 2.2538200000000002],
    'ymasserr' : [0.019386299999999999, 0.0023518699999999998, 0.0029657400000000001, 0.00291647, 0.00387054],
    'ywidth' : [0.019386299999999999, 0.053957199999999997, 0.083884200000000006, 0.098904699999999998, 0.119238],
    'ywidtherr' : [0.061873200000000003, 0.0016354900000000001, 0.0020318799999999998, 0.00191957, 0.0023715300000000002],
    }

def sigfigs(x, n):
    ret = '{0:g}'.format(float(str('{0:.'+str(n-1)+'e}').format(float(x))))
    ret_len = len(ret.replace('.',''))
    ret_len -= (ret_len - len(ret.lstrip('0.')))
    if float(ret) > 1. and ret.count('.') == 1:
        ret_len -= 1
    if ret_len < n:
        if ret.count('.') == 0:
            ret += '.'
        ret += '0'*(n-ret_len)
    return ret


print r'''\begin{tabular}{ccccccc}
\multicolumn{7}{c}{$\Xi^-$(1320)} \\
\multicolumn{7}{c}{$\Delta E_\mathrm{beam} = $~MeV} \\
\hline \hline
$E_\mathrm{beam}$ & $t$-slope & err & MM($\Kp_\mathrm{fast}$) & err & MM($\Kp_\mathrm{fast}$) & err \\
(GeV) &  &  & mean (GeV) & & width (MeV) & \\
\hline
'''
x = xi1320
l = len(x['tslope'])
for x in zip(
    x['erg'][-l:],
    x['tslope'],
    x['tslopeerr'],
    x['ymass'],
    x['ymasserr'],
    x['ywidth'],
    x['ywidtherr'],
    ):
    print sigfigs(x[0], 4),
    print r'&',sigfigs(x[1], 4),
    print r'&',sigfigs(x[2], 2),
    print r'&',sigfigs(x[3], 5),
    print r'&',sigfigs(x[4], 2),
    print r'&',sigfigs(1000.*x[5], 3),
    print r'&',sigfigs(1000.*x[6], 2),
    print r'\\'
print r'''
\hline \hline
\end{tabular}
'''

print r'''\begin{tabular}{ccc}
\multicolumn{3}{c}{$\Xi^-$(1530)} \\
\multicolumn{3}{c}{$\Delta E_\mathrm{beam} = $~MeV} \\
\hline \hline
$E_\mathrm{beam}$ & $t$-slope & err \\
\hline
'''
x = xi1530
l = len(x['tslope'])
for x in zip(
    x['erg_tslope'][-l:],
    x['tslope'],
    x['tslopeerr'],
    ):
    print sigfigs(x[0], 4),
    print r'&',sigfigs(x[1], 4),
    print r'&',sigfigs(x[2], 2),
    print r'\\'
print r'''
\hline \hline
\end{tabular}
'''


print r'''\begin{tabular}{ccccc}
\multicolumn{5}{c}{$\Xi^-$(1530)} \\
\multicolumn{5}{c}{$\Delta E_\mathrm{beam} = $~MeV} \\
\hline \hline
$E_\mathrm{beam}$ & MM($\Kp_\mathrm{fast}$) & err & MM($\Kp_\mathrm{fast}$) & err \\
(GeV) & mean (GeV) & & width (MeV) & \\
\hline
'''
x = xi1530
l = len(x['ymass'])
for x in zip(
    x['erg_y'][-l:],
    x['ymass'],
    x['ymasserr'],
    x['ywidth'],
    x['ywidtherr'],
    ):
    print sigfigs(x[0], 4),
    print r'&',sigfigs(x[1], 5),
    print r'&',sigfigs(x[2], 2),
    print r'&',sigfigs(1000.*x[3], 3),
    print r'&',sigfigs(1000.*x[4], 2),
    print r'\\'
print r'''
\hline \hline
\end{tabular}
'''
exit(0)


def hist2line(erg, data):
    ebinwid = (erg[1] - erg[0])
    x = [erg[0]-0.5*ebinwid]
    y = [0]
    b = 0
    for a in erg:
        x += [a - 0.5*ebinwid, a + 0.5*ebinwid]
        y += [data[b], data[b]]
        b += 1
    x += [erg[-1]+0.5*ebinwid]
    y += [0]
    return [x, y]

part = xi1320_xfn['noprot']
fig = pyplot.figure()
ax = fig.add_subplot(111)
h = part['basic']['accept']
x, y = hist2line(part['erg'][-len(h):], h)
ax.fill(x, y)

pyplot.show()

import pyfits
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy 
from pylab import *
import scipy

data=pyfits.open('HW_1_Mel6002.fit')
data=data[1].data

gr_color = [row['g'] - row['r'] for row in data]
ri_color=[row['r'] - row['i'] for row in data]

#b - get median of g-r

gr_color.sort()

if len(gr_color) % 2 !=0: 
	med=gr_color[int(len(gr_color)/2.-0.5)]
else:
	med = np.average(gr_color[int(len(gr_color)/2.)],gr_color[int(len(gr_color)/2.-1)])

#unsort g-r
gr_color = [row['g'] - row['r'] for row in data]



extent=[-.5,2,-.5,2]
H,xedges,yedges=scipy.histogram2d(ri_color,gr_color,range=[[-.5,2],[-.5,2]])
Greys_cm=cm.Greys

f=plt.figure(figsize = (15,4.7))
gs=gridspec.GridSpec(1,3)

a=plt.subplot(gs[0,0])
nbins=9
plt.hist(gr_color, range=[-1,3],bins=nbins)
plt.xlabel('g-r',fontsize=14)
plt.ylabel('count',fontsize=14)
f.text(.25,.7,'median=%s'%round(med,2))
plt.title('a) g-r histogram',fontsize=14)

c=plt.subplot(gs[0,1])
plt.scatter(ri_color,gr_color,s=3)
plt.xlim(-.5,2)
plt.ylim(-.5,2)
plt.xlabel('r-i',fontsize=14)
plt.ylabel('g-r',fontsize=14)
plt.title('c) g-r vs r-i scatter',fontsize=14)


d=plt.subplot(gs[0,2])
plt.imshow(H.T,origin='lower',interpolation='nearest',cmap=Greys_cm,extent=extent,vmin=0,vmax=600)
plt.colorbar()
plt.xlim(-.5,2)
plt.ylim(-.5,2)
plt.xlabel('r-i',fontsize=14)
plt.ylabel('g-r',fontsize=14)
plt.title('d) g-r vs r-i histogram',fontsize=14)

plt.savefig('HW1_problem1.pdf')



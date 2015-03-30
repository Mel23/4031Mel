import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

data = np.loadtxt('EW_z3p1_Ouchi2007.dat',unpack=True)

nbins=10
frequency=plt.hist(data,bins=nbins)
norm_freq=[value/len(data) for value in frequency[0]]
x=[]
for i in range(0,len(frequency[1])-1):
	x.append((frequency[1][i]+frequency[1][i+1])/2.)

f=plt.figure(figsize=(10,10))
gs=gridspec.GridSpec(1,1)
gs.update(wspace=0.1)

a=plt.subplot(gs[0,0])
plt.plot(x,norm_freq,marker='o')
plt.xlabel('Equivalent Width (Angstrom)')
plt.ylabel('Normalized Counts')

## probability function
def prob(EW,Wo):
	y=(Wo*(np.exp(-50./Wo)-1))**(-1)*np.exp(-EW/Wo)
	return y

plt.savefig('HW2_prob2.pdf')

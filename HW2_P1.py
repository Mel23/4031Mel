import pyfits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from scipy.stats import pearsonr as ps
from scipy.stats import spearmanr as sp
from scipy.stats import kendalltau as kd

data=pyfits.open('test_correlation.fits')
data=data[0].data
#a - compute correlation coefficients for data
cos=[]
p_values=[]

x=data[:,0]
y=data[:,1]

x=[value for value in x]
y = [value for value in y]
cos.append(ps(x,y)[0])
cos.append(sp(x,y)[0])
cos.append(kd(x,y)[0])
p_values.append(ps(x,y)[1])
p_values.append(sp(x,y)[1])
p_values.append(kd(x,y)[1])


#b - the bootstrap

s=np.linspace(0,len(data)-1,len(data))

cor_ps=[]
p_ps=[]
cor_sp=[]
p_sp=[]
cor_kd=[]
p_kd=[]

for i in range(0,1000):
	xnew=[]
	ynew=[]
	for j in range(0,200):
		k=np.random.choice(s)
		xnew.append(data[k][0])
		ynew.append(data[k][1])
	cor_ps.append(ps(xnew,ynew)[0])
	p_ps.append(ps(xnew,ynew)[1])
	cor_sp.append(sp(xnew,ynew)[0])
	p_sp.append(sp(xnew,ynew)[1])
	cor_kd.append(kd(xnew,ynew)[0])
	p_kd.append(kd(xnew,ynew)[1])


#spearman expectation

#kendall expectation
k_e=2./np.pi*np.arcsin(0.9)
#pearsons expectation
p_e=0.9*(1-(1-0.9)**2/(2.*len(x)))

f=plt.figure(figsize=(7,8))
gs=gridspec.GridSpec(2,1)
a_b=plt.subplot(gs[0,0])
plt.hist(cor_ps,histtype='step',label='pearson')
plt.axvline(x=cos[0],ls='dashed')
plt.axvline(x=p_e,lw=2,label='pearson expectation value')
plt.hist(cor_sp,histtype='step',label='spearman',color='r')
plt.axvline(x=cos[1],ls='dashed',color='r')
plt.hist(cor_kd,histtype='step',label='kendall',color='g')
plt.axvline(x=cos[2],ls='dashed',color='g')
plt.axvline(x=k_e,color='g',lw=2,label='kendall expectation value')
#plt.xlabel('correlation coefficient',fontsize=16)
plt.legend(loc='upper left',fontsize=6)
a_b.tick_params(labelbottom='off')
f.text(.25,.8,'*dashed lines indicate \n correlation values of \n original data sample', ha='center', va='center',fontsize=8)
########################################################################3

#part c and d again - with outliers!!
x.append(-.6)
x.append(-.76)
x.append(-2)
y.append(-2.1)
y.append(.92)
y.append(-5)

cos.append(ps(x,y)[0])
cos.append(sp(x,y)[0])
cos.append(kd(x,y)[0])
p_values.append(ps(x,y)[1])
p_values.append(sp(x,y)[1])
p_values.append(kd(x,y)[1])


#b - the bootstrap

s=np.linspace(0,len(data)-1,len(data))

cor_ps=[]
p_ps=[]
cor_sp=[]
p_sp=[]
cor_kd=[]
p_kd=[]

for i in range(0,1000):
	xnew=[]
	ynew=[]
	for j in range(0,200):
		k=np.random.choice(s)
		xnew.append(data[k][0])
		ynew.append(data[k][1])
	cor_ps.append(ps(xnew,ynew)[0])
	p_ps.append(ps(xnew,ynew)[1])
	cor_sp.append(sp(xnew,ynew)[0])
	p_sp.append(sp(xnew,ynew)[1])
	cor_kd.append(kd(xnew,ynew)[0])
	p_kd.append(kd(xnew,ynew)[1])


#spearman expectation

#kendall expectation
k_e=2./np.pi*np.arcsin(0.9)
#pearsons expectation
p_e=0.9*(1-(1-0.9)**2/(2.*len(x)))

e=plt.subplot(gs[1,0],sharex=a_b)
plt.hist(cor_ps,histtype='step',label='pearson')
plt.axvline(x=cos[0],ls='dashed')
plt.axvline(x=p_e,lw=2,label='pearson expectation value')
plt.hist(cor_sp,histtype='step',label='spearman',color='r')
plt.axvline(x=cos[1],ls='dashed',color='r')
plt.hist(cor_kd,histtype='step',label='kendall',color='g')
plt.axvline(x=cos[2],ls='dashed',color='g')
plt.axvline(x=k_e,color='g',lw=2,label='kendall expectation value')
plt.xlabel('correlation coefficient',fontsize=16)
plt.legend(loc='upper left',fontsize=6)
plt.title('including outliers')

plt.savefig('HW2_prob1.pdf')

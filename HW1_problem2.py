import pyfits
import numpy as np

data = pyfits.open('distribution.fits')

data=data[0].data

x=data[0]
y=data[1]

#normalize distribution:

y=y/np.sum(y)


#calculate mean:
mean=0
for i,value in enumerate(x):
	mean+=value*y[i]

#calculate median:
tot=0
median=0
for i,value in enumerate(x):
	tot+=y[i]
	if tot>0.5:
		median=value
		break

#calculate median:
tot=0
std=0
width=x[1]-x[0]
for i,value in enumerate(x):
	tot+=y[i]*width
	if tot>0.18:
		std=abs(mean-value)
		break


#Part c - generate random sample from distribution:
#I make a distribution of x values using frequencies given by the pdf, then use random.choice to select N random variables from that list. 
yhist=[int(value*1000000) for value in y]

newdist=[]
for i,value in enumerate(x):
	for j in range(0,yhist[i]):
		newdist.append(value)


#pick 5 values from list:
list5=[]
for i in range(0,5):
	list5.append(random.choice(newdist))
mean5=np.average(list5)
std5=np.std(list5)


#Part d - Do part c 100 times
meanlist5=[]
stdlist5=[]
for j in range(0,100):
	list5=[]
	for i in range(0,5):
		list5.append(random.choice(newdist))
	meanlist5.append(np.average(list5))
	stdlist5.append(np.std(list5))

#Part e - Do part d for N=5,50,500,5000,50000 samples
#N=50
meanlist50=[]
stdlist50=[]
for j in range(0,100):
	list50=[]
	for i in range(0,50):
		list50.append(random.choice(newdist))
	meanlist50.append(np.average(list50))
	stdlist50.append(np.std(list50))
#N=500
meanlist500=[]
stdlist500=[]
for j in range(0,100):
	list500=[]
	for i in range(0,500):
		list500.append(random.choice(newdist))
	meanlist500.append(np.average(list500))
	stdlist500.append(np.std(list500))
#N=5000
meanlist5000=[]
stdlist5000=[]
for j in range(0,100):
	list5000=[]
	for i in range(0,5000):
		list5000.append(random.choice(newdist))
	meanlist5000.append(np.average(list5000))
	stdlist5000.append(np.std(list5000))
#N=50000
meanlist50000=[]
stdlist50000=[]
for j in range(0,100):
	list50000=[]
	for i in range(0,50000):
		list50000.append(random.choice(newdist))
	meanlist50000.append(np.average(list50000))
	stdlist50000.append(np.std(list50000))



f=plt.figure(figsize = (16,10))
gs=gridspec.GridSpec(2,3)

a=plt.subplot(gs[0,0])
plt.scatter(x,y)
f.text(.15,.8,'mean = %s \n median = %s \n s.dev = %s'%(round(mean,2),round(median,2),round(std,2)),fontsize=14)
plt.title('pdf',fontsize=12)

b=plt.subplot(gs[0,1])
plt.hist(newdist,bins=50)
plt.title('pdf histogram with N_sample = 10,0000',fontsize=12)

c=plt.subplot(gs[0,2])
plt.hist(list5)
plt.ylim(0,4)
f.text(.69,.8, 'mean = %s \n st.dev = %s'%(round(mean5,2),round(std5,2)))
plt.title('random sample of 5 values',fontsize=12)

d=plt.subplot(gs[1,0])
plt.hist(meanlist5)
f.text(.13,.41,'mean of means = %s'%(round(np.average(meanlist5),2)))
plt.title('100 samples of N=5')

e=plt.subplot(gs[1,1:])
plt.hist(meanlist5,label='N=5, mean = %s'%round(np.average(meanlist5),2),histtype='step')
plt.hist(meanlist50,label='N=50, mean = %s'%round(np.average(meanlist50),2),histtype='step')
plt.hist(meanlist500,label='N=500, mean = %s'%round(np.average(meanlist500),2),histtype='step')
plt.hist(meanlist5000,label='N=5000, mean = %s'%round(np.average(meanlist5000),2),histtype='step')
plt.hist(meanlist50000,label='N=50000, mean = %s'%round(np.average(meanlist50000),2),histtype='step')
plt.title('100 samples of varying N')
plt.legend(loc=2)



plt.savefig('HW1_problem2.pdf')



import pyfits
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy.stats

x=np.linspace(-10,10,1000)



f=plt.figure(figsize = (15,10))
gs=gridspec.GridSpec(2,3)

gauss=plt.subplot(gs[0,0])
plt.plot(x,stats.norm(0,1).pdf(x),label='mu=0,sdv=1')
plt.plot(x,stats.norm(0,2).pdf(x),label='mu=0,sdv=2')
plt.plot(x,stats.norm(1,1).pdf(x),label='mu=1,sdv=1')
plt.plot(x,stats.norm(2,2).pdf(x),label='mu=2,sdv=2')
plt.legend(loc=2,prop={'size':8})
plt.title('Gaussian pdf')

binom=plt.subplot(gs[0,1])
plt.plot(x,stats.binom(0,1).ppf(x),label='mu=0,sdv=1')
plt.plot(x,stats.binom(0,2).ppf(x),label='mu=0,sdv=2')
plt.plot(x,stats.binom(1,1).ppf(x),label='mu=1,sdv=1')
plt.plot(x,stats.binom(2,2).ppf(x),label='mu=2,sdv=2')
plt.legend(loc=2,prop={'size':8})
plt.title('Binomial pdf')


poisson=plt.subplot(gs[0,2])
plt.plot(x,stats.poisson(0,1).ppf(x),label='mu=0,sdv=1')
plt.plot(x,stats.poisson(0,2).ppf(x),label='mu=0,sdv=2')
plt.plot(x,stats.poisson(1,1).ppf(x),label='mu=1,sdv=1')
plt.plot(x,stats.poisson(2,2).ppf(x),label='mu=2,sdv=2')
plt.legend(loc=2,prop={'size':8})
plt.title('Poisson pdf')

gausscdf=plt.subplot(gs[1,0])
plt.plot(x,stats.norm(0,1).cdf(x),label='mu=0,sdv=1')
plt.plot(x,stats.norm(0,2).cdf(x),label='mu=0,sdv=2')
plt.plot(x,stats.norm(1,1).cdf(x),label='mu=1,sdv=1')
plt.plot(x,stats.norm(2,2).cdf(x),label='mu=2,sdv=2')
plt.legend(loc=2,prop={'size':8})
plt.title('Guassian cdf')

binomcdf=plt.subplot(gs[1,1])
plt.plot(x,stats.binom(0,1).cdf(x),label='mu=0,sdv=1')
plt.plot(x,stats.binom(0,2).cdf(x),label='mu=0,sdv=2')
plt.plot(x,stats.binom(1,1).cdf(x),label='mu=1,sdv=1')
plt.plot(x,stats.binom(2,2).cdf(x),label='mu=2,sdv=2')
plt.legend(loc=2,prop={'size':8})
plt.title('Binomial cdf')

poissoncdf=plt.subplot(gs[1,2])
plt.plot(x,stats.poisson(0,1).cdf(x),label='mu=0,sdv=1')
plt.plot(x,stats.poisson(0,2).cdf(x),label='mu=0,sdv=2')
plt.plot(x,stats.poisson(1,1).cdf(x),label='mu=1,sdv=1')
plt.plot(x,stats.poisson(2,2).cdf(x),label='mu=2,sdv=2')
plt.legend(loc=2,prop={'size':8})
plt.title('Poisson cdf')

plt.savefig('HW1_problem3.pdf')



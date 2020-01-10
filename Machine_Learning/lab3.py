import numpy as np
import matplotlib.pyplot as pl
from scipy import stats as st

mean, sd = 0, 1
x = np.linspace(mean - 6 * sd, mean + 6 * sd, 100)
f = st.norm.pdf(x=x, loc=mean, scale=sd)
F = st.norm.cdf(x=x, loc=mean, scale=sd)
pl.figure(figsize=(10, 5))
pl.subplot(121)
pl.stem(x, f)
pl.xlabel('x')
pl.ylabel('f(x)')
pl.title('pdf with mean={} and s.d.={}'.format(mean, sd))
pl.subplot(122)
pl.stem(x, F)
pl.xlabel('x')
pl.ylabel('F(x)')
pl.title('cdf with mean={} and s.d.={}'.format(mean, sd))
pl.show()
print('-----' * 10)
# Exercise 1.2.1
M, n, N = 100, 25, 15
x = np.arange(0, n + 1)
f = st.hypergeom.pmf(x, M, n, N)
F = st.hypergeom.cdf(x, M, n, N)
pl.figure(figsize=(10, 5))
pl.subplot(121)
pl.stem(x, f)
pl.xlabel('x')
pl.ylabel('f(x)')
pl.title('pdf with M={}, n={} and N={}'.format(M, n, N))
pl.subplot(122)
pl.stem(x, F)
pl.xlabel('x')
pl.ylabel('F(x)')
pl.title('cdf with M={}, n={} and N={}'.format(M, n, N))
pl.show()
print('-----' * 10)
# Sampling from a distribution
mu, sigma = 0, 0.1
samples = np.random.normal(mu, sigma, 1000)
count, bins, ignore = pl.hist(samples, bins=30, normed=True)
pl.show()
# Normal distribution
mean = (0, 0)
cov = [[1, 1], [1, 10]]
x, y = np.random.multivariate_normal(mean, cov, 100000).T
pl.hist2d(x, y, 25, normed=True)
pl.xlabel('x')
pl.ylabel('y')
pl.colorbar()
pl.axis('equal')
pl.show()
del x, y

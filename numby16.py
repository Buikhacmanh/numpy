import numpy as np
m, sigma = 0, 0.1 # mean và standard deviation
s = np.random.normal(mu, sigma, size=5)
s
array([1.04652266, 1.01122791, 1.17575078, 0.92608879, 1.06772102])
np.random.randn(3, 3)
array([[ 0.03777261, -0.13544849, -0.01002595],
       [ 1.67080819, -0.66437971, -0.60555494],
       [-0.65099088,  0.51256776,  0.26238882]])
sigma * np.random.randn(...) + m
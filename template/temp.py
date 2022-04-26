import numpy as np
from numpy import linalg as LA

M = [[0, 1],[0,0]]

e, v = LA.eig(M)

t = e * np.log(e)


print(-np.sum(t))

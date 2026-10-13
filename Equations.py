import numpy as np

coef = np.array([[2,1],[1,3]])
res = np.array([8,13])

print(np.linalg.solve(coef,res))
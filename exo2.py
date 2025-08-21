import numpy as np
from scipy.optimize import minimize

def c(X):
    x, y = X
    return (x)**2 + (y)**2 - 3*x - 4*y + x*y

x0 = np.array([0.0, 0.0]) 
result = minimize(c, x0, method='BFGS')
print("Solution optimale :", result.x)
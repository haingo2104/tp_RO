import numpy as np
from scipy.optimize import minimize

def l(X):
    x , y = X
    return 3*(x)**2 + 2*(y)**2 + x*y
constraint = {'type' : 'eq' , 'fun':lambda X: X[0] + X[1] -100}
x0 = np.array([0.0,0.0])

result = minimize(l,x0,constraints=[constraint],method='SLSQP')

print("Répartition optimale (x, y) :", result.x)
print("Valeur minimale :", result.fun)
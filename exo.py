import numpy as np
from scipy.optimize import minimize

# Fonction à minimiser
def f(X):
    x, y = X
    return (x - 1)**2 + (y - 2)**2 + x*y

# Point initial
x0 = np.array([0.0, 0.0])

# Minimisation avec BFGS
result = minimize(f, x0, method='BFGS')

# Affichage des résultats
print("Solution optimale :", result.x)
print("Valeur minimale :", result.fun)

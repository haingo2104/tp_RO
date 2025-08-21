import numpy as np
from scipy.optimize import minimize

# Fonction objectif
def f(X):
    x, y = X
    return (x - 2)**2 + (y + 1)**2

# Contrainte d'égalité x + 2y = 3
constraint = {'type': 'eq', 'fun': lambda X: X[0] + 2*X[1] - 3}

# Point initial
x0 = np.array([0.0, 0.0])

# Minimisation
result = minimize(f, x0, constraints=[constraint], method='SLSQP')

# Résultat
print("Solution optimale (x, y) :", result.x)
print("Valeur minimale :", result.fun)

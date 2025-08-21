from scipy.optimize import linprog

# Fonction objectif
c = [-5, -4]

# Contraintes
A_ub = [
    [3, 2],
    [1, 2]
]
b_ub = [18, 12]

# Bornes
bounds = [(0, None), (0, None)]

# Résolution
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Affichage
if result.success:
    print("Solution optimale trouvée :")
    print(f"Tâches CPU (x1) = {result.x[0]:.2f}")
    print(f"Tâches I/O (x2) = {result.x[1]:.2f}")
    print(f"Gain maximal Z = {-result.fun:.2f}")
else:
    print("Échec :", result.message)

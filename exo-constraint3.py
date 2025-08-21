import utils.session
from scipy.optimize import linprog

# Fonction objectif (on met -3 et -2 car linprog fait une minimisation)
c = [-3, -2]

# Contraintes d'inégalité A_ub * x <= b_ub
A_ub = [
    [1, 1],  # x + y <= 4
    [1, 0],  # x <= 2
    [0, 1]   # y <= 3
]
b_ub = [4, 2, 3]

# Bornes sur les variables (x >= 0, y >= 0)
bounds = [(0, None), (0, None)]

# Résolution
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

# Affichage du résultat
if result.success:
    print("Solution optimale trouvée :")
    print(f"x = {result.x[0]:.2f}, y = {result.x[1]:.2f}")
    print(f"Valeur optimale de Z = {-result.fun:.2f}")  # attention, on remet le signe -
else:
    print("Échec de la résolution :", result.message)

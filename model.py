from sklearn.linear_model import LinearRegression
import numpy as np


# Tworzymy prosty model liniowy
model = LinearRegression()

# Generujemy sztuczne dane do treningu
X = np.array([[1], [2], [3], [4], [5]]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

# Trenujemy model
model.fit(X, y)
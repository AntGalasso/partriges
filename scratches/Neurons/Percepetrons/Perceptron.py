import numpy as np

# Dati: [x1, x2], y
data = np.array([
    [2, 3,  1],
    [3, 3,  1],
    [4, 5,  1],
    [1, 1, -1],
    [2, 1, -1],
    [3, 0, -1]
])

# Inizializzazione
w = np.zeros(2)
b = 0
learning_rate = 0.1

def sign(x):
    return 1 if x >= 0 else -1

# Algoritmo del percettrone
for epoch in range(10):  # puoi aumentare se vuoi
    for point in data:
        x = point[:2]
        y_true = point[2]
        y_pred = sign(np.dot(w, x) + b)
        if y_pred != y_true:
            w += learning_rate * y_true * x
            b += learning_rate * y_true

print(f"Pesi trovati: w = {w}, bias = {b}")

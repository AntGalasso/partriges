import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#logical dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 0, 0, 1])  # solo (1,1) è classe 1

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Funzione per calcolare la probabilità predetta
def predict(X, w, b):
    return sigmoid(np.dot(X, w) + b)

# Inizializzazione pesi e bias
w = np.array([0.5, 0.5])
b = 0.0
eta = 0.1
epochs = 30

# Per salvare la storia dei parametri
weights_history = [w.copy()]
bias_history = [b]

# Addestramento
for epoch in range(epochs):
    for i in range(len(X)):
        x_i = X[i]
        y_i = y[i]
        z = np.dot(x_i, w) + b
        y_hat = sigmoid(z)
        error = y_hat - y_i
        w -= eta * error * x_i
        b -= eta * error
    weights_history.append(w.copy())
    bias_history.append(b)

# Preparazione animazione
fig, ax = plt.subplots()
points_0 = X[y == 0]
points_1 = X[y == 1]
scatter_0 = ax.scatter(points_0[:, 0], points_0[:, 1], color='red', label='Classe 0')
scatter_1 = ax.scatter(points_1[:, 0], points_1[:, 1], color='blue', label='Classe 1')
line, = ax.plot([], [], 'k--', label='Decision boundary')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_title('Regressione Logistica: AND con Gradient Descent')
ax.legend()

# Funzione di aggiornamento per l'animazione
def update(frame):
    w = weights_history[frame]
    b = bias_history[frame]
    x_vals = np.array([-0.5, 1.5])
    if w[1] != 0:
        y_vals = -(w[0] * x_vals + b) / w[1]
    else:
        y_vals = np.array([0, 0])
    line.set_data(x_vals, y_vals)
    ax.set_title(f'Epoca {frame}')
    return line,

ani = FuncAnimation(fig, update, frames=len(weights_history), interval=300, repeat=False)

# MOSTRA ANIMAZIONE
plt.show()

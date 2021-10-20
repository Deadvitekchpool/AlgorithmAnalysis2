import random
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import brute
from scipy.optimize import minimize

alpha = random.uniform(0, 1)
beta = random.uniform(0, 1)

x_k = []
y_k = []

for i in range(0, 101):
	d = np.random.normal(0, 1)
	temp_x = i / 100
	temp_y = alpha * temp_x + beta + d
	x_k.append(temp_x)
	y_k.append(temp_y)

x_k = np.array(x_k)
y_k = np.array(y_k)

def f(x, a, b):
	return a * x + b

def D(params):
	global x_k, y_k

	a, b = params

	return np.sum((f(x_k, a, b) - y_k)**2)

brute_force = brute(D, ([0, 1], [0, 1]), Ns = 1 / 0.001)

gauss = minimize(D, [0, 0], method="Powell", tol=0.001)

nelder_mead = minimize(D, [0, 0], method="Nelder-Mead", tol=0.001)

plt.title("Linear approximant")
plt.scatter(x_k, y_k, label="Generated data", color='orange')
plt.plot(x_k, alpha * x_k + beta, "r", label="Generative line")
plt.plot(x_k, brute_force[0] * x_k + brute_force[1], label="Exhaustive search", color='green')
plt.plot(x_k, gauss.x[0] * x_k + gauss.x[1], label="Gauss method", color='purple')
plt.plot(x_k, nelder_mead.x[0] * x_k + nelder_mead.x[1], label="Nelder-Mead method", color='blue')
plt.grid()
plt.legend()
plt.show()
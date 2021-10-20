import math
import numpy as np

def f(x, alg):
	if alg == 1:
		return x**3
	elif alg == 2:
		return abs(x - 0.2)
	elif alg == 3:
		return x * math.sin(1/x)

def brute_force(a, b, e):
	n = math.floor((b - a) / e)
	x = []

	for k in range(0, n + 1):
		temp = a + k * ((b - a) / n)
		x.append(temp)

	f_vals = [f(xk, 2) for xk in x]

	x_min = f_vals.index(min(f_vals))

	return (x[x_min], len(f_vals))



res = brute_force(0.01, 1.0, 0.001)
print("x_min: " + str(res[0]))
print("f was called " + str(res[1]) + " times")
print("The algorithm had " + str(res[1]) + " iterations")
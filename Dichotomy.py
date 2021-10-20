import math
import numpy as np
import random

def f(x, alg):
	if alg == 1:
		return x**3
	elif alg == 2:
		return abs(x - 0.2)
	elif alg == 3:
		return x * math.sin(1/x)

def dichotomy(a, b, e):
	d = random.uniform(0, e)
	x1 = 0
	x2 = 0
	f_calls = 0
	while abs(a - b) >= e:
		x1 = (a + b - d) / 2
		x2 = (a + b + d) / 2
		if f(x1, 2) <= f(x2, 2):
			b = x2
		else:
			a = x1
		f_calls += 2

	return (a, b, f_calls)

res = dichotomy(0.01, 1.0, 0.001)
print("[x1, x2]: [" + str(res[0]) + ", " + str(res[1]) + "]")
print("f was called " + str(res[2]) + " times")
print("The algorithm had " + str(res[2] / 2) + " iterations")
import math

def f(x, alg):
	if alg == 1:
		return x**3
	elif alg == 2:
		return abs(x - 0.2)
	elif alg == 3:
		return x * math.sin(1/x)

def gs(a, b, e):
	x1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
	x2 = b + (math.sqrt(5) - 3) / 2 * (b - a)
	y1 = f(x1, 2)
	y2 = f(x2, 2)
	f_calls = 2
	while abs(a - b) >= e:
		if y1 <= y2:
			b = x2
			x2 = x1
			y2 = y1
			x1 = a + (3 - math.sqrt(5)) / 2 * (b - a)
			y1 = f(x1, 2)
		else:
			a = x1
			x1 = x2
			y1 = y2
			x2 = b + (math.sqrt(5) - 3) / 2 * (b - a)
			y2 = f(x2, 2)

		f_calls += 1

	return (a, b, f_calls)

res = gs(0.0, 1.0, 0.001)
print("[x1, x2]: [" + str(res[0]) + ", " + str(res[1]) + "]")
print("f was called " + str(res[2]) + " times")
print("The algorithm had " + str(res[2]) + " iterations")
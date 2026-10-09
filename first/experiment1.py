import math
import numpy as np

p = 4

print("=" * 60)
print("Task 1")
a_values = [10**10, 10**12, 10**14, 10**16, 10**18, p * 10**16]
for a in a_values:
    b = -a
    c = 1.0
    r1 = (a + b) + c
    r2 = a + (b + c)
    print(f"a = {a:.6e}  (a+b)+c = {r1:.12e}  a+(b+c) = {r2:.12e}  same = {r1 == r2}")

print("=" * 60)
print("Task 2")
x_values = [10**2, 10**4, 10**8, 10**12, 10**16, p * 10**12]
for x in x_values:
    y1 = math.sqrt(x + 1) - math.sqrt(x)
    y2 = 1.0 / (math.sqrt(x + 1) + math.sqrt(x))
    print(f"x = {x:.6e}  y1 = {y1:.12e}  y2 = {y2:.12e}  |y1-y2| = {abs(y1-y2):.12e}")

print("=" * 60)
print("Task 3")
K = np.float32(p * 10**9)
one = np.float32(1.0)
a = np.float32(1.0)
b = -(K + one)
c = K
print(f"K = {float(K):.6e}")
print(f"K+1 (exact float) = {p * 10**9 + 1}")
print(f"float32(K+1) = {float(np.float32(K + one)):.6e}")
print(f"float32 of python int K+1 = {float(np.float32(p * 10**9 + 1)):.6e}")
print(f"b stored = {float(b):.6e}")

disc = np.float32(math.sqrt(np.float32(b * b - np.float32(4.0) * a * c)))
x1_A = (-b + disc) / (np.float32(2.0) * a)
x2_A = (-b - disc) / (np.float32(2.0) * a)
if abs(x1_A) < abs(x2_A):
    x1_A, x2_A = x2_A, x1_A
err_A = abs(x2_A - 1.0) / 1.0
print(f"Method A: x1 = {x1_A:.10e}  x2 = {x2_A:.10e}  rel err x2 = {err_A:.6e}")

sign_b = np.float32(1.0) if b >= 0 else np.float32(-1.0)
x1_B = (-b - sign_b * disc) / (np.float32(2.0) * a)
x2_B = c / (a * x1_B)
err_B = abs(x2_B - 1.0) / 1.0
print(f"Method B: x1 = {x1_B:.10e}  x2 = {x2_B:.10e}  rel err x2 = {err_B:.6e}")

print("=" * 60)
print("Task 4")
eps = p * 1e-6
print(f"eps = {eps:.6e}")
x = 2.0
xp = 2.0 + eps
y = 1.0 / x
yp = 1.0 / xp
rx = abs(xp - x) / abs(x)
ry = abs(yp - y) / abs(y)
print(f"Problem A: rx = {rx:.12e}  ry = {ry:.12e}")

x = 1.0 + eps
xp = 1.0 + 2 * eps
y = 1.0 / (x - 1.0)
yp = 1.0 / (xp - 1.0)
rx = abs(xp - x) / abs(x)
ry = abs(yp - y) / abs(y)
print(f"Problem B: rx = {rx:.12e}  ry = {ry:.12e}")

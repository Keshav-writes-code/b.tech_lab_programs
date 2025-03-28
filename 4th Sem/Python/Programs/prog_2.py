import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
import scipy

# EXPONENTIAL FUNCTION
a = scipy.special.exp10(3)
print(a)
b = scipy.special.exp2(3)
print(b)

# TRIGONOMETRIC FUNCTION
c = scipy.special.cosdg(90)
print(c)
d = scipy.special.sindg(90)
print(d)

# INTEGRATION FUNCTION
i = scipy.integrate.quad(lambda x: scipy.special.exp10(x), 0, 1)
print(i)

# DOUBLE INTEGRATION
def e(x, y): return x * y * 2
def f(x): return 1
def g(x): return -1
scipy.integrate.dblquad(e, 0, 2, f, g)

# FOURIER TRANSFORMATION
x = np.array([1, 2, 3, 4])
y = fft(x)
print(y)

# Linear Algebra
a = np.array([[1, 2], [3, 4]])
b = scipy.linalg.inv(a)
print(b)
a = np.array([1, 2, 3, 4]).reshape(2, 2)
b = scipy.linalg.inv(a)
print(b)

#  Interpolation function
x = np.arange(5, 20)
y = np.exp(x / 3.0)
f = scipy.interpolate.interp1d(x, y)
x1 = np.arange(6, 12)
y1 = f(x1)
plt.plot(x, y, 'o', x1, y1, '--')
plt.show()

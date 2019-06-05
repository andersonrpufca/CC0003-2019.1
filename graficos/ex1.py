# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

# Dados
x = np.arange(0.0, 2.0, 0.01)
a = (x ** 2 + np.cos(x)) / 4
b = np.cos(x) / (4 - x)
c = x ** 3 - 5 * x ** 2 + 7 * x - 3
d = x ** 3 - 0.25 * x ** 2 + 0.75 * x - 2
e = np.sin(x) - math.exp(1) ** x
f = math.exp(1) ** x - 4 * x ** 2
fig, ax = plt.subplots()
ax.plot(x, a,label="A")
ax.plot(x ,b,label="B")
ax.plot(x ,c,label="C")
ax.plot(x ,d,label="D")
ax.plot(x ,e,label="E")
ax.plot(x ,f,label="F")

ax.set(xlabel='x', ylabel='f(x)')
ax.grid()
ax.legend()
plt.show()
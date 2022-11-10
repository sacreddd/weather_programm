import matplotlib.pyplot as plt
import random as r
import numpy as np



k_o = []
for i in range(24):
    k_o.append(r.randint(0, 100))
t = []
for i in range(24):
    t.append(r.randint(-3, 3))

s_v = []
for i in range(24):
    s_v.append(r.randint(1, 3))
v = []
for i in range(24):
    v.append(r.randint(72, 77))

plt.subplot(2,2,1)
plt.plot(k_o)
plt.xticks(np.arange(0, 24))

plt.subplot(2,2,2)
plt.plot(t)
plt.xticks(np.arange(0, 24))

plt.subplot(2,2,3)
plt.plot(s_v)
plt.xticks(np.arange(0, 24))

plt.subplot(2,2,4)
plt.plot(v)
plt.xticks(np.arange(0, 24))

plt.show()

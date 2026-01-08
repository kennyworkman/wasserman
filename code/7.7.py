import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

mags = []
with open('fijiquakes.dat') as f:
    header = True
    for x in f.readlines():
        if header:
            header = False
            continue
        obs, lat, long, depth, mag, stations = x.strip().split()
        mags.append(mag)

mags = np.array(mags, dtype=float)
n = mags.size
def emp_cdf(x: float):
    return np.sum(mags <= x) / n

epsilon_n = math.sqrt((1 / (2*n))*math.log(2 / 0.05))

def L(x: float):
    return emp_cdf(x) - epsilon_n

def U(x: float):
    return emp_cdf(x) + epsilon_n

xs = np.sort(mags)
ys = [emp_cdf(x) for x in xs]
ls = [L(x) for x in xs]
us = [U(x) for x in xs]
plt.fill_between(xs, ls, us, alpha=0.3, step='pre', label='95% CI')
plt.step(xs, ys, label='F_n')
plt.legend()
plt.savefig('7.7.pdf')

# CI for F(4.9) - F(4.3)

z = norm.ppf(1 - 0.05/2)
theta_hat = emp_cdf(4.9) - emp_cdf(4.3)
epsilon = math.sqrt((theta_hat * (1-theta_hat)) / n)*z

L = theta_hat - epsilon
U = theta_hat + epsilon

print(L, U)

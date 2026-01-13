import numpy as np
import matplotlib.pyplot as plt

alpha = 0.05
p = 0.4
ns = np.arange(1, 10001)
coverage = []
lengths = []

for n in ns:
    eps = np.sqrt(np.log(2/alpha)/(2*n))
    sims = np.random.binomial(n, p, size=1000)/n
    covered = np.mean((p >= sims - eps) & (p <= sims + eps))
    coverage.append(covered)
    lengths.append(2*eps)

plt.figure()
plt.plot(ns, coverage)
plt.axhline(1-alpha, color='red', linestyle='--')
plt.title("Coverage vs n")
plt.xlabel("n")
plt.ylabel("Coverage")

plt.figure()
plt.plot(ns, lengths)
plt.title("Interval Length vs n")
plt.xlabel("n")
plt.ylabel("Length")
plt.show()

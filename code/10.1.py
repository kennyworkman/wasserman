import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 25
sigma = 1
alpha = 0.05
c = sigma * norm.ppf(1 - alpha) / np.sqrt(n)

mu = np.linspace(-1.5, 2, 500)
beta = 1 - norm.cdf(np.sqrt(n) * (c - mu) / sigma)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(mu, beta, linewidth=2)
ax.axhline(y=alpha, color="r", linestyle="--", label=rf"$\alpha = {alpha}$")
ax.axvline(x=0, color="gray", linestyle=":", alpha=0.5)
ax.plot(0, alpha, "ro", markersize=8)
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\beta(\mu)$")
ax.set_title(r"Power function: reject $H_0$ if $\bar{X} > c$")
ax.legend()
fig.tight_layout()

plt.savefig("10.1.pdf")

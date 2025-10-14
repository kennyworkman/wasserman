import numpy as np
import matplotlib.pyplot as plt

samples = 10000

Xs = np.random.normal(loc=0, scale=1, size=samples)
Ys = np.exp(Xs)

print(Xs)
print(Ys)

pdf_domain = np.linspace(0, np.percentile(Ys, 99.5), 1000)

pdf = 1 / (pdf_domain * np.sqrt(1 * np.pi)) * np.exp(-1/2 * np.log(pdf_domain)**2)

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(Ys, bins=80, density=True, alpha=0.6, label="simulated Y", edgecolor="black")
ax.plot(pdf_domain, pdf, linewidth=2, label="theoretical pdf")
ax.set_xlabel("y")
ax.set_ylabel("density")
ax.set_title(r"Histogram of $Y=e^{X}$ ($X\sim N(0,1)$) with log-normal pdf overlay")
ax.legend()
ax.set_xlim(left=0)
fig.tight_layout()

plt.savefig("2.13.pdf")

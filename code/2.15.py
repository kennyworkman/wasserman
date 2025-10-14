import numpy as np
import matplotlib.pyplot as plt

beta = 1
samples = 10000

Us = np.random.uniform(0, 1, samples)
F_inverse = -(1/beta)*np.log(1 -(beta**2)*Us)

print(Us)
print(F_inverse)

exp_domain = np.linspace(0, np.percentile(F_inverse, 99.5), 1000)
exp_pdf = (1/beta)*np.exp(-exp_domain / beta)

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(F_inverse, bins=80, density=True, alpha=0.6, label="generated", edgecolor="black")
ax.plot(exp_domain, exp_pdf, linewidth=2, label="theoretical pdf")
fig.tight_layout()

plt.savefig("2.15.pdf")

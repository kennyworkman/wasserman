import numpy as np
import matplotlib.pyplot as plt

n_values = np.arange(1, 101)

E_Xn = np.full_like(n_values, 0.5, dtype=float)   # always 1/2
Var_Xn = 1 / (12 * n_values)                      # 1/(12n)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(n_values, E_Xn, label="E[X̄ₙ]")
plt.xlabel("n")
plt.ylabel("Expectation")
plt.title("Expectation of Sample Mean")
plt.ylim(0,1)
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
plt.plot(n_values, Var_Xn, label="Var(X̄ₙ)")
plt.xlabel("n")
plt.ylabel("Variance")
plt.title("Variance of Sample Mean")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("3.19.1.pdf")

n_values = [1, 5, 25, 100]
num_trials = 100000

plt.figure(figsize=(12,8))

for i, n in enumerate(n_values, 1):
    samples = np.random.rand(num_trials, n).mean(axis=1)

    plt.subplot(2,2,i)
    plt.hist(samples, bins=50, density=True, alpha=0.7, color="steelblue")
    plt.axvline(0.5, color="red", linestyle="--", label="theoretical mean = 0.5")
    plt.title(f"Sampling distribution of X̄ₙ, n={n}")
    plt.xlabel("X̄ₙ")
    plt.ylabel("Density")
    plt.legend()

plt.tight_layout()
plt.savefig("3.19.2.pdf")

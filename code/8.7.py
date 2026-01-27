import numpy as np
import matplotlib.pyplot as plt

n = 50
theta = 1
X = np.random.uniform(0, theta, size=n)
theta_hat = np.max(X)

B = 10000
boot_maxes = [np.max(np.random.choice(X, size=n, replace=True)) for _ in range(B)]

x = np.linspace(0, theta, 500)
true_density = n * x**(n-1) / theta**n

plt.hist(boot_maxes, bins=50, density=True, alpha=0.7, label='Bootstrap')
plt.plot(x, true_density, 'r-', linewidth=2, label='True density')
plt.xlabel('θ̂')
plt.ylabel('Density')
plt.legend()
plt.savefig('8.7.pdf')

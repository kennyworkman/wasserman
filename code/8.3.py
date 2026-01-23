import math

import numpy as np
from scipy.stats import t, norm

n = 25
X = t.rvs(df=3, size=25)

# This is now *all* of my observed data. We can compute our plug-in estimate
# for theta.

def T(X) -> float:
    q75 = np.quantile(X, 0.75)
    q25 = np.quantile(X, 0.25)
    return (q75 - q25) / 1.34

theta_hat = T(X)

print(f"Theta_hat: {theta_hat}")

# We can also compute the bootstrap replications of our estimator
B = 1000
replicates = []
for i in range(B):
    X_boot = np.random.choice(X, size=n, replace=True)
    replicates.append(T(X_boot))

def sample_mean(x) -> float:
    return sum(x) / len(x)

alpha = 0.05

# Let's now explore the bootstrap CI.
# 1/ Normal 

v_boot = sample_mean(list(map(lambda x: x*x, replicates))) - (sample_mean(replicates)) ** 2

se_boot = math.sqrt(v_boot)
z = norm.ppf(1-alpha/2)

print(f"Normal CI: ({theta_hat - se_boot * z}, {theta_hat + se_boot * z})")

# 2/ Pivotal intervals
print(f"Pivotal CI: ({2*theta_hat - np.quantile(replicates, 1-alpha/2)}, {2*theta_hat - np.quantile(replicates, alpha/2)})")

# 3/ Percentile intervals
print(f"Percentile CI: ({np.quantile(replicates, alpha/2)}, {np.quantile(replicates, 1-alpha/2)})")

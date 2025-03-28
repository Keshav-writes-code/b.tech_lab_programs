import numpy as np
import matplotlib.pyplot as plt

# Define parameters
population_distribution = np.random.exponential(scale=2, size=10000)  # Example: exponential distribution
sample_size = 100  # Size of each sample
num_samples = 1000  # Number of samples to generate

# Generate random samples
samples = np.random.choice(population_distribution, size=(num_samples, sample_size))

# Compute the means of each sample
sample_means = np.mean(samples, axis=1)

# Plot the histogram of sample means
plt.hist(sample_means, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7)

# Plot the theoretical normal distribution (CLT prediction)
mu = np.mean(population_distribution)
sigma = np.std(population_distribution) / np.sqrt(sample_size)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2)), color='red', linewidth=2)

plt.title('Central Limit Theorem')
plt.xlabel('Sample Mean')
plt.ylabel('Probability Density')
plt.legend(['Normal Distribution', 'Sample Means'])
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def discrete_pmf(data):
    unique, counts = np.unique(data, return_counts=True)
    pmf = counts / len(data)
    return unique, pmf

def continuous_pdf(data, bins=50):
    count, bins = np.histogram(data, bins=bins, density=True)
    pdf = count / np.sum(count)
    return bins[:-1], pdf

def continuous_cdf(data):
    x = np.sort(data)
    cdf = np.arange(1, len(x) + 1) / len(x)
    return x, cdf

# Sample data for discrete random variable
discrete_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Sample data for continuous random variable
continuous_data = np.random.normal(loc=0, scale=1, size=1000)

# Calculate PMF for discrete data
x_discrete, pmf_discrete = discrete_pmf(discrete_data)

# Calculate PDF for continuous data
x_continuous, pdf_continuous = continuous_pdf(continuous_data)

# Calculate CDF for continuous data
x_cdf, cdf_continuous = continuous_cdf(continuous_data)

# Plot PMF
plt.subplot(1, 3, 1)
plt.bar(x_discrete, pmf_discrete)
plt.title('Probability Mass Function (PMF)')
plt.xlabel('Values')
plt.ylabel('Probability')

# Plot PDF
plt.subplot(1, 3, 2)
plt.plot(x_continuous, pdf_continuous)
plt.title('Probability Density Function (PDF)')
plt.xlabel('Values')
plt.ylabel('Probability Density')

# Plot CDF
plt.subplot(1, 3, 3)
plt.plot(x_cdf, cdf_continuous)
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Values')
plt.ylabel('Cumulative Probability')

plt.tight_layout()
plt.show()

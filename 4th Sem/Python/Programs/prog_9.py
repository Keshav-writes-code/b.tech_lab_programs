import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def discrete_pmf(data):
    unique, counts = np.unique(data, return_counts=True)
    pmf = counts / len(data)
    return unique, pmf

def continuous_pdf(data, bins=50):
    count, bins = np.histogram(data, bins=bins, density=True)
    print(count)
    return 

discreate_data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
continuos_data = np.random.normal(loc=0, scale=1, size=1000)
x_discreate, pmf_discreate = discrete_pmf(discreate_data)

# x_continuos, pdf_continuous = continuous_pdf(continuos_data)

continuous_pdf(continuos_data)
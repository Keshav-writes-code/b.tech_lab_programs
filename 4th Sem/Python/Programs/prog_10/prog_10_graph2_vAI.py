import matplotlib.pyplot as plt
import numpy as np
import csv 
import os
dirname = os.path.dirname(__file__)
data = np.genfromtxt(os.path.join(dirname, 'salaries.csv'), delimiter=',', skip_header=1,dtype=str)

# - - - - - - - - 2nd Graph - - - - - - - - -
# - - - - Which Countries Pay higher - - - -
countries = np.unique(data[:, 9])

salaries = np.array([np.mean(data[data[:, 9] == country, 6].astype(float)) for country in countries])

countries_salaries = np.column_stack((countries, salaries))
sorted_indices = np.argsort(countries_salaries[:, 1].astype(float))[::-1]
countries_salaries = countries_salaries[sorted_indices]
print(countries_salaries)

endPoint = 10
x = countries_salaries[:endPoint, 0]
y = countries_salaries[:endPoint, 1].astype(float)


plt.barh(x[::-1], y[::-1])

plt.xlabel("Salaries (USD)")
plt.ylabel("Countries")
plt.title("Top 10 Countries that Pay Well")
plt.tight_layout()

plt.show()
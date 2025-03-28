import matplotlib.pyplot as plt
import numpy as np
import csv 
import os
dirname = os.path.dirname(__file__)
data = np.genfromtxt(os.path.join(dirname, 'salaries.csv'), delimiter=',', skip_header=1,dtype=str)

# - - - - - - - - 1st Graph - - - - - - - - -
# - - Salaries VS Hired Date of Employees - -
years = np.unique(data[:, 0])
salaries = np.array([])
std = np.array([])
for year in years:
    mask = data[:,0] == year
    salaries = np.append(salaries, np.mean(data[mask,6].astype(float)))
    std = np.append(std, np.std(data[mask,6].astype(float)))
plt.subplot(3,2,1)
plt.plot(years, salaries, marker='o')
plt.fill_between(years, salaries - np.array(std), salaries + np.array(std), alpha=0.3)
plt.xlabel("Year")
plt.ylabel("Salaries (USD)")
plt.title("Salaries VS Hire Year of Employees")

# - - - - - - - - 2nd Graph - - - - - - - - -
# - - - - Which Countries Pay higher - - - -
countries = np.array(list(set(data[:,9])))
salaries = np.array([])
for country in countries:
    mask = data[:,9] == country
    mean = int(np.mean(data[mask,6].astype(float)))
    salaries = np.append(salaries, mean)
countries_salaries = np.column_stack((countries, salaries))
sorted_indecies = np.argsort(countries_salaries[:, 1].astype(float))
countries_salaries = countries_salaries[sorted_indecies[::-1]]
plt.subplot(3,2,2)
endPoint = 10
x = countries_salaries[:endPoint,0]
y = countries_salaries[:endPoint,1].astype(float)
plt.barh(x[::-1], y[::-1])
plt.xlabel("Salaries (USD)")
plt.ylabel("Countries")
plt.title("Top 10 Countries that Pay Well")

# - - - - - - - - - - - 3rd Graph - - - - - - - - - - -
# - - - - Top 10 Countries Engineer Come From - - - - -
country_counts = np.unique(data[:,7], return_counts=True)
country_names, counts = country_counts
country_percentages = counts / len(data) * 100
country_counts_array = np.column_stack((country_names, country_percentages))
sorted_indecies = np.argsort(country_counts_array[:, 1].astype(float))
country_counts_array = country_counts_array[sorted_indecies[::-1]]
plt.subplot(3,2,3)
endPoint = 4
plt.pie(country_counts_array[:endPoint,1], labels=country_counts_array[:endPoint,0], startangle = 180)
plt.title("Top 4 Countries Engineer Come From")

# - - - - - - - - 4th Graph - - - - - - - - -
# - - - - Experience VS their Salary - - - - -
exp_labels = np.unique(data[:, 1])
salaries = np.array([])
std = np.array([])
for exp_label in exp_labels:
    mask = data[:,1] == exp_label
    salaries = np.append(salaries, np.mean(data[mask,6].astype(float)))
    std = np.append(std, np.std(data[mask,6].astype(float)))
plt.subplot(3,2,4)
plt.plot(exp_labels, salaries, marker='o')
plt.fill_between(exp_labels, salaries - np.array(std), salaries + np.array(std), alpha=0.3)
plt.xlabel("Expereince")
plt.ylabel("Salaries (USD)")
plt.title("Salaries VS Experience")

# - - - - - - - - 5th Graph - - - - - - - - -
# - - - - Which Jobs are Paying Well? - - - -
jobs = np.array(list(set(data[:,3])))
salaries = np.array([])

for job in jobs:
    mask = data[:,3] == job
    mean = int(np.mean(data[mask,6].astype(float)))
    salaries = np.append(salaries, mean)

jobs_salaries = np.column_stack((jobs, salaries))
sorted_indecies = np.argsort(jobs_salaries[:, 1].astype(float))
jobs_salaries = jobs_salaries[sorted_indecies[::-1]]

plt.subplot(3,1,3)
endPoint = 10
x = jobs_salaries[:endPoint,0]
y = jobs_salaries[:endPoint,1].astype(float)
plt.barh(x[::-1],y[::-1] )

plt.xlabel("Salaries (USD)")
plt.ylabel("Job Title")
plt.title("Top 10 Highest Paying Jobs")
plt.tight_layout()
plt.show()

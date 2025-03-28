import numpy as np

data = np.random.randint(0, 100, size=(10, 4))
print("dataset :-\n", data)

# calculate mean of the dataset
mean_data = np.mean(data, axis=0)
print("Mean of the dataset: ", mean_data)

# Calculate Meadian of the Dataset
median_data = np.median(data, axis=0)
print("Median of the dataset: ", median_data)

# Calculate Mode of the Dataset
mode_data = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=0, arr=data)
print("Mode of the dataset: ", mode_data)
import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = np.mean(speed)
print("Mean of Speed is: ", x)

x = np.median(speed)
print("Median of Speed is: ", x)

x = stats.mode(speed)
print("Mode of Speed is: ", x)

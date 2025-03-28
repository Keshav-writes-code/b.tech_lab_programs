import random as rd

def create_sample(population,sample_size):
    if sample_size>len(population):
        raise ValueError("Sample size cannot be larger than population size.")
    sample=rd.sample(population,sample_size)
    return sample

population=[1,2,3,4,5,6,7,8,9,10]
sample_size=5
sample=create_sample(population,sample_size)
print("Sample:",sample)
import numpy as np
import matplotlib.pyplot as plt
# Create a simple 2D dataset with two classes
np.random.seed(0)
X1= np.random.randn(50, 2) + np.array( [2, 2])
X2 = np.random.randn(50, 2) + np.array([-2, -2])
X = np.vstack([X1, X2])
y= np.array([1]*50+[-1]*50)

w = np.random.randn(2)
b = 0
learning_rate =0.1
iterations = 10
decision_boundaries = []


for _ in range(iterations):
  errors =0
  for i in range(len(X)):
    prediction = np.sign(np.dot(X[i], w) + b)
    if y[i] !=prediction:
      errors += 1
      w += learning_rate * y[i] * X[i]
      b += learning_rate* y[i]
  decision_boundaries.append((-w[0]/w[1],-b/w[1])) 


plt.scatter(X[:50,0],X[:50,1],color='blue',label='Class 1')
plt.scatter(X[50:,0],X[50:,1],color='red',label='Class -1')

for i, boundry in enumerate(decision_boundaries):
  plt.plot([boundry[0],boundry[0]], [-5,5],color='green',linestyle='--',label=f'iter {i+1}')
plt.title('Perceptron Learning: Decision Boundaries Over Iterations')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlabel("Feature 1")
plt.ylabel('Feature 2')
plt.show()
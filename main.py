import numpy as np
import matplotlib.pyplot as plt

vector1 = np.array([1,2])
vector2 = np.array([5,9])
scalar1 = 5
#Multiply the vector with a scalar
newvector1 = vector1 * scalar1
print(newvector1)
#Dotproduct between the 2 vectors
thedotproduct = np.dot(vector1,vector2)

plt.plot([3], [thedotproduct], 'bs-')
plt.plot(vector1, 'bs-')
plt.show()
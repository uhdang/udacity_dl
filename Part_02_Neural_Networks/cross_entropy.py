import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    sum = 0
    for i in range(len(Y)):
        yi = Y[i]
        pi = P[i]
        sum += -(yi * np.log(pi) + (1-yi) * np.log(1-pi))
    return sum
            

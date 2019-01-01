import numpy as np
import math

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def getSumOfEuler(L):
    sum = 0
    for i in L:
        sum += math.exp(i)
    return sum
        
def softmax(L):
    sum = getSumOfEuler(L)
    list = []
    for i in L:
        value = math.exp(i) / sum
        list.append(value)
    return list

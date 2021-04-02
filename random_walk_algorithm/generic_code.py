"""
Multivariant Random walk optimization
"""

import random as rnd 
from math import sqrt

def f(X):  # objective function
    # X is a vector of variables
    return X[0] - X[1] + 2*(X[0]**2) + 2*X[0]*X[1] + (X[1]**2)


def magnitude_cal(X):
    X_square = [x**2 for x in X]
    X_square_sum = sum(X_square)
    return sqrt(X_square_sum)


X = [0.0, 0.0]  # initial values of variables

stepLength = 1.0    
E = 0.05    # minimum allowed step length
total_iterations = 100
total_trials = 100

output = f(X)  # value of obj function with initial values of x1 and x2
print("Initial value of obj function: " + str(output))

for iteration in range (total_iterations):
    if stepLength > E:
        for trial in range(total_trials):

            randomNumber = [round(rnd.uniform(-1.0, 1.0), 2) for i in range(len(X))] # inline for loop
            mag = magnitude_cal(randomNumber)
            unit_vectors = [r/mag for r in randomNumber]
            # [unit1, unit2] = random1/mag, random2/mag
            # x1_, x2_ = (x1 + stepLength*unit1), (x2 + stepLength*unit2)
            X_ = []
            for i in range(len(X)):
                X_.append(round(X[i] + stepLength*unit_vectors[i], 3))
            
            output_ = f(X_)
            
            if output_ < output:    # minimizing problem
                X = X_
                output = output_
                print ("{:<10} {:<15} {:<15} {:<10}".format('iteration','step length','trials','f(x1,x2)'))
                print ("{:<10} {:<15} {:<15} {:<10.3f}".format(iteration, stepLength, trial,output))
                print("Value of variables are: ", str(X))
                print("= = " *5)
            
            elif output_ >= output:
                if(trial <= total_iterations):
                    continue
                else:
                    break   # breaking the trial loop and going to the next iteration

    else:
        break # breaking the iteration loop to stop the algorithm
    
    stepLength /=2


print("The function has reached its optimal solution!")
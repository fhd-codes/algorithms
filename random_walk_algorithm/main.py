import random as rnd 
from math import sqrt

def f(x1, x2):  # objective function
    return x1 - x2 + 2*(x1**2) + 2*x1*x2 + (x2**2)


x1, x2 = 0.0, 0.0
stepLength = 1.0
E = 0.05
total_iterations = 100
total_trials = 100

output = f(x1, x2)  # value of obj function with initial values of x1 and x2
print("Initial value of obj function: " + str(output))

for iteration in range (total_iterations):
    if stepLength > E:
        for trial in range(total_trials):
            random1, random2 = round(rnd.uniform(-1.0, 1.0), 2), round(rnd.uniform(-1.0, 1.0), 2)
            mag = sqrt(random1**2 + random2**2) 
            [unit1, unit2] = random1/mag, random2/mag
            x1_, x2_ = (x1 + stepLength*unit1), (x2 + stepLength*unit2)
            output_ = f(x1_, x2_)
            
            if output_ < output:    # minimizing problem
                x1, x2 = x1_, x2_
                output = output_
                print ("{:<10} {:<15} {:<15} {:<10} {:<10} {:<10}".format('iteration','step length','trials','x1','x2','f(x1,x2)'))
                print ("{:<10} {:<15} {:<15} {:<10.3f} {:<10.3f} {:<10.3f}".format(iteration, stepLength, trial, x1, x2, output))
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
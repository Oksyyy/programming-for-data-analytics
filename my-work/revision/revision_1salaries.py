# revision_salaries.py
# Program to generate 10 random salaries from between 20000 and 80000
# Author: Oksana Abrosimova 

import numpy as np

np.random.seed(1)

salaries  = np.random.randint(20000, 80000, 10)
# First number is minimum salary
# Second number is maximum salary
# Third number is how many numbers (salaries) to generate

np.random.seed(1)

print(salaries)
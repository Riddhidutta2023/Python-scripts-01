# This program takes two integers as input and calculates their GCD (Greatest Common Divisor) using the math.gcd function.
# It also generates a random integer between the two input integers using the random.randint function.

from math import gcd
from random import randint


#ask for two integers
input1 = int(input("Enter the first integer: "))
input2 = int(input("Enter the second integer: "))

#calculate the GCD
gcd_result = gcd(input1, input2)

random_integer = randint(input1, input2)
#display the result
print(f"The GCD of {input1} and {input2} is: {gcd_result}")
print(f"A random integer between {input1} and {input2} is: {random_integer}")   


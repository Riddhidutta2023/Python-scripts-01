# This program calculates the hypotenuse of a right triangle using the Pythagorean theorem.

from math import sqrt

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
hypotenuse = sqrt(base**2 + height**2)

print(f"The length of the hypotenuse is: {hypotenuse:.2f}")

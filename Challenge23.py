"""
Challenge 23
A gardener needs to buy some turf for a project they are working on. The garden is rectangular
with a circular flower bed in the middle.

Write a program that:
asks the user for the dimensions of the lawn and the radius of the circle (in metres)
uses a function to calculate and output the amount of turf needed
"""

import math

print ("Gardener Turf Calculator")

width = float(input ("Enter the width of the garden in metres: "))
height = float(input ("Enter the height of the garden in metres: "))
radius = float(input ("Enter the radius of the circular flower garden in metres: "))

totalTurf = (width * height) - (math.pi*radius**2)

print ("You will need to buy %.2f meters of turf" % totalTurf)
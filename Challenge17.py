"""
Challenge 17

Write a program that:
outputs all odd numbers between 1 and 99

"""

print ("Challenge 17: output all odd numbers between 1 and 99")

for i in range ( 1, 100):

    if i % 2 != 0: # a % b calculate the remainder of dividing a by b. Odd numbers always have a remainder if divided by 2+
        print ("%s " % i,end="")
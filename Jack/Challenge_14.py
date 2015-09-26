"""
Challenge 14

Write a program that:
asks the user to input a sentence
outputs the number of times the word 'the' occurs in it
"""
print ("Challenge 14: Counts how many times THE appears in a sentence")

string = input ("Enter your sentenece: ")
string = string.lower() # convert all to lower case as user may have entered The or THE or thE
count = string.count("the")

print ("THE appears %s times in your sentence" % count)
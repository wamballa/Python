"""
Challenge 13

Write a program that:
asks the user to input a sentence
asks the user to input:
    the word they want to replace
    the word they want to replace it with
    outputs the new sentence

"""

print ("Challenge 13: Replace a word in a sentence")

string = input ("Enter your sentence: ")
word = input ("What word do you want to replace?: ")

if word in string: # check that the word to be replaced is in string
    replace = input ("Replace %s with: " % word )
    string = string.replace ( word, replace )
    print ("Your new sentence is: %s" % string)
else:
    print ("     %s \nis not in your sentence\n     %s \nso I can't replace it!" % (word, string))
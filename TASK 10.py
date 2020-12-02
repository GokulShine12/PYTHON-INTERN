#Program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re
strg=input("String:")
a=re.compile("[A-Za-z0-9]+")
if a.fullmatch(strg):
    print("Valid String")
else:
    print("Invalid String")

#Python program that matches a word containing 'ab'
strg1=input("Word:")
if re.search('ab',strg1):
    print(" Matches ")
else:
    print("Invalid")

#Python program to check for a number at the end of a word/sentence
strg2=input("Sentence:")
if re.search(r'\d$',strg2):
    print("Valid word")
else:
    print("Invalid word")

#Python program to search the numbers (0-9) of length between 1 to 3 in a given string
strg3=input("String:")
if re.search('\d',strg3) and len(strg3)<=3:
    print("Found")
else:
    print("Not found")

#Python program to match a string that contains only uppercase letters
strg4=input("String:")
if re.match("^[A-Z]+$",strg4):
    print("Valid")
else:
    print("Invalid")

# 1. List down all the error types - using python program 

#Syntax error

  print "True"

#Division by zero error

try:
  print(10/0)
except ZeroDivisionError:
  print("Division by zero error")

#Key error

try:
  a={'cse-a':'65','cse-b':'60'}
  a['cse-c']
except KeyError:
  print("Key not found error")

#Module not found error
try:
  import mod
except ModuleNotFoundError:
  print("Module not found")


# 2. calculator
def calculator():
         try:
           a=int(input("Number 1 : "))
           b=int(input("Number 2 : "))
           c=input("Operation: +,-,*,/")
           if c=='+':
             print(" Addition of 2 nos is :",a+b)
           elif c=='-':
            print(" Subtraction of 2nos is :",a-b)
           elif c=='*':
            print(" Multiply of 2nos is :",a*b)
           elif c=='/':
             try:
              print(" Division of 2nos is :",a/b)
             except ZeroDivisionError:
               print("division by zero error")
         except ValueError:
           print("enter valid input")
calculator()


# 3. Print one message if the try block raises a NameError and another for other errors
try:
  print(name)
except NameError:
  print("Name is not defined")
except:
  print("Other error has occured")
  
  
# 4. When try-except scenario is not required ?

    " When our program has normal statements , there is no need for try-except "


# 5. Input inside the try catch block
try:
  sport=int(input("Your favorite sport is "))
  print(sport)
except:
  print("An exception occurs")

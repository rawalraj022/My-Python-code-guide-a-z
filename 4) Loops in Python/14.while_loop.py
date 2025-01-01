# Q) If we try to print our same name 10 times , What we will do inside the python ?

"""
⇒ We can print our same name 10 times in two ways :

i) 1st way is write print function 10 times but it’s a manual approach ,

ii) 2nd way is we can automate this particular task with the help of loops ,
"""

## i) 1st way is write print function 10 times but it’s a manual approach 

# Code :
"""
print("Rajkumar Rawal")
print("Rajkumar Rawal")
print("Rajkumar Rawal")
print("Rajkumar Rawal")
print("Rajkumar Rawal")
print("Rajkumar Rawal")
print("Rajkumar Rawal")
print("Rajkumar Rawal")
print("Rajkumar Rawal")
print("Rajkumar Rawal")
"""

## ii) 2nd way is we can automate this particular task with the help of loops

"""
There are two kinds of loops in python available they are :

i) While loop 

ii) For loop
"""

## i) While loop
    
    # While loop is used to execute a block of statements repeatedly until a given condition is satisfied.
    # And when the condition becomes false, the line immediately after the loop in program is executed.

# Syntax of while loop
"""
while condition:
    # Body of loop
    # Statements
"""

# Code :
"""
i = 0       # in programming we start counting from 0 so we have to start from 0 
            # if we start from 1 then it will print 11 times because 0 to 10 = 11 times
            # i = 0 is initialization of loop variable .

while i < 10:   # i < 10 is condition of loop , if condition is true then loop will execute otherwise loop will not execute 
    print("Rajkumar Rawal") # Body of loop , this statement will execute until the condition is true
    i += 1      # i += 1 is increment of loop variable , it will increment the value of i by 1
                # i += 1 is equivalent to i = i + 1
                # i += 1 is used to avoid infinite loop , if we don't use this then loop will execute infinite times
                # i += 1 is used to terminate the loop when the condition becomes false

"""


# Q) Program to print multiplication table  ? 

# Code :

"""
number = int(input("Enter the number :"))    # input function is used to take input from user

i = 1             # i = 1 is initialization of loop variable

while i<11:          # i < 11 is condition of loop , if condition is true then loop will execute otherwise loop will not execute
    #print(i*number)   # it will print only the multiplication of number
    print(number,"*",i,"=",i*number)   # it will print the multiplication table of number
    i += 1   # increment of loop variable

"""


# Q) While loop with else  ?

number = int(input("Enter the number :"))    # input function is used to take input from user

x = 1

while x < 4:
    print(x*number)
    x += 1

else:
    print("x is no longer less than 4")



# In next tutorial we will using this while loop with else 
    # in our guessing game project 


# - If we are creating any .py file make sure there won’t be any kinds of space between the words so, what we can do is we can replace that space with underscore’_’ symbol we can give because if we give the space whenever we will execute that particular file with our command prompt , so it may create some issue so that’s why **we don’t keep any kind of space whenever we create a .py file** .
#    - But if we are creating any jupyter notebook’ipynb’ file then, we can mention the space.
#    - These are some suggestion from python official side so we are talking about .
# - We use **jupyter notebook ‘ipynb’ file for **experiment** .
# - We use **‘.py’** file for **coding the project in python** .


"""
Exercise - 1 :  
Find the minimum number of 3 given numbers given by the user ? 
"""


"""
# Taking input from the user

num1 = int(input("Enter the first number: "))    
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Checking the minimum number among the three numbers using if-elif-else statement 

if num1 < num2 and num1 < num3:
    print("Minimum number is:", num1)

elif num2 < num1 and num2 < num3:
    print("Minimum number is:", num2)

else:
    print("Minimum number is:", num3)

"""




"""
    Exercise - 3 : 
    Create a calculator for every operation like addition, subtraction, multiplication, and division using if-elif-else statement. 
"""


# Taking input from the user

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation you want to perform: ")

# Creating a function for every operation 

if operation == '+':         # Addition operation 
    print("Addition of two numbers is:", num1 + num2)

elif operation == '-':       # Subtraction operation
    print("Subtraction of two numbers is:", num1 - num2)

elif operation == '*':           # Multiplication operation
    print("Multiplication of two numbers is:", num1 * num2)

elif operation == '/':        # Division operation
    print("Division of two numbers is:", num1 / num2)

else:               # Invalid operation
    print("Invalid operation")





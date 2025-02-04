import argparse          # argparse is a module in the Python standard library for creating command-line interfaces (CLIs) with ease and flexibility.
import sys               # sys is a module in the Python standard library that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.

def calculator(args):              # This function takes the arguments from the command line and performs the operation specified by the user on the two numbers.
    if args.o == "add":            # If the operation is addition, the function returns the sum of the two numbers.
        return args.a + args.b     
    elif args.o == "sub":          # If the operation is subtraction, the function returns the difference of the two numbers.
        return args.a - args.b 
    elif args.o == "mul":          # If the operation is multiplication, the function returns the product of the two numbers.
        return args.a * args.b 
    elif args.o == "div":          # If the operation is division, the function returns the quotient of the two numbers.
        if args.b != 0:             # If the second number is not zero, the division is performed and the result is returned.
            return args.a / args.b  
        else:                      # If the second number is zero, an error message is returned.
            return "Error: Division by zero"
        

# The following code reads the arguments from the command line, calls the calculator function with the arguments, and prints the result to the standard output.
parser = argparse.ArgumentParser()                        # Create an ArgumentParser object.
parser.add_argument("--a", type=float, default=1.0)      # Add a command-line argument for the first number with a default value of 1.0.
parser.add_argument("--b", type=float, default=2.0)     # Add a command-line argument for the second number with a default value of 2.0.
parser.add_argument("--o", type=str, default="add")    # Add a command-line argument for the operation with a default value of "add".

args = parser.parse_args()                            # Parse the command-line arguments.
sys.stdout.write(str(calculator(args)))             # Call the calculator function with the arguments and print the result to the standard output.


## Explanation of the above code:

# The code defines a function calculator that takes the arguments from the command line and performs the operation specified by the user on the two numbers. The function checks the operation specified by the user and performs the corresponding arithmetic operation on the two numbers. If the operation is division and the second number is zero, an error message is returned.

# The code then creates an ArgumentParser object using the argparse module to define the command-line arguments for the script. Three arguments are defined: --a for the first number, --b for the second number, and --o for the operation. The default values for the arguments are set to 1.0, 2.0, and "add" respectively.

# The code then parses the command-line arguments using parser.parse_args() and stores the arguments in the args variable. The calculator function is called with the arguments, and the result is printed to the standard output using sys.stdout.write(). The result is converted to a string using str() before printing it.

# To run the script, you can use the following command:
# python script.py --a 5 --b 2 --o add 
# This command will calculate the sum of 5 and 2 and print the result to the standard output.

# The script can perform addition, subtraction, multiplication, and division operations on two numbers specified by the user from the command line. The operation to be performed is specified using the --o argument, and the numbers are specified using the --a and --b arguments. The script provides a simple command-line calculator utility that can be used to perform basic arithmetic operations on numbers.

# argparse module is used to create a command-line interface with ease and flexibility. It allows you to define command-line arguments, parse them, and access the values of the arguments in a structured way. The argparse.ArgumentParser class is used to create an ArgumentParser object, which is used to define the command-line arguments for the script. The add_argument() method is used to add command-line arguments to the ArgumentParser object, specifying the argument name, type, default value, and other options.
# sys module is used to interact with the interpreter and access variables maintained by the interpreter. In this script, sys.stdout.write() is used to print the result of the calculator function to the standard output. The str() function is used to convert the result to a string before printing it.

""" 
f-string is a new way to format strings in Python 3.6 and above versions of Python. 
It is a more readable and concise way to format strings. 
It is also faster than the older formatting methods.  

**Syntax:**
f"string {variable}"

**Example:**
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")
Output:
My name is John and I am 25 years old.

"""

"""
# Example 1 [ Using format() method ]

s = "My name is {}, I am a {}"

name = "Rajkumar"
gender = "Male"

print(s.format(name, gender))

# To solve the same problem using format() method it takes more lines of code.
    # So, f-string is shorter and more readable than format() method.

"""

# To solve the same problem using format() method it takes more lines of code.
    # So, f-string is shorter and more readable than format() method.

# Using f-string method doing example 1 problem in a single line of code. 

name = "Rajkumar"
gender = "Male"

print(f"My name is {name}, I am a {gender}")


# We are going to use f-string in the future projects very often 
    # because it is more readable and concise than the older formatting

# f-string is also faster than the older formatting methods.

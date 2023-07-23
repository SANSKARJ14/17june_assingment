#18th June '23 Assignment.
"""
1. What is the role of try and exception block?

try and except blocks allows you to gracefully handle errors, log the error messages, recover from certain exceptional
situations, or take alternative actions to keep the program running smoothly even in the presence of errors.
It is considered a best practice for writing robust and fault-tolerant code.

"""
"""
2. What is the syntax for a basic try-except block?

try:
    # Code that might raise an exception
except SomeException:
    # Code to handle the exception

"""

"""
3. What happens if an exception occurs inside a try block and there is no matching
except block?

the program will terminate, and an error message (also known as a traceback) will be displayed.

The traceback will show the details of the unhandled exception, including the type of the exception is None:
    pass
"""

"""

4. What is the difference between using a bare except block and specifying a specific
exception type?

a.)Using a Specific Exception Type:
When you specify a specific exception type after the except keyword, like except SomeException,
it means that the corresponding except block will only catch exceptions of that particular type.
Any other exceptions that are not of that type will not be caught by this except block.

b.)Using a Bare except Block:
When you use a bare except block (i.e., except: without specifying any exception type),
it acts as a generic exception handler. It will catch any exception that occurs in the try block,
regardless of its type. This can be useful for catching unexpected or unknown exceptions and handling them in a
general way.

"""
"""
5.) Can you have nested try-except blocks in Python? If yes, then give an example.

Yes, Python allows you to have nested try-except blocks

def divide_numbers(a, b):
    try:
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    try:
        num1 = int(a)
        num2 = int(b)
        divide_numbers(a, b)
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")


"""
"""
6.) Can we use multiple exception blocks, if yes then give an example.

Yes, we can use multiple except blocks in Python to handle different types of exceptions separately

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid data types for division.")

"""
"""
7. Write the reason due to which following errors are raised:

a. EOFError: This error is raised when the built-in input() function tries to read input from the user,
but the user unexpectedly closes the input stream (for example, by pressing Ctrl+D on Unix/Linux or Ctrl+Z on Windows).
The abbreviation "EOF" stands for "End of File," indicating that the input stream has reached the end unexpectedly.

b. FloatingPointError: This error is raised when a floating-point arithmetic operation results in an exceptional
condition that cannot be represented, such as dividing by zero or producing an overflow or underflow. 
These errors typically occur when performing calculations involving floating-point numbers that exceed the limits
of their representation.

c. IndexError: This error is raised when trying to access an index of a sequence (like a list or tuple) that is
out of range. It occurs when attempting to access an element at an index that is negative or exceeds 
the size of the sequence.

d. MemoryError: This error is raised when an operation runs out of memory and cannot allocate additional memory to
complete the operation. It typically occurs when dealing with large data structures 
or when memory resources are exhausted.

e. OverflowError: This error is raised when an arithmetic operation exceeds the maximum representable value for a
numeric type. It occurs when trying to represent a result that is too large to be stored in the data type,
like an integer that overflows its limits.

f.)TabError: This error is raised when indentation-related issues occur in Python code.
It usually happens when mixing tabs and spaces for indentation in the same block of code, leading to inconsistencies

g.)ValueError: This error is raised when a function receives an argument of the correct type but with an inappropriate
value. It can occur, for example, when converting a string to an integer, but the string does not represent
a valid integer.

"""
"""
8. Write code for the following given scenario and add try-exception block to it.

a. Program to divide two numbers


def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid data types for division.")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
try:
    num1 = float(num1)
    num2 = float(num2)
    divide_numbers(num1, num2)
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
"""
"""

b. Program to convert a string to an integer:
def convert_into_string(s):
    try:
        num = int(s)
        print ("integer value :",num)
    except ValueError:
        print("invalid input")

input_string = input("enter a number as string")
convert_into_string(input_string)

"""
"""
c. Program to access an element in a list:



def access_list_elemnt(lst,index):
    try:
        element = lst[index]
        print ("element at index ",index , ':',element)
    except IndexError:
        print("error : index out of range ")

my_list = [50,60,70,80,90,100]
index = int (input("enter an index to access the list element:"))
access_list_elemnt(my_list,index)

"""
"""
d. Program to handle a specific exception:


def divide(data):
    try:
        ruselt = 100/data
        print ("the ruselt is ",ruselt)
    except ZeroDivisionError:
        print("you cannot divide by zero ")
    except Exception as e :
        print ("error:",str(e))

try:
    data = int(input("give me a number you want to divide "))
    actual_task = divide(data)
except ValueError:
    print ("error: give correct value")

"""
"""

def divide(a,b):
    try:
        ruselt = a/b
        print ("the ruselt is ",ruselt)
    except Exception as e:
        print ("error:",str(e) )

num1 = input("give value of frist number :")
num2 = input("give value of second number:")

try:
    num1 = float(num1)
    num2 = float(num2)
    divide(num1,num2)
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")

"""












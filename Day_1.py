#day1-Exception Handling

"""a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
try:
    c=a/b
    print("The result is: ",c)
except Exception as e:
    print("An error occurred: ",e)
"""
#Rethrowing an error in exception handling
"""def fun1():
    print("Inside fun1")
    try:
        fun2()
    except Exception as e:
        print("An error occurred in fun1: ",e)
    print("fun1 excuted successfully")
def fun2():
    print("Inside fun2")
    try:
        a=10/0
    except Exception as e:
        print("An error occurred in fun2: ",e)
        raise e
    finally:
        print("Leaving fun2")
fun1()
    """
#Exceptions

"""try:
    x=int(input("Enter a number: "))
    y=int(input("Enter another number: "))
    result=a/b
    print("The result is: ",result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception as e:
    print("An error occurred: ",e)"""

#single exception block for multiple exceptions
try:
    x=int(input("Enter a number: "))
    y=int(input("Enter another number: "))
    result=x/y
    print("The result is: ",result)
except (ZeroDivisionError, ValueError) as e:
    print("An error occurred: ",e)
else:
    print("The operation was successful")
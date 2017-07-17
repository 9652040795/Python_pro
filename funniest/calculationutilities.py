import time
import random

def simple_math(x,y):
    return x+y

def sum(a, b):
    return a + b

def multiply(a,b):
    time.sleep(10)
    return a*b

def add(self, x, y):
    """Takes two integers and adds them together to produce
    the result."""

    if type(x) == int and type(y) == int:
        return x + y
    else:
        raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))


def highestNumbebr(num):
    num = float(input("Enter a number: "))
    if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print("Negative number")


def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


def fact(n):
    """
    Factorial function

    :arg n: Number
    :returns: factorial of n

    """
    if n == 0:
        return 1
    return n * fact(n -1)


def div(n):
    """
    Just divide
    """
    res = 10 / n
    return res


def sum(self, a, b):
    return a + b


def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)

def teardown_module(module):
    print ("teardown_module   module:%s" % module.__name__)

def setup_function(function):
    print ("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    print ("teardown_function function:%s" % function.__name__)

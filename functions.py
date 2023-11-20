import math
from sympy import *
import numpy as np

# Function for the menu
def menu():
    print("Options:")
    print('1 - add')
    print('2 - subtract')
    print('3 - multiply')
    print('4 - divide')
    print('5 - square root')
    print('6 - special functions')
    print('7 - quit')

def specialFunctionsMenu():
    print("Options:")
    print('1 - pythagorean theorem')
    print('2 - derivatives')
    print('3 - factorization')
    print('4 - quadratic formula')
    print('5 - gcd')
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def sqrt_root():
    num = float(input("Enter number: "))
    return math.sqrt(num)

def pythagorean_theorem():
    print("What side are you missing? (1 - Hypotenuse, 2 - Leg)")
    action = input(": ")
    if action == "1":
        adjacent = float(input("Enter the Adjacent side: "))
        opposite = float(input("Enter the Opposite side: "))
        return math.sqrt((adjacent * adjacent) + (opposite * opposite))
    elif action == "2":
        hypotenuse = float(input("Enter the Hypotenuse: "))
        leg = float(input("Enter the Leg: "))
        return math.sqrt((hypotenuse*hypotenuse) - (leg*leg)) 
    else:
        print("Invalid input. Please try again.")

def quadratic_formula():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    c = float(input("Enter the third value: "))
    discriminant = b * b -4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("x is equal to", x1, "and", x2)
    elif discriminant == 0:
        x1 = -b / (2 * a)
        print("x is only equal to", x1)
    else:
        print("there is no real root")

def gcd():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return math.gcd(num1, num2)


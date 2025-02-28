#!/usr/bin/env python3


def summation(data):
    return sum(data)
import math

def square_root(x):
    if x < 0:
        raise ValueError("Don't enter a negative number")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Don't enter a negative number")
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Don't enter a non-positive numbers")
    return math.log(x)

def power(x, b):
    return x ** b

def main():
    while True:
        print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Log(base e)")
        print("4. Power ")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            x = float(input("Enter a number: "))
            print("Result:", square_root(x))
        elif choice == '2':
            x = int(input("Enter an integer: "))
            print("Result:", factorial(x))
        elif choice == '3':
            x = float(input("Enter a number: "))
            print("Result:", natural_log(x))
        elif choice == '4':
            x = float(input("Enter base number: "))
            b = float(input("Enter exponent: "))
            print("Result:", power(x, b))
        elif choice == '5':
            print("Leaving Calculator")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


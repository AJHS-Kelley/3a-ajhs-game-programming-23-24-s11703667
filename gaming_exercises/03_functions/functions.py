# Functions, 10-18-23, London Baldwin
import random
def functionName(): # Fuction Signature
    print("Whats your name?\n")
    name = input("Please type it and press enter.\n")
    print(f"Hello, {name}\n")

# Call the Function
functionName()

def happyBirthday(numTimes, age):
    count = 0
    while count < numTimes:
        print("Happy Birthday!\n")
        count += 1
    print(f"Wow, youre {age} years old!\n")




def functionWithReturn(num1, num2):
    sum = num1 + num2
    quotient = sum / 5
    return quotient # return immediately exits a function.
    
def functionWithoutReturn(num1, num2):
    sum = num1 + num2
    quotient = sum / 5
    print(quotient)

example = functionWithoutReturn(5, 10)
print(example)

def rollDice(numRoll, sizeRoll):
    count = 0
    sum = 0
# Data Types and Operators, London Baldwin, v0.0

myInt = 5
myFloat = 9.4

# Arithmetic Operators -- PEMDAS
print(myInt + 3) # Addition
print(myFloat - 7) # Subtraction
print(myFloat * 8) # Multiplication 
print(myInt / 7) # Division
print(myInt ** 2) # Exponents

# Modulus -- divides, then returns remainder.
print(10 % 5)
# COMMONLY USED TO DETERMINE EVEN/ODD NUMBERS

# Assignment Operator
myString = "lala k"
x = 0
# = means "Assign the variable on the left the value on the right."
# = throws out any previouly assigned value! 

# Addition Assignment Operator
myString += "I need a million bucks"
x += 2
# += means "Keep the current value and add the new value from the right."

# Comparison Operators -- Return True oe False
print(3 > 7) # Greater Than
print(45 >= 46) # Greater Than or Equal To
print(0 < -10) # Less Than
print(-78 <= 590) # Less Than Or Equal To
print(9 == 6) # Is Equal To
print(4 != 6) # Not Equal To

# Logical Operators 
# and requires ALL conditions to be true for overall time
print(7 > 2 and 4 < 10) # (True and True) == True
print(7 > 2 and 4 < 3) # (True and False) == False
print(7 > 2 and 4 > 3 and 1 != 2 and 5 == 5)

# or requires AT LEAST ONE condition to be True for overall True.
print(3 > 6 or 5 < 10) # (False or True) == True
print(-10 > -5 or 15 < 10) # (False or False) == False

# not -- 'opposite' value
favColor = "Pink"
print(favColor == not "Pink")

print( 4 > 3 and 1 != 2 and 5 < 3)
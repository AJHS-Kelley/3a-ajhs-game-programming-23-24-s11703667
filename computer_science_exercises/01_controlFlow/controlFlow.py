# Control Flow, london Baldwin, v0.0

# DECLARATIONS
favColor = "Pink"
luckyNumber = 13
myGPA = 3.0
myAge = 17
pineappleOnPizza = True

# if Statement
if luckyNumber > 30: # luckyNumber > 30 is a CONDITIONAL EXPRESSION
    print("Wow, what a great number!")

if myGPA < 3.6:
    print("Thats My Gpa")  

# if-else
if myGPA >= 3.0:
    print("Congratulations you made the honor roll!")  
else:
    print("You did not make the honor roll")

if myAge > 18:
    print("You are Legal age")
else:
    print("You are not legal age")

# if-elif-else Statement
if myAge > 65:
    print("Please enjoy retirement!")
elif myAge > 55:
    print("You have a $10,000 bonus!")
elif myAge > 40:
    print("you have earned a $5,000 bonus.")
else:
    print("You have earned $1,000 bonus.")
# 99% of the time check for the highest values first

# NESTED if / else / elif Statements
if pineappleOnPizza == True:
    print("You have strange taste. I bet you're old!")
    if myAge > 50:
        print("What was it like riding to school on a dinosaur?")
    else:
        print("Ok, you're still young enough to be cool.")
else:
    print("Ok good, you eat pizza like a normal human.")

if favColor == "Blue":
    print("We have the same fav color!")
    if myGPA >= 3.0:
        print("You get a pizza party!")
    else:
        print("Try harder next time!")
else:
    print("Ew why is it not blue?")

# while Loop -- Think MUSICAL CHAIRS -- Best used when you DO NOT know how many times the loop must run.
# loopCounter = 0
# while loopCounter < 100:
    print(f"The current loop count is {loopCounter}.")
    loopCounter += 1

# while loopCounter >= 0:
#    print(f"the current loop count is {loopCounter}.")
#    loopCounter -= 1
#    loopCounter = 0

# loopCounter = 0
# while loopCounter <= 100:
#     print(f"The current loop count is {loopCounter}")
#     if loopCounter % 2 == 0:
#         print(f"{loopCounter} is even!")
#     else:
#         print(f"{loopCounter} is odd!")
#     loopCounter += 1

# for Loop -- Think Go Fish! Used when you know the number of iterations needed.
for eachNumber in range(10):
    #eachNumber is known as the 'iterable variable'
    #range(x specifies the numbers from 0 to x
    print(eachNumber)


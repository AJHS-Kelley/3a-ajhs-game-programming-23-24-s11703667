# Pick the secret number from a range for the possible numbers (i.e 0-10, 0-100, etc.).
# Provide the player with x amount of guesses, based on the range of numbers.
# First player to get to 3 points will be declared a winner.
    # Player guesses the number.
    # Compare guess to secret number.
    # If the guess is correct what should happen?
        # Award the player a point.
        # Print a 'win' message on the screen.
# If they guess is incorrect, what should happen?
    # Indicate if guess is high/low compared to secret number.
# If the player does noy guess correctly beforre hitting the limit, what happens?
    # Award a point to the Cpu.
    # Print a loss message.


# Guess a Number, London Baldwin, v0.0
import random, tracemalloc, winsound
from PIL import Image
tracemalloc.start()

# DECLARATIONS
secretNumber = -1 # Range: 0 -- 20
playerName = "" # empty string
playerScore = 0
cpuScore = 0
numGuesses = 0
playerGuess = -1
diffLevel = None
numAttempts = -1
rangeMin = -1
rangeMax = -1

loserSound = ''
winnerSound = 'sfx/numberGuess/win.mp3'

imageWin = Image.open('img/numberGuess/img.win.jpg')
imageLoss = Image.open('img/numberGuess/loss.jpg')

print("""
        +=========================+
        |                         |
        |    Guess The Number     |
        |           by            |
        |     London Baldwin      |
        |          2023           |
        +=========================+
      
      
      """)

playerName = input("What should I call you?\nType your name and press enter.\n")
# VERIFY INPUT WHENEVER POSSIBLE
print(f"You want me to call you {playerName}.  Is that correct?")
isCorrect = input("Please type yes if correct, no if not correct.\n")
if isCorrect == "yes":
    print(f"Ok {playerName}, let's continue!")
else:
    playerName = input("What should I call you?\nTyper your name and press eneter.\n")

# The way this loop is written, if I do not type in Easy, Normal, or Hard, no difficulty is set by default and game loops until the CPU wins. 
while diffLevel == None:
    diffLevel =  input("Choose your difficulty Level! Easy, Normal, or Hard\n")
    # To fix your issue, change this to an if-elif-else block.  The else: block should be a default value if you cannot identify the difficulty. 
    if diffLevel == "Easy":
        print(f"You need to guess a number from 1-10")
        rangeMin = 1
        rangeMax = 10
        numAttempts = 5
    
    elif diffLevel == "Normal":
        print(f"You need to guess a number from 1-20")
        rangeMin = 1
        rangeMax = 20
        numAttempts = 5
    elif diffLevel == "Hard":
        print(f"You need to guess a number from 1-100")
        rangeMin = 1
        rangeMax = 100
        numAttempts = 3
    else:
        print(f"You need to guess a number from 1-10")
        rangeMin = 1
        rangeMax = 10
        numAttempts = 5

      

# GENERATE SECRET NUMBER
# We want the secret number generator to run when each match starts.  Look at the while loop and for loop and see if you can determine where to move this line.
# We also want the range for the random number generator to change based on difficulty. 
 # INCLUSIVE
# print(secretNumber)

# PLAYER GUESS
# print("You need to guess a number from 0 to 20.  You have 3 guesses!\n")

while playerScore != 3 and cpuScore != 3: # MATCH STARTS HERE 
    # pass # Tells Python to skip this block without giving an error.
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}\n")
    secretNumber = random.randint(rangeMin, rangeMax)
    print(secretNumber)
    numGuesses = 0
    for guesses in range(numAttempts): # ROUND STARTS HERE 
        print(f"You have {numAttempts - numGuesses} guesses left this round\n")
        playerGuess = int(input("Type your number in and press ENTER!\n"))
        # int coverts whatever is input into an INTERGER
        print(f"You have picked {playerGuess}. Let's see if it's a match!\n")
        if playerGuess == secretNumber:
            print("You must be psychic! It matched\n")
            playerScore += 1
            break # immediately exit a loop!
        
        else:
            if playerGuess < secretNumber:
                print("Your guess is too low!\n")
            else:
                print("Your guess is too high!\n")
            # playerGuess = int(input("Type your number in and press ENTER!\n"))
            # print(f"You have picked {playerGuess}. Let's see if it's a match!\n")
        numGuesses += 1
    if playerGuess != secretNumber: # put spaces between operators and values.
        print("You might not be smarter then the CPU, It won!\n")
        winsound.PlaySound(loserSound, winsound.SND_FILENAME)
        cpuScore += 1 # put spaces between operators and values.

if playerScore >= 3:
    print("You have won three rounds, YOU WON THE GAME!")
    imageWin.show()
    winsound.PlaySound(winnerSound, winsound.SND_win.mp3)
else:
    print("THE CPU REIGNS VICTORIOUS! YOU LOST :(")
    imageLoss.show()

print("Memory Usage: (Current, Peak)")
print(tracemalloc.get_traced_memory())
tracemalloc.stop()



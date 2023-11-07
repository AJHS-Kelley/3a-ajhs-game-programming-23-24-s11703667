wordList = ['cat hat bat map cap dog hog log ear tin high tear drill wait hate cake reup love']
















































def getRandomWord(wordlist):
    wordIndex = random.randint(0 , len(wordList) - 1)
    #len(listName) - 1 IS MOST COMMON WAY TO PREVENT INDEX OUT OF RANGE ERROS
    #print(wordIndex)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    # Display The Missed Letters
    print('Missed Letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            # The : character is used to SLICE strings into pieces.
            # [:i] means slicefrom the start until index i
            # [i+1:] means slice from i+1 until the END
            # [startingPoint:endingPoint]
            
    for letter in blanks:
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    # Only allow: single character, A-Z only, not guessed already.
    while True: # default 'infinite' loop
        print('Please guess a letter and press enter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please  enter a single letter.\n")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter an English Letter only.")
        elif guess in alreadyGuessed:
            print('Already guessed. Please guess a different letter!')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again? Yes or No, then press enter')
    return input().lower().startswith('y') # return True/False based on input

# START THE ACTUAL GAME
print("Let's Play Hangman!") # \ ESCAPES special characters.
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(wordList)
print("Testing Secret Word:" + secretWord)
gameIsDone = False

# GAME LOOP BEGINS HERE
while True: # 99% of the time the loop is done this way.
    # TWO WAYS TO EXIT while True: return OR break
    # DISPLAY THE BOARD
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord: # Is the guess in the secretWord?
        correctLetters = correctLetters + guess

        # CHECK FOR VICTORY
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters == True:
                print("Winner Winner Chicken Dinner!")
                gameIsDone = True

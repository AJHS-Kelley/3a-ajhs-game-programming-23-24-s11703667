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

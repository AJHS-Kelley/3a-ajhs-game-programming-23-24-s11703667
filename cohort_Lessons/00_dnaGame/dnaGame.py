# DNA Replication Game, London baldwin, v0.0a

# Import Entire Module
import time, datetime # BRING THE WHOLE TOOL BOX

# Import Specific Method from a Module
from random import choice # BRING JUST THE TOOL YOU NEED

dnaBases = ["A", "T", "G", "C"] # Adenine, Thymine, Guanine, Cytosine

def gameIntro() -> None:
    print("Hello Welcome to the DNA Replicator Game!\n")
    print("In This Game You Will have to Retype the Automated DNA Base as fast as you can!\n")

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a whole number for the number of bases to generate.\n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

def genRNA(dnaSequence: str) -> tuple: 
    print(f"The DNA Sequence is {dnaSequence}.\n ")
    print(" You need to enter the correct RNA sequence based on this DNA sequence.\n")
    print("Remember, the RNA base will have a U base to match with an A base from DNA.\n")
    # Start Timer
    rnaStart = time.time()
    rnaSequence = input("Please type the corrent RNA sequence with no spaces. Then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime) #Tuples are ORDERED (index), UNCHANGEABLE, Allows DUPLICATES

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence):
        if rnaBase == "U" and dnaBase != "T":   
            break
        elif rnaBase == "C" and dnaBase != "G":    
            break
        elif rnaBase == "T" and dnaBase != "A":
            break
        elif rnaBase == "G" and dnaBase != "C":
            break
        else:
            isMatch = True
    return isMatch

def calcScore(time: float, dnaSequence: str) -> int:
    score = 0
    if time < 1.0:
        score+= 10000
    elif time < 5.0:
        score+= 1000
    elif time < 10.0:
        score+= 100
    else:
        score+= 10


# DNA Sequence Length Multiplier
# If you want to give a bonus, make the multiplier > 1.0
# If you want to penalize, make the multiplier < 1.0



dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)
print(checkSequence(dna, rna[0]))
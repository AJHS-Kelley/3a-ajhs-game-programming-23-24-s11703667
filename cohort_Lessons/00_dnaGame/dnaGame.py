# DNA Replication Game, London baldwin, v0.0a

# Import Entire Module
import time, datetime # BRING THE WHOLE TOOL BOX

# Import Specific Method from a Module
from random import choice # BRING JUST THE TOOL YOU NEED

dnaBases = ["A", "T", "G", "C"] # Adenine, Thymine, Guanine, Cytosine

def gameIntro() -> None:
    pass

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
    print("Remember, the RNA base will have a base to match with an base from DNA.\n")
    # Start Timer
    rnaStart = time.time()
    rnaSequence = input("Please type the corrent RNA sequence with no spaces. Then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime) #Tuples are ORDERED (index), UNCHANGEABLE, Allows DUPLICATES

dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)
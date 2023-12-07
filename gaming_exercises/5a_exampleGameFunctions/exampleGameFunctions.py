# London Baldwin, Fuctions Example, v0.0
import random
playerName = "Mario Luigi Toad Peach Yoshi Bowser Wario Daisy".split()
playerWorld = ""
playerLives = ""

def getPlayer(playerName):
    while True: 
        print(playerName)
        print("Choose you Player!l")
        name = input()
        if name not in(playerName):
            print("Please Choose Name From The List!")
        else:
            return name
        

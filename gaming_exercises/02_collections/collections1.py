# Adding Items
playerInventory = []
while len(playerInventory) < 10:
    item = input("What do you want to add?\n")
    playerInventory.append(item) # .append() adds to the end of the list.
playerInventory.sort()
# .whatever() is known as a METHOD. IT MEANS "DO THIS TO THAT".
print(playerInventory)
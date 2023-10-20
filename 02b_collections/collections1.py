# Adding Items
# playerInventory = []
# while len(playerInventory) < 10:
#     item = input("What do you want to add?\n")
#     playerInventory.append(item) # .append() adds to the end of the list.
# playerInventory.sort()
# # .whatever() is known as a METHOD. IT MEANS "DO THIS TO THAT".
# print(playerInventory)

# # REMOVE ITEMS
# while len(playerInventory) > 5:
#     item = input("What do you want to remove?\n")
#     playerInventory.remove(item)
# playerInventory.sort()
# print(playerInventory)

# Lists For Fixed Inventory System
# weaponList = [
#     False, # Flame thrower
#     False, # Pistol
#     True, # Swiss blade
#     False, # Bazooka
#     True # Banana
# ]
# # each item/value in a list is an ELEMENT
# # the location of each element in the list is the INDEX
# # first element is index[0]
# # shortcut to last element is index[-1]
# weaponNum = 0
# while weaponNum < len(weaponList):
#     if weaponNum == 0 and weaponList[0] == True:
#         print("Your Character is equipped with a Flame thrower.\n")
#     if weaponNum == 0 and weaponList[1] == True:
#         print("Your Character is equipped with a Pistol.\n")
#     if  weaponNum == 0 and weaponList[2] == True:
#         print("Your Character is equipped with a Swiss Blade.\n")
#     if weaponNum == 0 and weaponList[3] == True:
#         print("Your Character is equipped with a Bazooka.\n")
#     if weaponNum == 0 and weaponList[4] == True:
#         print("Your Character is equipped with a Banana.\n")
#     weaponNum += 1

# ITEM EXISTS IN INENTORY
doorKeys = [
    "red",
    "blue",
    "green",
    "yellow"
]
item = input("Which key do you require?").lower()
if item in doorKeys:
    print(f"You have the {item} key!\n")
else:
    print(f"You do not have the {item} key.")
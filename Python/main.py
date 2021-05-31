import csv


from player import Player
from . import board
from . import items
from . import party
from . import beast



def main():
    beast_list = readFile()

    P1 = Player()
    P1.setName(enterName("Player 1"))
    P2 = Player()
    P2.setName(enterName("Player 2"))



#Standard enter name prompt, requires noun requiring a name (e.g. Beast or player)
def enterName(noun):
    name = input("Please enter a " + noun + " name:")
    answer = input("Is \"" + name + "\" correct? (y/n)")

    while answer != "y" or answer != "Y" or answer != "n" or answer != "N":
        print("Invalid. Please type \"y\" or \"n\"")
        answer = input("Is \"" + name + "\" correct? (y/n)")

    if answer != "n" or answer != "N":
        name = enterName(noun)

    return name



def readFile():
    with open('beastData.csv') as f:
        reader = csv.reader(f, delimiter="\t")

        existingBeastList = []

        for line in reader:
            attribute_list = []

            for item in line:
                attribute_list.append(item)
            newBeast = Beast(attribute_list[0], attribute_list[1], attribute_list[2], attribute_list[3], attribute_list[4],
                                 attribute_list[5], attribute_list[6], attribute_list[7])
            existingBeastList.append(newBeast)
    return existingBeastList


#Prints data put in
def printData(Data):
    print(Data)



def movementOnBoard():
    #rollDie()
    #applyMovementEffect()
    #movePlayer()
    #checkBoardSpace for event or effect
    #check if another player is occupying that space

    return

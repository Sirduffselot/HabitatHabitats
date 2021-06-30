import random
import csv
from player import Player
from party import Party
from guards import Guards



#Standard battle between two players
class Battle:
    # def __init__(self, Group1, Group2):
    #     Group1 = Group1
    #     Group2 = Group2

    #Battles
    def standardBattle(self, Party1, Party2):
        #Determines which party leader is faster
        partyPrimary, partySecondary = differentiatingSpeed(Party1, Party2)
        #Initiates battle menu for faster beast
        battleMenu(partyPrimary, partySecondary)
        isDead(partyPrimary)

        #Determines which party leader is faster
        beastPrimary, beastSecondary = differentiatingSpeed(Party1.get_leader(), Party2.get_leader())
        #Initiates battle menu for slower beast
        battleMenu(beastPrimary, beastSecondary)

        #If either party is out of Beasts
        if (not Party1) or (not Party2):


        return

    def strongholdBattle(self, Party, Guards):
        return

    def bossBattle(self, Party, Boss):
        return


# The battle menu
def battleMenu(partyActing, partyOpponent):
    beastActing = partyActing.get_leader
    beastOpponent = partyOpponent.get_leader

    print("What will you do?\n")
    print("Menu:")
    print("1 - Attack")
    print("2 - Stats")
    print("3 - Run")

    userValue = input()

    if (userValue == 1):
        attack(beastActing, beastOpponent)
    elif (userValue == 2):
        checkStats(beastActing, beastOpponent)
    elif (userValue == 3):
        runFromBattle(beastActing, beastOpponent)
    else:
        print("Not a correct option, please try again...")
        battleMenu(partyActing, partyOpponent)



# Individual round between specifically two beasts
def attack(beast1, beast2):




def checkStats(beastActing, beastOpponent):
    return

#Determines if running from a battle was a success
def runFromBattle():
    return

# Factor in die throw, difference in beast speed, and diceRoll()
def damageCalculator(beastPrimary, beastSecondary):
    # Assumes beast1 is faster than beast2
    luckyValueTemp = luckyValue(beastPrimary)
    total_attack = beastPrimary.attack + rollDie() + luckyValueTemp
    total_defense = beastSecondary.defense
    # netResult is the net attack on the opponent's hp
    netResult = total_attack - total_defense

    if (luckyValueTemp is 1):
        print(beastPrimary.name + " got lucky (+1 Atk)...")

    if netResult > 0:
        # If net effect is positive, remove the opponent's hp by that amount
        new_hp = beastSecondary.hp - netResult
        beastSecondary.set_currentHp(new_hp)

        print(beastPrimary.name + " did " + netResult + " dmg...")
    else:
        print("It had no effect...")

def rollDie():
    randomNum = random.randint(1, 7)
    return randomNum



#Returns the faster Beast
def differentiatingSpeed(party1, party2):
    #Returns fasterParty. slowerParty

    beast1 = party1.members[0]
    beast2 = party2.members[0]

    if beast2.speed > beast1.speed:
        return party2, party1
    else:
        #If tied or Beast1 is faster
        return party1, party2



def generateRandomNumber():
    randomNum = random.randint(1, 11)
    return randomNum

def luckyValue(beast):
    if beast.luck >= generateRandomNumber():
        return 1
    else:
        return 0



#Swapping Beasts when leader dies
def swapBeast():
    return


def isDead(party):
    #Announces party member deaths
    for x in party:
        if party.members[x].get_currentHp() is 0:
            print(party.members[x].get_nickname() + " has died...")

    #Removes dead party members
    for x in range(2, -1, -1):
        if party.members[x].get_currentHp() is 0:
            party.removeDeadFromParty(x)
import random
import csv
from player import Player
from party import Party
from guards import Guards



# Standard battle between two players
class Battle:
    # def __init__(self, Group1, Group2):
    #     Group1 = Group1
    #     Group2 = Group2

    #Battles
    def standardBattle(self, Party1, Party2):
        # Determines whether the battle will continue
        anyFightersLeft = False

        #Determines which party leader is faster, and thus begins the fight
        partyPrimary, partySecondary = differentiatingSpeed(Party1, Party2)

        # Initiates battle menu for faster beast
        battleMenu(partyPrimary, partySecondary)

        # Checks if primary party lost
        if checkForAnyLivingPartyMembers(partyPrimary) == False:

            return

        # Initiates battle menu for the other player's beast
        battleMenu(partySecondary, partyPrimary)

        # Checks if secondary party lost
        checkForAnyLivingPartyMembers(partySecondary)

        return

    def strongholdBattle(self, Party, Guards):
        return

    def bossBattle(self, Party, Boss):
        return


# The battle menu
def battleMenu(partyActing, partyOpponent):
    beastActing = partyActing.getLeader
    beastOpponent = partyOpponent.getLeader

    print("What will you do?\n")
    print("Menu:")
    print("1 - Attack")
    print("2 - Spell")
    print("3 - Stats")
    print("4 - Run")

    userValue = input()

    if (userValue == 1):
        attack(beastActing, beastOpponent)
    elif (userValue == 4):
        if (isSpellAvailable(partyActing.getLeader()) == True):
            spell()
    elif (userValue == 3):
        checkStats(beastActing, beastOpponent)
        battleMenu(partyActing, partyOpponent)
    elif (userValue == 4):
        runFromBattle(beastActing, beastOpponent)
    else:
        print("Not a correct option, please try again...")
        battleMenu(partyActing, partyOpponent)

#Checks if the leader of a party has died
def isBeastDead(party):
    if party.getLeader().currentHP <= 0:
        print(party.members[0].getNickname() + " has died...")
        party.members[0].setCurrentStatus("Dead")

    return

#Swapping Beasts when leader dies
def swapBeast():
    #Set new leader
    #Swap positions of beast in party, dead leader [0] for another living beast
    return

#Checks a party to see if there are any remaining fighters alive
def checkForAnyLivingPartyMembers(Party, livingCheck):
    for x in Party.members:
        if Party.members[x].currentStatus != "Dead":
            livingCheck = True

    return livingCheck

#Individual round between specifically two beasts
def attack(beast1, beast2):

    return

def isSpellAvailable(beast1):

    return

def spell(beast1, beast2):
    return

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



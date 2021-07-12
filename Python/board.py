import csv
import random

from battle import Battle


class Space:
    def __init__(self):
        self.event = None
        self.effect = None
        self.nextSpace = None
        self.alternativeSpace = None

    def setEvent(self, event):
        self.event = event

    def setEffect(self, effect):
        self.effect = effect

    def setNextSpace(self, nextSpace):
        self.nextSpace = nextSpace

    def setAlternativeSpace(self, alternativeSpace):
        self.alternativeSpace = alternativeSpace



#Class for creating the board to roam around on
class Board:
    def __init__(self):
        S0 = Space()
        S0.setEvent("Start")
        S1 = Space()

    #Initiates battle mode between two parties
    def battleMode(self):
        battle = Battle;
        battle.standardBattle(self, Party1, Party2)
        return

    def updatePlayerSpace(self):
        return

    def decipherEventSpace(self, player):
        currentEvent = player.currentSpace.get_event()

        if currentEvent is "Start":
            return
        #take care of event
        #
        #
        return






def effectSpaceDecipher(player):
    currentEffect = player.currentSpace.get_effect()
    # take care of effect
    #
    #
    return

def separateBeastListByTiers(existingBeastList):
    commonBeastList = []
    rareBeastList = []
    legendaryBeastList = []

    for x in existingBeastList:
        if existingBeastList[x].tier is "C":
            commonBeastList.append(existingBeastList[x])
        elif existingBeastList[x].tier is "R":
            rareBeastList.append(existingBeastList[x])
        elif existingBeastList[x].tier is "L":
            legendaryBeastList.append(existingBeastList[x])
        else:
            print("separateBeastListByTiers() error! Error! Error!")

    return commonBeastList, rareBeastList, legendaryBeastList



# Beast generator used for market spaces and "Free Beast" spaces
def standardRandomBeastGenerator(commonBeastList, rareBeastList, legendaryBeastList):
    randomNum = random.randint(1, 101)
    # 60% Chance to get common beast
    if randomNum > 0 and randomNum < 61:
        return random.choice(commonBeastList)
    # 30% Chance to get rare beast
    elif randomNum > 60 and randomNum < 91:
        return random.choice(rareBeastList)
    # 10% Chance to get legendary beast
    elif randomNum > 90 and randomNum < 101:
        return random.choice(legendaryBeastList)
    else:
        print("standardRandomBeastGenerator() error! Error! Error!")



# Beast generator used for wheel spins
def wheelRandomBeastGenerator(commonBeastList, rareBeastList, legendaryBeastList):
    randomNum = random.randint(1, 101)
    # 50% Chance to get common beast
    if randomNum > 0 and randomNum < 51:
        return random.choice(commonBeastList)
    # 35% Chance to get rare beast
    elif randomNum > 50 and randomNum < 86:
        return random.choice(rareBeastList)
    # 15% Chance to get legendary beast
    elif randomNum > 85 and randomNum < 101:
        return random.choice(legendaryBeastList)
    else:
        print("wheelRandomBeastGenerator() error! Error! Error!")

def market():
    return
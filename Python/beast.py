import csv
import random



class Beast:
    def __init__(self, beastName, baseHp, attack, defense, speed, luck, activeTrait, passiveTrait, className, tier):
        self.nickname = beastName
        self.beastName = beastName
        self.currentHp = baseHp
        self.currentStatus = None;
        self.baseHp = baseHp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.activeTrait = activeTrait
        self.passiveTrait = passiveTrait
        self.className = className
        self.tier = tier

    def getName(self):
        print(self.nickname)

    def getBeastName(self):
        print(self.beastName)

    def getCurrentHp(self):
        print(self.currentHp)

    def getCurrentStatus(self):
        print(self.currentStatus)

    def getBaseHp(self):
        print(self.baseHp)

    def getAttack(self):
        print(self.attack)

    def getDefense(self):
        print(self.defense)

    def getSpeed(self):
        print(self.speed)

    def getLuck(self):
        print(self.luck)

    def getTrait(self):
        print(self.trait)

    def getClassName(self):
        print(self.className)

    def getTier(self):
        print(self.tier)

    def setNickname(self, nickname):
        self.nickname = nickname

    def setCurrentHp(self, currentHp):
        self.currentHp = currentHp

    def setCurrentStatus(self, currentStatus):
        self.currentStatus = currentStatus



#Boss Beasts, found through random encounters
class Boss:
    def __init__(self, beastName, currentHp, baseHp, attack, defense, speed, luck, trait):
        self.beastName = beastName
        self.currentHp = baseHp
        self.baseHp = baseHp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.trait = trait
import csv
import random



class Beast:
    def __init__(self, beastName, baseHp, attack, defense, speed, luck, trait, className, tier):
        self.nickname = beastName
        self.beastName = beastName
        self.currentHp = baseHp
        self.baseHp = baseHp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.trait = trait
        self.className = className
        self.tier = tier

    def get_name(self):
        print(self.nickname)

    def get_beastName(self):
        print(self.beastName)

    def get_currentHp(self):
        print(self.currentHp)

    def get_baseHp(self):
        print(self.baseHp)

    def get_attack(self):
        print(self.attack)

    def get_defense(self):
        print(self.defense)

    def get_speed(self):
        print(self.speed)

    def get_luck(self):
        print(self.luck)

    def get_trait(self):
        print(self.trait)

    def get_className(self):
        print(self.className)

    def get_tier(self):
        print(self.tier)

    def set_nickname(self, nickname):
        self.nickname = nickname

    def set_currentHp(self, currentHp):
        self.currentHp = currentHp



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
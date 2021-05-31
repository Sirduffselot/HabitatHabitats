import csv
import random
from items import ItemPouch



#Class for each player
class Player:
    def __init__(self):
        #Name of the player
        self.name = ""
        #Amount of gold the player has
        self.gold = 0
        #Party of 3 or less Beasts
        self.party = []
        #Item Pouch of items
        self.itemPouch = ItemPouch()
        #List of Active Effects availabe from Beasts in party
        self.activeEffects = []
        #List of Passive Effects availabe from Beasts in party
        self.passiveEffects = []
        #Effect on the player that affects movement on board
        self.boardEffect = "None"
        #Current space that the player is occupying
        self.currentSpace = "None"
        #Total laps the player has completed
        self.totalLaps = 0

    def get_name(self):
        return self.name

    def get_gold(self):
        return self.gold

    def get_party(self):
        return self.party

    def get_BoardEffect(self):
        return self.BoardEffect

    def get_CurrentSpace(self):
        return self.currentSpace

    def get_TotalLaps(self):
        return self.totalLaps

    def set_Name(self, name):
        self.name = name

    def set_Party(self, party):
        self.party = party

    def set_BoardEffect(self, boardEffect):
        self.boardEffect = boardEffect

    def set_CurrentSpace(self, currentSpace):
        self.currentSpace = currentSpace

    def set_TotalLaps(self, totalLaps):
        self.totalLaps = totalLaps

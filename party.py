import csv
import random
from beast import Beast


class Party:
    def __init__(self):
        #List of Beasts in a party
        self.members = []
        #Effects that affect gameplay during battle
        self.partyEffects = []

    def get_leader(self):
        return self.members[0]

    def set_leader(self):
        #Only during menu from board
        #Use swap
        return

    #Lists names of each Beast in party
    def listPartyNames(self):
        for x in self.members:
            print((x + 1) + ". " + self.members[x].nickname)

    #Lists stats for each Beast in party
    def listPartyStats(self):
        #If party is empty
        if not self.members:
            print("You have no Beasts in your party.")
            print()
        else:
            print("--------------------")
            for x in self.members:
                print(self.members[x].name)
                print(self.members[x].className)
                print(self.members[x].tier + "\n")
                print(self.members[x].hp)
                print(self.members[x].attack)
                print(self.members[x].defense)
                print(self.members[x].speed)
                print(self.members[x].luck)
                print("--------------------")

    def addToParty(self, beast):
        #If party is full
        if len(self.members) == 3:
            print("Party is full")
            answer = input("Would you like to remove a party member? (y/n)")
            while answer != "y" or answer != "Y" or answer != "n" or answer != "N":
                print("Invalid. Please try again.")
                answer = input("Would you like to remove a party member? (y/n)")

            if answer is "y" or answer is "Y":
                self.members.removeFromParty
            return

        #If there is room in party
        answer = input("Would you like to give it a nickname? (y/n)")
        while answer != "y" or answer != "Y" or answer != "n" or answer != "N":
            print("Invalid. Please try again.")
            answer = input("Would you like to give it a nickname? (y/n)")

        if answer is "y" or answer is "Y":
            nickname = enterName("Beast")
            beast.set_nickname(nickname)

        #Adds Beast to party
        self.members.append(beast)
        print(beast.nickname + " joined the party.")

    #Select party members to remove
    def removeFromParty(self):
        partySize = len(self.members)

        print("Select a Beast to remove:")
        self.members.listPartyNames
        answer = input()
        while answer > partySize or answer < 1:
            print("Invalid. Please try again.")
            print("Select a Beast to remove:")
            self.members.listPartyNames
            answer = input()

        print(self.members[(answer - 1)].name + " has left the party.")
        del(self.members[(answer - 1)])

    #Removes dead party members
    def removeDeadFromParty(self, x):
        del (self.members[x])

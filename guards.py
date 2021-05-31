import csv



#Guards of the castle
class Guards():
    def __init__(self):
        # List of Beasts as guards of castle
        self.guards = []
        # Party leader, or the first Beast to appear in a battle
        self.leader = ""
        # Effects that affect gameplay during battle
        self.partyEffects = []
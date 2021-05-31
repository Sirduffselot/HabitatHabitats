

#Random encounters of CPUS
class Encounter:
    def __init__(self):
        # List of Beasts in a party
        self.party = []
        # Party leader, or the first Beast to appear in a battle
        self.leader = ""
        # Effects that affect gameplay during battle
        self.partyEffects = []

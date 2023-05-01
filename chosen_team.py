import parameter as prm

class Chosen_Team:
    def __init__(self, cap_id, vice_id, id = None):
        self.chosenPlayerList = id
        self.captain = cap_id
        self.vice_captain = vice_id
    
    def printPlayerList(self):
        for player in self.chosenPlayerList:
            print(prm.playerList[player - 1])
    def __str__(self):
        return f"Players chosen:\n{self.printPlayerList()}"

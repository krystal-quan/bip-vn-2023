import parameter as prm

class Chosen_Team:
    totalPoint = 0
    def __init__(self, cap_id = None, vice_id = None, id = None, main_id = None, tf_left = None, point = 0, out_id = None, in_id = None):
        self.chosenPlayerList = id
        self.mainTeam = main_id
        self.captain = cap_id
        self.vice_captain = vice_id
        self.point = point
        self.out_id = out_id
        self.in_id = in_id
        self.tf_left = tf_left
        
    
    def printPlayerList(self):
        for player in self.chosenPlayerList:
            print(prm.playerList[player - 1])
    def __str__(self):
        return f"Players chosen:\n{self.printPlayerList()}"

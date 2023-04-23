import csv
import random
import player as Player
class ChosenPlayer:
    def __init__(self, id = [], *args):
        self.chosenPlayerList = id
    
    def printPlayerList(self):
        for player in self.chosenPlayerList:
            print(playerList[player - 1])
    def __str__(self):
        return f"Players chosen:\n{printPlayerList()}"
    
# Variables
NUM_OF_PLAYERS = 15        
playerList = []
chosenPlayerList = []
currentPlayer = []
gameWeekCount = 0


def getDataFromCSV():
    with open('cleaned_player.csv','r', encoding="Latin1") as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            playerList.append(Player(lines[0], lines[1], lines[17]))
            
def printPlayerList():
    for player in playerList:
        print(player)

def choosePlayerEachWeek():
    global gameWeekCount
    while (gameWeekCount < 38):
        if (gameWeekCount == 0):
            while (True):
                for _ in range(NUM_OF_PLAYERS):
                    while (True):
                        tempId = random.randint(1, Player.num_of_players)
                        if (tempId not in currentPlayer):
                            currentPlayer.append(tempId)
                            break
                if (True):
                    #TODO: Check if total value of 15 player is less than 100
                    chosenPlayerList.append(ChosenPlayer(currentPlayer))
                    break
        else:
            eliminatedPlayer = random.randint(0, NUM_OF_PLAYERS - 1)
            currentPlayer.pop(eliminatedPlayer)
            while (True):
                tempId = random.randint(1, Player.num_of_players)
                if (tempId not in currentPlayer):
                    currentPlayer.append(tempId)
                    break
        chosenPlayerList.append(ChosenPlayer(currentPlayer))
        gameWeekCount += 1

getDataFromCSV()
choosePlayerEachWeek()
for i in range(len(chosenPlayerList)):
    print(f"GameWeek {str(i)}:")
    chosenPlayerList[i].printPlayerList()

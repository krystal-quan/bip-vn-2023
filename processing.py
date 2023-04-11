import csv
import random

class Player:
    num_of_players = 0
    def __init__(self, first_name, second_name, value):
        self.first_name = first_name
        self.second_name = second_name
        self.value = value
        Player.num_of_players += 1
        self.id = Player.num_of_players
    
    def __str__(self):
        return f"Player {self.id}: {self.first_name} {self.second_name} - Value: {self.value}"
    
    def getValue(self):
        return self.value
    
    def getName(self):
        return f"{self.first_name} {self.second_name}"
    
class ChosenPlayer:
    def __init__(self, id = [], *args):
        self.chosenPlayerList = id
    
    def printPlayerList(self):
        for player in self.chosenPlayerList:
            print(playerList[player - 1])
    def __str__(self):
        return f"Players chosen:\n{printPlayerList()}"
    
class Point:
    totalPoints = 0
    pointList = []
    
    def __init__(self, points):
        self.points = points
        Point.totalPoints += points
        Point.pointList.append(points)
        
    def __str__(self):
        return f"Total points: {Point.totalPoints}\nPoints per game: {Point.getPointsPerGame()}"
        
    def getPoints(self, gameWeek):
        return f"GameWeek {gameWeek}: {Point.pointList[gameWeek - 1]}"
    
    def getTotalPoints(self):
        return Point.totalPoints
    
    def getPointsPerGame(self):
        for i in range(len(Point.pointList)):
            return f"{Point.getPoints(i + 1)}"
    
    

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

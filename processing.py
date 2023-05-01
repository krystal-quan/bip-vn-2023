import csv
import random
import player as plr
import parameter as prm
import chosen_team as cht

            
def printPlayerList():
    for player in prm.playerList:
        print(player)

def choosePlayerEachWeek():
    while (prm.gameWeek < 38):
        if (prm.gameWeek == 0):
            while (True):
                for _ in range(prm.NUM_OF_PLAYERS):
                    while (True):
                        tempId = random.randint(1, prm.TOTAL_PLAYERS)
                        if (tempId not in prm.gameWeekRoster):
                            prm.gameWeekRoster.append(tempId)
                            break
                # if (True):
                #     #TODO: Check if total value of 15 player is less than 100
                #     prm.gameWeekRoster.append(cht.Chosen_Team(prm.gameWeekRoster))
                break
        else:
            eliminatedPlayer = random.randint(0, prm.NUM_OF_PLAYERS - 1)
            prm.gameWeekRoster.pop(eliminatedPlayer)
            while (True):
                tempId = random.randint(1, prm.TOTAL_PLAYERS)
                if (tempId not in prm.gameWeekRoster):
                    prm.gameWeekRoster.append(tempId)
                    break
        temp = random.randint(1, prm.NUM_OF_PLAYERS)
        prm.chosenPlayerList.append(cht.Chosen_Team(temp, (temp + 7) % prm.NUM_OF_PLAYERS + 1, prm.gameWeekRoster))
        prm.gameWeek += 1

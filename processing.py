import csv
import random
import player as plr
import parameter as prm
import chosen_team as cht
import stored_old_data as sod

            
def printPlayerList():
    for player in prm.playerList:
        print(player)

def completeWeek(gameWeek):
    #print(f"gameweek in prc : {gameWeek}")
    tempPoint = 0
    cap_available = True
    cap_id = prm.chosenPlayerList[gameWeek - prm.startWeek].captain
    #if (cap_id == None) :
    #    cap_id = prm.chosenPlayerList[gameWeek-1].mainTeam[0]
    #print(f"cap_id in processing: {cap_id}")
    #print(f"cap_id + {cap_id}")
    if prm.playerList[cap_id]._total_points != -1:
        cap_available = True
    for i in prm.chosenPlayerList[gameWeek - prm.startWeek].mainTeam:
        if prm.playerList[i]._total_points != -1:
            if (i == prm.chosenPlayerList[gameWeek - prm.startWeek].captain and cap_available):
                tempPoint += prm.playerList[i]._total_points * 2
            elif (
                i == prm.chosenPlayerList[gameWeek - prm.startWeek].vice_captain
                and not cap_available
            ):
                tempPoint += prm.playerList[i]._total_points * 2
            else:
                tempPoint += prm.playerList[i]._total_points
    prm.point += tempPoint
    prm.transferLeft = min(prm.transferLeft + prm.FREE_TOKEN, prm.MAX_TOKEN)
    
            

            

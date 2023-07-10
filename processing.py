import csv
import random
import player as plr
import parameter as prm
import chosen_team as cht
import stored_old_data as sod

"""
Print all player ids in playerList
"""            
def printPlayerList():
    for player in prm.playerList:
        print(player)

"""
Input: the order of the gameWeek
To do: + Calculate point achieved in the gameWeek
       + Update transfer left after the gameWeek 
Ouput: None
"""
def completeWeek(gameWeek):
    tempPoint = 0
    cap_available = True
    if gameWeek >= 1 :
        gg.set_game_week(f"gws\gw{prm.gameWeek}.csv", prm.playerList, prm.gameWeek)
    cap_id = prm.chosenPlayerList[gameWeek - prm.startWeek].captain
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
    
            

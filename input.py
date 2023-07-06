"""
import json
import compare
import parameter as prm
import update_player_data as upd
import chosen_team as cht
prm.playerList = upd.set_player_list()

# transfer: number transfer left in file input
global transfer
"""
"""
Input: .json file contain data of main roster and transfer, file must be correct format.
Output: player_list is a list of dictionary, each dictionary has name and position of 15 players.
TO DO: change data in .json file to a list in Python
"""
def extractJsonFileToPython(filename):
    global transfer
    with open(filename) as f:
        data = json.load(f)
    
    main_roster = data['Main Roster']
    transfer = data['transfer']
    prm.gameWeek = data['Week']
    main_players = data['Players chosen']

    # Store main_roster
    player_list = []
    player_id_list = []

    # Store main_player
    main_player_list = []
    main_player_id_list = []

    captain_id = 0
    vice_id = 0

    # Append in the main_roster list
    for player_data in main_roster:
        player_name = player_data['player']
        player_position = player_data['position']
        captain_value = player_data['Captain']
        vice_value = player_data['Vice captain']
        player_list.append({'name' : player_name, 'position' : player_position})
        id = compare.continuous_search(prm.playerList,player_name, 0, len(prm.playerList)) + 1
        player_id_list.append(id)
        captain_value = player_data['Captain']
        vice_value = player_data['Vice captain']
        if captain_value == 1 :
            captain_id = id
        if vice_value == 1 :
            vice_id = id
    
    # Append in the main_player list
    for main_player in main_players :
        player_name = main_player['player']
        player_position = main_player['position']
        main_player_list.append({'name' : player_name, 'position' : player_position})
        id = compare.continuous_search(prm.playerList,player_name, 0, len(prm.playerList)) + 1
        main_player_id_list.append(id)



    return captain_id, vice_id, player_id_list, main_player_id_list, transfer

def getInput():
    filename = 'input_full.json'
    captain_id, vice_id, player_id, mainPlayer_id, transferLeft = extractJsonFileToPython(filename)
    print(player_id)
    print(mainPlayer_id)
    print(transferLeft)
    """
    for player in players:
        print(f"Player: {player['name']}, Position: {player['position']}")
        print(compare.continuous_search(prm.playerList,player['name'], 0, len(prm.playerList)) + 1)
    """
   # prm.transferLeft = transferLeft
    #print(prm.transferLeft)
   # prm.chosenPlayerList.append(cht.Chosen_Team(captain_id, vice_id, player_id, mainPlayer_id, prm.transferLeft, prm.point, 0, 0))
    #print(prm.chosenPlayerList[0].printPlayerList())
getInput()
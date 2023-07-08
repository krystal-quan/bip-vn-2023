
import json
import compare
import parameter as prm
import update_player_data as upd
import chosen_team as cht
prm.playerList = upd.set_player_list()

# transfer: number transfer left in file input


"""
Input: .json file contain data of main roster and transfer, file must be correct format.
Output: player_list is a list of dictionary, each dictionary has name and position of 15 players.
TO DO: change data in .json file to a list in Python
"""
def extractJsonFileToPython(filename):
   
    with open(filename) as f:
        data = json.load(f)
    
    main_roster = data['Main Roster']
    prm.transferLeft = data['transfer']
    prm.gameWeek = data['Week']
    prm.startWeek = data['Week']
    #main_players = data['Players chosen']

    # Store main_roster
    player_list = []
    player_id_list = []

    # Store main_player
    # Append in the main_roster list
    for player_data in main_roster:
        player_name = player_data['player']
        player_position = player_data['position']
        player_list.append({'name' : player_name, 'position' : player_position})
        id = compare.continuous_search(prm.playerList,player_name, 0, len(prm.playerList)) + 1
        player_id_list.append(id)
        
    
    return player_id_list

# Get input from requirement and update the player IDs chosen. 
def getInput():
    filename = 'input_full.json'
    player_id = extractJsonFileToPython(filename)
    prm.chosenPlayerList.append(cht.Chosen_Team(player_id[0], player_id[1], player_id, player_id[0:12], prm.transferLeft, prm.point, [40], [player_id[0]]))
    prm.playerInput = player_id
    

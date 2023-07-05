import json

# transfer: number transfer left in file input
global transfer

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
    player_list = []

    for player_data in main_roster:
        player_name = player_data['player']
        player_position = player_data['position']
        player_list.append({'name' : player_name, 'position' : player_position})

    return player_list

if __name__ == '__main__':
    filename = 'input.json'
    players = extractJsonFileToPython(filename)

    for player in players:
        print(f"Player: {player['name']}, Position: {player['position']}")
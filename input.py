import json
import parameter
import compare

"""
Input: .json file contain data of main roster and transfer, file must be correct format.
        player_list: list of players in whole game week.
Output: None
TO DO: change data in .json file to a list in Python
"""
def extractJsonFileToPython(filename, player_list):
    with open(filename) as f:
        data = json.load(f)
    
    main_roster = data['Main Roster']
    parameter.transferLeftInput = data['transfer']
    parameter.gameWeekInput = data['week']
    player_list_input = []

    for player_data in main_roster:
        player_name = player_data['player']
        player_position = player_data['position']
        player_list_input.append({'name' : player_name, 'position' : player_position})

    setPlayerData(player_list_input, player_list)

    return 0

"""
Input:  player_input: 15 players input.
        player_list: list of players in whole game week.
Output: None
TO DO:  update data to file parameters
"""
def setPlayerData(player_input, player_list):
    for player in player_input:
        pos = compare.continuous_search(player_list, player['name'], 0, len(player_list))
        if pos != -1:
            parameter.gameWeekRosterInput.append(player_list[pos])

if __name__ == '__main__':
    filename = 'input.json'
    players = extractJsonFileToPython(filename)

    for player in players:
        print(f"Player: {player['name']}, Position: {player['position']}")
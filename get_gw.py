import compare
import pandas as pd
import stored_old_data as st

'''
Input:
    file_name is name of file gameweek
    player_list is a list to manage data of player
    week is order of gameweek
Output:
    counter is variable to check the number of player play in this week
To do: Update new data of player in new week.
'''
def set_game_week(file_name, player_list, week):
    game_week = pd.read_csv(file_name, encoding='ISO-8859-1')
    diff = len(player_list) - game_week.shape[0]
    counter = 0
    stored_player(player_list, week)
    for index, row in game_week.iterrows():
        pos = compare.continuous_search(player_list, row['name'], index, index + diff)
        if (pos != -1):
            player_list[pos].set_goals_scored(row['goals_scored'])
            player_list[pos].set_assists(row['assists'])
            player_list[pos].set_total_points(row['total_points'])
            player_list[pos].set_minutes(row['minutes'])
            player_list[pos].set_goals_conceded(row['goals_conceded'])
            player_list[pos].set_creativity(row['creativity'])
            player_list[pos].set_influence(row['influence'])
            player_list[pos].set_threat(row['threat'])
            player_list[pos].set_bonus(row['bonus'])
            player_list[pos].set_bps(row['bps'])
            player_list[pos].set_ict_index(row['ict_index'])
            player_list[pos].set_clean_sheets(row['clean_sheets'])
            player_list[pos].set_red_cards(row['red_cards'])
            player_list[pos].set_yellow_cards(row['yellow_cards'])
            player_list[pos].set_selected_by_percent(row['selected'])
            counter += 1
        else:
            pos = compare.continuous_search(player_list, row['name'], 0, len(player_list))
            if (pos != -1):
                player_list[pos].set_goals_scored(row['goals_scored'])
                player_list[pos].set_assists(row['assists'])
                player_list[pos].set_total_points(row['total_points'])
                player_list[pos].set_minutes(row['minutes'])
                player_list[pos].set_goals_conceded(row['goals_conceded'])
                player_list[pos].set_creativity(row['creativity'])
                player_list[pos].set_influence(row['influence'])
                player_list[pos].set_threat(row['threat'])
                player_list[pos].set_bonus(row['bonus'])
                player_list[pos].set_bps(row['bps'])
                player_list[pos].set_ict_index(row['ict_index'])
                player_list[pos].set_clean_sheets(row['clean_sheets'])
                player_list[pos].set_red_cards(row['red_cards'])
                player_list[pos].set_yellow_cards(row['yellow_cards'])
                player_list[pos].set_selected_by_percent(row['selected'])
                counter += 1
            else:
                print ('Failed to find')
    return counter

'''
Input:
    player_list is a list to manage data of player
    week is order of gameweek
Output: None
To do: Store old data of player to reuse.
'''
def stored_player(player_list, week):
    for i in range(len(player_list)):
        st.set_player_data(player_list[i], i, week - 1)
        player_list[i].reset()

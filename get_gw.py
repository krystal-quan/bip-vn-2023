import compare
import update_player_data
import pandas as pd
import stored_old_data as st

# Hàm này sẽ cập nhật giá trị mới nhất của gameweek vào trong player_list, đồng thời tạo 1 bản copy vào trong
# mảng 2 chiều players trong stored_old_data.py, 1 chiều là số cầu thủ = 683, 1 chiều là số tuần = 38 (fix cứng)
# các cầu thủ không đá sẽ bị reset các chỉ số chính về 0 (trừ giá tiền và vị trí)
# phải nhập đúng số week (tuần n thì nhập là n) để ghi file được chính xác
# file_name là tên của file gameweek có thể là 'gw1.csv' hay 'gws\gw1.csv' tùy vào vị trí của file gameweek
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
            # player_list[pos].set_value(row['value'])
            # Vì đang xét giá trị không đổi nên không đổi value, muốn đổi thì tùy
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
            else:
                print ('Failed to find')
    return counter

def stored_player(player_list, week):
    for i in range(len(player_list)):
        st.set_players(player_list[i], i, week - 1)
        player_list[i].reset()

if __name__ == '__main__':
    player_list = update_player_data.set_player_list()
    print(set_game_week("gw1.csv", player_list))
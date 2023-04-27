import player as pl
import get_gw as gw
import update_player_data as upd
import FPL_CPLEX as cpl

if __name__ == "__main__":
    player_list = upd.set_player_list()
    gw.set_game_week('gws\\gw1.csv', player_list, 1)
    player_list[0].print_all()
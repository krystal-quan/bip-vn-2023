<<<<<<< HEAD
import processing as prc
import parameter as prm
import player as plr
import update_player_data as upd


prm.gameWeek = 0
while (prm.gameWeek <=38):
    if (prm.gameWeek == 0):
        prm.playerList = upd.set_player_list()
    prm.gameWeek += 1
    
print(prm.TOTAL_PLAYER)
=======
import player as pl
import get_gw as gw
import update_player_data as upd
import FPL_CPLEX as cpl

if __name__ == "__main__":
    player_list = upd.set_player_list()
    gw.set_game_week('gws\\gw1.csv', player_list, 1)
    player_list[0].print_all()
>>>>>>> 382ee2677e8c28bf925a7314913b0ec69bb780fd

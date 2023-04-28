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
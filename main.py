import processing as prc
import parameter as prm
import player as plr
import update_player_data as upd
import print_output_file as pof
import chosen_team as cht

if __name__ == "__main__":
    prm.playerList = upd.set_player_list()
    prc.choosePlayerEachWeek()
    pof.create_output_file()
    pof.updateFile(0)
    pof.close_file()
        
        

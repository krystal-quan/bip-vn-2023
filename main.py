
import parameter as prm
import player as plr
import update_player_data as upd
import print_output_file as pof
import chosen_team as cht

if __name__ == "__main__":
    # Get players data from csv file and store them in player_list
    prm.playerList = upd.set_player_list()
    
    import get_gw as gg
    
    
    import CPLEX_Solution as CS
    import processing as prc
    import stored_old_data as sod
    
    # pof.create_output_file()
    pof.create_json_output_file()
    while(prm.gameWeek < 39):
        print(f"Game Week {prm.gameWeek}")
        if (prm.gameWeek >= 1):
            gg.set_game_week(f"gws\gw{prm.gameWeek}.csv", prm.playerList, prm.gameWeek)
            prc.completeWeek(prm.gameWeek)
        if (prm.gameWeek < 38):
            CS.updateValue(prm.gameWeek)
            CS.chooseTeam(prm.gameWeek)
        # pof.updateFile(prm.gameWeek)
        pof.executeFile(prm.gameWeek)
        prm.gameWeek += 1
    # pof.close_file()
    pof.close_json_file()
        

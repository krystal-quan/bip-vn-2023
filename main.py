
import parameter as prm
import player as plr
import update_player_data as upd
import print_output_file as pof
import chosen_team as cht
import input

if __name__ == "__main__":
    
    import get_gw as gg
    input.getInput(prm.startWeek)
    

    import CPLEX_Solution as CS
    import processing as prc
   
    pof.create_json_output_file()
    while(prm.gameWeek < 39):
        print(f"Game Week {prm.gameWeek}")
        if prm.startWeek != 0 and prm.gameWeek >= prm.startWeek + 1:
            gg.set_game_week(f"gws\gw{prm.gameWeek-1}.csv", prm.playerList, prm.gameWeek)
            CS.updateValue(prm.gameWeek) 
            CS.chooseTeam(prm.gameWeek)  
            prc.completeWeek(prm.gameWeek)
            
        elif prm.startWeek == 0 and prm.gameWeek >= prm.startWeek + 1:
            gg.set_game_week(f"gws\gw{prm.gameWeek}.csv", prm.playerList, prm.gameWeek)
            CS.updateValue(prm.gameWeek) 
            CS.chooseTeam(prm.gameWeek)  
            prc.completeWeek(prm.gameWeek)
        if (prm.gameWeek == 0) :
            print("main: prm.gameweek == 0")
            CS.updateValue(prm.gameWeek)  
            CS.chooseTeam(prm.gameWeek)
            prc.completeWeek(prm.gameWeek)
            
        pof.executeFile(prm.gameWeek)
        prm.gameWeek += 1
    # pof.close_file()
    pof.close_json_file()
        

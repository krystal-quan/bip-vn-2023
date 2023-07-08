
import parameter as prm
import player as plr
import update_player_data as upd
import print_output_file as pof
import chosen_team as cht
import input

if __name__ == "__main__":
    # Get players data from csv file and store them in player_list
   # prm.playerList = upd.set_player_list()
    #print(f"Main: {prm.gameWeek}")
  #  print(f"Main: {prm.transferLeft}")
   # print(f"Main: {prm.chosenPlayerList}")
    
    import get_gw as gg
    input.getInput()
    

    import CPLEX_Solution as CS
    import processing as prc
    #import stored_old_data as sod
    # Week 0: Update (Expected points) => chooseTeam (Choosen from history data) => rotate 
    # Week 1 : Set expected points indexes for W1 => Calculate points gotten for w1 => Optimizie w2 => ChooseTeam for w2
    
    #pof.create_output_file()
    pof.create_json_output_file()
    while(prm.gameWeek < 39):
        print(f"Game Week {prm.gameWeek}")
        if (prm.gameWeek >= prm.startWeek + 1):
            gg.set_game_week(f"gws\gw{prm.gameWeek-1}.csv", prm.playerList, prm.gameWeek)
            #print(prm.gameWeek)
        #if (prm.gameWeek >= 6 and prm.gameWeek < 38):
            CS.updateValue(prm.gameWeek-1) # Update expected point for optimization
            #print(f"main.py 33: {prm.transferLeft}")
            CS.chooseTeam(prm.gameWeek-1)  
            prc.completeWeek(prm.gameWeek-1)
        # pof.updateFile(prm.gameWeek)
        if (prm.gameWeek >= prm.startWeek + 1):
            pof.executeFile(prm.gameWeek)
        prm.gameWeek += 1
    # pof.close_file()
    pof.close_json_file()

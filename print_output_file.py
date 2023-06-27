import parameter as prm
import json

def get_total_output():
    with open("config.txt", "r") as f:
        prm.OUTPUT_FILES = f.read()
        print("Number of output files:", prm.OUTPUT_FILES)
        f.close()
    # Rewrite config.txt
    with open("config.txt", "w") as f:
        f.write(str(int(prm.OUTPUT_FILES) + 1))
        f.close()

f = None

def create_output_file():
    get_total_output()
    newFile = f"output\output{prm.OUTPUT_FILES}.txt"
    global f
    f = open(newFile, "w")
    
def updateFile(gameWeek):
    global f
    if (gameWeek == 38):
        f.write("Final result:\n")
        f.write(f"Total point: {prm.point}\n")
        f.write("------------------------------------------\n")
        return
        
    f.write(f"Game Week: {gameWeek}" + "\nPlayers chosen:\n")
    for id in prm.chosenPlayerList[gameWeek].chosenPlayerList:
        temp = prm.playerList[id].getPlayerInfo()
        f.write("\t" + temp + "\n")
    f.write("\n")
    f.write("\nMain Roster:\n")
    for id in prm.chosenPlayerList[gameWeek].mainTeam:
        temp = prm.playerList[id].getPlayerInfo()
        f.write("\t" + temp)
        if (id == prm.chosenPlayerList[gameWeek].captain):
            f.write(" (CAPTAIN)")
        elif (id == prm.chosenPlayerList[gameWeek].vice_captain):
            f.write(" (VICE_CAPTAIN)")
        f.write("\n")
    f.write("\n")
        
    if (gameWeek >= 1):
        f.write("Players out: \n")
        for id in prm.chosenPlayerList[gameWeek].out_id:
            temp = prm.playerList[id].getPlayerInfo()
            f.write("\t" + temp + "\n")
        f.write("Players in:\n")
        for id in prm.chosenPlayerList[gameWeek].in_id:
            temp = prm.playerList[id].getPlayerInfo()
            f.write("\t" + temp + "\n")
        f.write("\n")
        temp  = "Transfer left: " + (str)(prm.chosenPlayerList[gameWeek].tf_left) + "\n"
        f.write(temp)
        temp = "Total point: " + (str)(prm.chosenPlayerList[gameWeek].point) + "\n"
        f.write(temp)
    f.write("------------------------------------------\n")
          
def close_file():
    global f
    f.close()

def create_json_output_file():
    newFile = f"output\\result.json"
    global js 
    js = open(newFile, "w")
    global ls 
    ls = []

def executeFile(gameWeek):
    global js
    global ls

    if (gameWeek == 38):
        dic1 = {"Total points" : f"{prm.point}"}
        dic2 = {f"Week {gameWeek}": dic1}
        ls.append(dic2)
        dic3 = {"All week" : ls}
        json_object = json.dumps(dic3, indent=1)
        js.write(json_object)
        return 0
    
    lWeek = []
    lRoster = []
    for id in prm.chosenPlayerList[gameWeek].chosenPlayerList:
        temp = prm.playerList[id]
        dic1 = {"id" : f"{temp.get_id()}", 
                "player" : f"{temp.get_full_name()}", 
                "position" : f"{temp.get_position()}",
                "Captain" : f"{1 if (id == prm.chosenPlayerList[gameWeek].captain) else 0}",
                "Vice captain" : f"{1 if (id == prm.chosenPlayerList[gameWeek].vice_captain) else 0}"}
        lRoster.append(dic1)
    dRoster = {'Main Roster' : lRoster}
    lWeek.append(dRoster)

    lChosen = []
    for id in prm.chosenPlayerList[gameWeek].mainTeam:
        temp = prm.playerList[id]
        dic2 = {"id" : f"{temp.get_id()}", 
                "player" : f"{temp.get_full_name()}", 
                "position" : f"{temp.get_position()}"}
        lChosen.append(dic2)
    dChosen = {'Players chosen': lChosen}
    lWeek.append(dChosen)

    if (gameWeek >= 1):
        lTrans = []
        dic3 = {}
        for id in prm.chosenPlayerList[gameWeek].in_id:
            temp = prm.playerList[id].getPlayerInfo()
            dic3['in'] = temp
        for id in prm.chosenPlayerList[gameWeek].out_id:
            temp = prm.playerList[id].getPlayerInfo()
            dic3['out'] = temp
        lTrans.append(dic3)
        dTrans = {'Transfers' : lTrans}
        lWeek.append(dTrans)
    
    dWeek = {f"Week {gameWeek}" : lWeek}
    ls.append(dWeek)

def close_json_file():
    global js
    js.close()
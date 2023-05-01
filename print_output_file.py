import parameter as prm

def get_total_output():
    with open("config.txt", "r") as f:
        prm.OUTPUT_FILES = f.read()
        print("Number of output files:", prm.OUTPUT_FILES)

f = None

def create_output_file():
    get_total_output()
    newFile = f"output\output{prm.OUTPUT_FILES}.txt"
    global f
    f = open(newFile, "w")
    
def updateFile(gameWeek):
    if (gameWeek == 0):
        global f
        f.write("Game Week 0\nPlayers chosen:\n")
        for id in prm.chosenPlayerList[gameWeek].chosenPlayerList:
            temp = prm.playerList[id-1].getPlayerInfo()
            f.write(temp + "\n")
            
def close_file():
    global f
    f.close()
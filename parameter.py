import update_player_data as upd

#Constraints, which are unchanged throughout the optimization process.
OUTPUT_FILES = 0
E_CONSTANT = 1e-5
K_CONSTANT = [] #Constants such that l << ✏ for all l 2 L, and 1 > 2 >...> L.
TOTAL_PLAYERS = 0 #Total number of players in the dataset.
NUM_OF_PLAYERS = 15 #Number of players in the squad.
GOALKEEPER_SELECTED = 2 #Number of goalkeepers required in the selected squad.
DEFENDER_SELECTED = 5 #Number of defenders required in the selected squad.
MIDFIELDER_SELECTED = 5 #Number of midfielders required in the selected squad.
FORWARD_SELECTED = 3 #Number of forwards required in the selected squad.
# Temporary not used, may use later.
# maxSameTeamSelected = 3 #Maximum number of players allowed in the selected squad from the same team.
PLAYER_REQUIRED = 11 #Number of players required in the starting line-up.
GOALKEEPER_REQUIRED = 1 #Number of goalkeepers required in the starting line-up.
DEFENDER_REQUIRED = 3 #Minimum number of defenders required in the starting line-up.
MIDFIELDER_REQUIRED = 3 #Minimum number of midfielders required in the starting line-up.
FORWARD_REQUIRED = 1 #Minimum number of forwards required in the starting line-up.
START_BUDGET = 100 #Starting budget.
BETA = 1e5 #Sufficiently high constant.
ALPHA = 1e5 #Sufficiently high constant.
SUB_PLAYER = 4 #Number of players which are substitutes.
SUB_GOALKEEPER = 1 #Number of goalkeepers which are substitutes.
FREE_TOKEN = 1 #Number of free transfers given every gameweek.
MAX_TOKEN = 2 #Maximum number of free transfers possible to accumulate over gameweeks.

#Variables, which are changed throughout the optimization process.
point = []
# May delete this variable.
# sellPrice = [] #Sell price of player p in a gameweek t.
# playerValue = [] #Value of player p in a gameweek t.
deductedPoint = [] #Number of points deducted for each penalized transfer.
playerList = None #List of players in the dataset.
chosenPlayerList = [] #List of players chosen in the selected squad.
gameWeekRoster = [] #List of players chosen in the starting line-up.
gameWeek = 0 #Current gameWeek.





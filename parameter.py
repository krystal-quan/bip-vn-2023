#Parameters:

point = []
eConstant = 1e-5
kconstant = [] #Constants such that l << ✏ for all l 2 L, and 1 > 2 >...> L.
sellPrice = [] #Sell price of player p in a gameweek t.
playerValue = [] #Value of player p in a gameweek t.
deductedPoint = 0 #Number of points deducted for each penalized transfer.
goalkeeperSelected = 2 #Number of goalkeepers required in the selected squad.
defenderSelected = 5 #Number of defenders required in the selected squad.
midfielderSelected = 5 #Number of midfielders required in the selected squad.
forwardSelected = 3 #Number of forwards required in the selected squad.
maxSameTeamSelected = 3 #Maximum number of players allowed in the selected squad from the same team.
playerRequired = 11 #Number of players required in the starting line-up.
goalkeeperRequired = 1 #Number of goalkeepers required in the starting line-up.
defenderRequired = 3 #Minimum number of defenders required in the starting line-up.
midfielderRequired = 3 #Minimum number of midfielders required in the starting line-up.
forwardRequired = 1 #Minimum number of forwards required in the starting line-up.
startBudget = 100000000 #Starting budget.
beta = 1e5 #Sufficiently high constant.
alpha = 1e5 #Sufficiently high constant.
subPlayer = 4 #Number of players which are substitutes.
subGoal = 1 #Number of goalkeepers which are substitutes.
_q = 1 #Number of free transfers given every gameweek.
q_ = 2 #Maximum number of free transfers possible to accumulate over gameweeks.
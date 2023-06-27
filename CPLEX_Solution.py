from docplex.mp.model import Model
import parameter as prm
import chosen_team as cht
import stored_old_data as sod


"""
Lists to encode whether the player plays in the position or not.
"""
PD = [1 if prm.playerList[i]._position == 'DEF' else 0 for i in range(prm.TOTAL_PLAYERS)]
PM = [1 if prm.playerList[i]._position == 'MID' else 0 for i in range(prm.TOTAL_PLAYERS)]
PF = [1 if prm.playerList[i]._position == 'FWD' else 0 for i in range(prm.TOTAL_PLAYERS)]
PK = [1 if prm.playerList[i]._position == 'GK' else 0 for i in range(prm.TOTAL_PLAYERS)]

"""
# Add-in variables
OT: list to encode whether the player was chosen in the previous Gameweek 
CS: list costs of players (fixed)
EP: list Expected Points for each player, updated every GW
IFL: list of Influence index for each player, updated every GW
"""
OT = [0 for _ in range(prm.TOTAL_PLAYERS)]
CS = [0 for _ in range(prm.TOTAL_PLAYERS)]
EP = [0 for _ in range(prm.TOTAL_PLAYERS)]
IFL = [0 for _ in range(prm.TOTAL_PLAYERS)]


# Constants
R = 4  #points deducted for each penalized transfer
MK = 2 #No of goalkeepers in the selected squad
MD = 5 #No of defenders
MM = 5 #No of Midfielders
MF = 3 #No of forwards

E = 11  #No of players in the starting line-up
EK = 1  #No of goalkeepers in the line-up
ED = 3  #No of defenders 
EM = 3  #No of midfielders
EF = 1  #No of forwards
BS = 100  #starting budget


"""
Input: order number of gameweek
Ouput: None
To do: Update the expected points and influence indexes for each player in GW
"""
def updateValue(gameWeek):
    for i in range(prm.TOTAL_PLAYERS):
        if (gameWeek == 0):
            CS[i] = prm.playerList[i]._value * 0.1
            if prm.playerList[i]._position in ['GK', 'DEF']:
                EP[i] = 4  * prm.playerList[i]._clean_sheets + prm.playerList[i]._goals_scored * 6 + prm.playerList[i]._assists * 3 - prm.playerList[i]._yellow_cards - prm.playerList[i]._red_cards * 3 - prm.playerList[i]._goals_conceded * 0.5
                IFL[i] = prm.playerList[i]._influence * 0.4 + prm.playerList[i]._creativity * 0.4 + prm.playerList[i]._threat * 0.2
            elif (prm.playerList[i]._position == 'MID'):
                EP[i] = prm.playerList[i]._clean_sheets + prm.playerList[i]._goals_scored * 5 + prm.playerList[i]._assists * 3 - prm.playerList[i]._yellow_cards - prm.playerList[i]._red_cards * 3
                IFL[i] = prm.playerList[i]._influence * 0.3 + prm.playerList[i]._creativity * 0.4 + prm.playerList[i]._threat * 0.3
            elif (prm.playerList[i]._position == 'FWD'):
                EP[i] = prm.playerList[i]._goals_scored * 4 + prm.playerList[i]._assists * 3 - prm.playerList[i]._yellow_cards - prm.playerList[i]._red_cards * 3
                IFL[i] = prm.playerList[i]._influence * 0.2 + prm.playerList[i]._creativity * 0.3 + prm.playerList[i]._threat * 0.5
        elif (gameWeek >= 1):
            if (prm.playerList[i]._total_points == -1 or prm.playerList[i]._red_cards == 1 ):
                EP[i] = 0
                IFL[i] = 0
            if prm.playerList[i]._position in ['GK', 'DEF']:
                EP[i] = 4  * prm.playerList[i]._clean_sheets + prm.playerList[i]._goals_scored * 6 + prm.playerList[i]._assists * 3 - prm.playerList[i]._yellow_cards - prm.playerList[i]._red_cards * 3 - prm.playerList[i]._goals_conceded * 0.5
                IFL[i] = prm.playerList[i]._influence * 0.4 + prm.playerList[i]._creativity * 0.4 + prm.playerList[i]._threat * 0.2
            elif (prm.playerList[i]._position == 'MID'):
                EP[i] = prm.playerList[i]._clean_sheets + prm.playerList[i]._goals_scored * 5 + prm.playerList[i]._assists * 3 - prm.playerList[i]._yellow_cards - prm.playerList[i]._red_cards * 3
                IFL[i] = prm.playerList[i]._influence * 0.3 + prm.playerList[i]._creativity * 0.4 + prm.playerList[i]._threat * 0.3
            elif (prm.playerList[i]._position == 'FWD'):
                EP[i] = prm.playerList[i]._goals_scored * 4 + prm.playerList[i]._assists * 3 - prm.playerList[i]._yellow_cards - prm.playerList[i]._red_cards * 3
                IFL[i] = prm.playerList[i]._influence * 0.2 + prm.playerList[i]._creativity * 0.3 + prm.playerList[i]._threat * 0.5
           
        

"""
Input: order number of gameweek
Output: None
Todo: 2 main tasks in this function :
+ Task 1: writing linear programming and solve it
+ Task 2: Get the solution from CPLEX for outputting 
"""

def chooseTeam(gameWeek):
    m = Model(name='FPL')
    # Player is in the team (15 players)
    x_p = m.binary_var_list(prm.TOTAL_PLAYERS, name="x")
    # Player is in main roster (11 players)
    y_p = m.binary_var_list(prm.TOTAL_PLAYERS, name="y")
    cap_p = m.binary_var_list(prm.TOTAL_PLAYERS, name="cap")
    vice_p = m.binary_var_list(prm.TOTAL_PLAYERS, name="vice")

    # Selected Squad Constraints
    m.add_constraint(m.sum(x_p[i] for i in range(prm.TOTAL_PLAYERS)) == prm.NUM_OF_PLAYERS)
    m.add_constraint(m.sum(y_p[i] for i in range(prm.TOTAL_PLAYERS)) == prm.PLAYER_REQUIRED)
    for i in range(prm.TOTAL_PLAYERS):
        m.add_constraint(y_p[i] <= x_p[i])
    m.add_constraint(m.sum(x_p[i] * CS[i] for i in range(prm.TOTAL_PLAYERS)) <= prm.START_BUDGET) # Budget Constraint
    
    # Selected Squad Constraints
    m.add_constraint(m.sum(x_p[i] * PK[i] for i in range(prm.TOTAL_PLAYERS)) == MK)
    m.add_constraint(m.sum(x_p[i] * PD[i] for i in range(prm.TOTAL_PLAYERS)) == MD)
    m.add_constraint(m.sum(x_p[i] * PM[i] for i in range(prm.TOTAL_PLAYERS)) == MM)
    m.add_constraint(m.sum(x_p[i] * PF[i] for i in range(prm.TOTAL_PLAYERS)) == MF)
    
    # Starting Line-up Constraints
    m.add_constraint(m.sum(y_p[i] * PK[i] for i in range(prm.TOTAL_PLAYERS)) == EK)
    m.add_constraint(m.sum(y_p[i] * PD[i] for i in range(prm.TOTAL_PLAYERS)) >= ED)
    m.add_constraint(m.sum(y_p[i] * PM[i] for i in range(prm.TOTAL_PLAYERS)) >= EM)
    m.add_constraint(m.sum(y_p[i] * PF[i] for i in range(prm.TOTAL_PLAYERS)) >= EF)
    
    # Captain and Vice-captain Constraints
    m.add_constraint(m.sum(cap_p[i] for i in range(prm.TOTAL_PLAYERS)) == 1)
    m.add_constraint(m.sum(vice_p[i] for i in range(prm.TOTAL_PLAYERS)) == 1)
    for i in range(prm.TOTAL_PLAYERS):
        # This is to ensure captain and vice captain are in the main roster
        m.add_constraint(cap_p[i] <= y_p[i])
        m.add_constraint(vice_p[i] <= y_p[i])
        # This is to ensure captain and vice captain are different players
        m.add_constraint(cap_p[i] + vice_p[i] <= 1)
 
    if (gameWeek == 0):
       # z = m.sum(x_p[i] * (EP[i] * (1 + cap_p[i] + vice_p[i])) for i in range(prm.TOTAL_PLAYERS))  => Error :)
        z = m.sum(x_p[i] * (EP[i] * (1 + cap_p[i] + vice_p[i]) + IFL[i] * 0.04) for i in range(prm.TOTAL_PLAYERS))
        m.maximize(z)
        m.solve()
       
    elif (gameWeek >= 1):
        #Substitution Constraints
        m.add_constraint(m.sum(m.abs(x_p[i] - OT[i]) for i in range(prm.TOTAL_PLAYERS)) <= prm.transferLeft)
        z = m.sum(x_p[i] * (EP[i] * (1 + cap_p[i] + vice_p[i]) + IFL[i] * 0.04) for i in range(prm.TOTAL_PLAYERS))
        #z = m.sum(x_p[i] * EP[i] * (1 + cap_p[i] + vice_p[i]) for i in range(prm.TOTAL_PLAYERS))
        m.maximize(z)
        m.solve()
        m.print_solution()

    # Get the solution
    player_id = []
    mainPlayer_id = []
    captain_id = None
    vice_id = None
    in_id = []
    out_id = []
    for i in range(prm.TOTAL_PLAYERS):
        if (prm.gameWeek >= 1):

            if x_p[i].solution_value == 1 and OT[i] == 0: # this week is chosen, last week was not
                in_id.append(i)
            elif x_p[i].solution_value != 1 and OT[i] == 1:
                out_id.append(i)

        if x_p[i].solution_value == 1:
            player_id.append(i)
            OT[i] = 1
        else:
            OT[i] = 0
        if cap_p[i].solution_value == 1:
            captain_id = i
    
        if y_p[i].solution_value == 1:
            mainPlayer_id.append(i)
        if vice_p[i].solution_value == 1:
            vice_id = i
     
    prm.transferLeft = prm.transferLeft - len(out_id)
    prm.chosenPlayerList.append(cht.Chosen_Team(captain_id, vice_id, player_id, mainPlayer_id, prm.transferLeft, prm.point, out_id, in_id))
        
            
            
        
        
        
        
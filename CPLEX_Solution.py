from docplex.mp.model import Model
import parameter as prm
import chosen_team as cht
import stored_old_data as sod



PD = [1 if prm.playerList[i]._position == 'DEF' else 0 for i in range(prm.TOTAL_PLAYERS)]
PM = [1 if prm.playerList[i]._position == 'MID' else 0 for i in range(prm.TOTAL_PLAYERS)]
PF = [1 if prm.playerList[i]._position == 'FWD' else 0 for i in range(prm.TOTAL_PLAYERS)]
PK = [1 if prm.playerList[i]._position == 'GK' else 0 for i in range(prm.TOTAL_PLAYERS)]
# Add-in variables
OT = [0 for _ in range(prm.TOTAL_PLAYERS)]
CS = [0 for _ in range(prm.TOTAL_PLAYERS)]
EP = [0 for _ in range(prm.TOTAL_PLAYERS)]
IFL = [0 for _ in range(prm.TOTAL_PLAYERS)]


# Constants
R = 4
MK = 2
MD = 5
MM = 5
MF = 3
MC = 15
E = 11
EK = 1
ED = 3
EM = 3
EF = 1
BS = 100

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
            if (prm.playerList[i]._total_points == -1 or prm.playerList[i]._red_cards == 1):
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
            # if (gameWeek == 11):
            #     print(f"{prm.playerList[i]._first_name} {prm.playerList[i]._second_name} - {EP[i]} - {IFL[i]}")
        
        
def chooseTeam(gameWeek):
    m = Model(name='FPL')
    # Player is in the team (15 players)
    x_p = m.binary_var_list(prm.TOTAL_PLAYERS, name="x")
    # Player is in main roster (11 players)
    y_p = m.binary_var_list(prm.TOTAL_PLAYERS, name="y")
    cap_p = m.binary_var_list(prm.TOTAL_PLAYERS, name="cap")
    vice_p = m.binary_var_list(prm.TOTAL_PLAYERS, name="vice")
    m.add_constraint(m.sum(x_p[i] for i in range(prm.TOTAL_PLAYERS)) == prm.NUM_OF_PLAYERS)
    m.add_constraint(m.sum(y_p[i] for i in range(prm.TOTAL_PLAYERS)) == prm.PLAYER_REQUIRED)
    for i in range(prm.TOTAL_PLAYERS):
        # This is to ensure player is in the team if he is in the main roster
        m.add_constraint(y_p[i] <= x_p[i])
    # Ensure total budget is not exceeded
    m.add_constraint(m.sum(x_p[i] * CS[i] for i in range(prm.TOTAL_PLAYERS)) <= prm.START_BUDGET)
    
    # This is to ensure the number of players in each position is correct
    m.add_constraint(m.sum(x_p[i] * PK[i] for i in range(prm.TOTAL_PLAYERS)) == MK)
    m.add_constraint(m.sum(x_p[i] * PD[i] for i in range(prm.TOTAL_PLAYERS)) == MD)
    m.add_constraint(m.sum(x_p[i] * PM[i] for i in range(prm.TOTAL_PLAYERS)) == MM)
    m.add_constraint(m.sum(x_p[i] * PF[i] for i in range(prm.TOTAL_PLAYERS)) == MF)
    
    m.add_constraint(m.sum(y_p[i] * PK[i] for i in range(prm.TOTAL_PLAYERS)) == EK)
    m.add_constraint(m.sum(y_p[i] * PD[i] for i in range(prm.TOTAL_PLAYERS)) >= ED)
    m.add_constraint(m.sum(y_p[i] * PM[i] for i in range(prm.TOTAL_PLAYERS)) >= EM)
    m.add_constraint(m.sum(y_p[i] * PF[i] for i in range(prm.TOTAL_PLAYERS)) >= EF)
    
    # This is to ensure there will be only 1 captain and 1 vice captain
    m.add_constraint(m.sum(cap_p[i] for i in range(prm.TOTAL_PLAYERS)) == 1)
    m.add_constraint(m.sum(vice_p[i] for i in range(prm.TOTAL_PLAYERS)) == 1)
    for i in range(prm.TOTAL_PLAYERS):
        # This is to ensure captain and vice captain are in the main roster
        m.add_constraint(cap_p[i] <= y_p[i])
        m.add_constraint(vice_p[i] <= y_p[i])
        # This is to ensure captain and vice captain are different players
        m.add_constraint(cap_p[i] + vice_p[i] <= 1)
    # # This is to ensure vice captain has estimated points less than captain (Errored)
    # d1 = (m.sum(vice_p[i] * (EP[i] * 2 + IFL[i] * 0.04)) for i in range(prm.TOTAL_PLAYERS))
    # d2 = (m.sum(cap_p[i] * (EP[i] * 2 + IFL[i] * 0.04)) for i in range(prm.TOTAL_PLAYERS))
    # m.add_constraint(d1 <= d2)
    
    if (gameWeek == 0):
        z = m.sum(x_p[i] * (EP[i] * (1 + cap_p[i] + vice_p[i]) + IFL[i] * 0.04) for i in range(prm.TOTAL_PLAYERS))
        m.maximize(z)
        m.solve()
        # m.print_solution()
    elif (gameWeek >= 1):
        m.add_constraint(m.sum(m.abs(x_p[i] - OT[i]) for i in range(prm.TOTAL_PLAYERS)) <= prm.transferLeft)
        # z = m.sum(x_p[i] * (EP[i] * (1 + cap_p[i] + vice_p[i]) + IFL[i] * 0.04) for i in range(prm.TOTAL_PLAYERS))
        z = m.sum(x_p[i] * EP[i] * (1 + cap_p[i] + vice_p[i]) for i in range(prm.TOTAL_PLAYERS))
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
            if x_p[i].solution_value == 1 and OT[i] == 0:
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
        
            
            
        
        
        
        
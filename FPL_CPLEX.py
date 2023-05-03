from docplex.mp.model import Model
import numpy as np
# PARAMETERS :
  # Set
# Number of gameweeks:
nT = 38
# Number of players:
nP = 683
# Num of teams
nC = 20
# Num of priorities
nL = 4
# Set of gameweeks
T = [0 for i in range(nT)]
# Set of players
P = [0 for i in range(nP)]
# Set of teams
C = [0 for i in range(nC)]
# Set of priorities
L = [0 for i in range(nL)]
# Subset

PD = [0 for i in range(nP)]
PM = [0 for i in range(nP)]
PF = [0 for i in range(nP)]
#PK = [0 for i in range(nP)]
PK = [1,2,3,4,5]
PC = [0 for i in range(nP)]
TFH = [0 for i in range(nP)]
TSH = [0 for i in range(nP)]
#Parameters

P_pt = [[0]*nT]*nP # nP rows and nT columns 
e = 0.0005
CS_pt = [0 for i in range(nP)]
CB_pt = [0 for i in range(nP)]
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
B = float('inf')
A = float('inf')
# Num of substitues 
Ph = 4
PhK = 1
#Maximum of free tranfers
Qp = 2
Q = 1

x_pt = []
y_pt = []
f_pt = []
h_pt = []
g_ptl = []
u_pt = []
e_pt = []
l_pt = []
v_t = []
q_t = []
al_t = []
def init(player_list):
    nT = 38
    nP = len(player_list)
    nC = 20
    nL = 4

    x_pt = [[0]*nT]*nP
    y_pt = [[0]*nT]*nP
    f_pt = [[0]*nT]*nP
    h_pt = [[0]*nT]*nP
    g_ptl = [[[0]*nL for _ in range(nT)] for _ in range(nP)]
    u_pt = [[0]*nT]*nP
    e_pt = [[0]*nT]*nP
    l_pt = [[0]*nT]*nP
    v_t = [0]*nT
    q_t = [0]*nT
    al_t = [0]*nT

import update_player_data as upd
import get_gw as gw

def run_cplex(week):
    player_list = upd.set_player_list()
    if (week >= 1):
        gw.set_game_week(f"gws\gw{week}.csv", player_list, week)
    nT = 38
    nP = len(player_list)
    nC = 20
    nL = 4

    P_pt = [player_list[i].get_total_points() for i in range(nP)]
    e = 0.0005
    CS_pt = [(float(player_list[i].get_value())*0.7) for i in range(nP)]
    CB_pt = [player_list[i].get_value() for i in range(nP)]
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
    B = float('inf')
    A = float('inf')
    Ph = 4
    PhK = 1
    Qp = 2
    Q = 1
    
    T = [i + 1 for i in range(nT)]
    PL = player_list
    C = [i + 1 for i in range(nC)]
    L = [i + 1 for i in range(nL)]

    PD = [1 if PL[i].get_position() == 'DEF' else 0 for i in range(nP)]
    PM = [2 if PL[i].get_position() == 'MID' else 0 for i in range(nP)]
    PF = [3 if PL[i].get_position() == 'FWD' else 0 for i in range(nP)]
    PK = [4 if PL[i].get_position() == 'GK' else 0 for i in range(nP)]

    init(player_list)
    m = Model()
    x_p = m.binary_var_list(nP, name="x")
    # y_p = m.binary_var_list(nP, name="y")
    f_p = m.binary_var_list(nP, name="f")
    h_p = m.binary_var_list(nP, name="h")
    g_pl = m.binary_var_matrix(nP,nL, name="g")
    u_p = m.binary_var_list(nP, name="u")
    e_p = m.binary_var_list(nP, name="e")
    # l_p =  m.binary_var_list(nP, name="l")
    v = m.integer_var(0,B, name="v")
    # q = m.integer_var(0,B, name="q")
    al = m.integer_var(0,B, name="al")

    # z = m.binary_var(name="z")

    m.add_constraint(m.sum(x_p[i] for i, value in enumerate(PK) if value == 4) == MK)
    m.add_constraint(m.sum(x_p[i] for i, value in enumerate(PD) if value == 1) == MD)
    m.add_constraint(m.sum(x_p[i] for i, value in enumerate(PM) if value == 2) == MM)
    m.add_constraint(m.sum(x_p[i] for i, value in enumerate(PF) if value == 3) == MF)

    # m.add_constraint(m.sum(y_p[i] for i in range(nP)) == E)
    # m.add_constraint(m.sum(y_p[i] for i, value in enumerate(PK) if value == 4) == EK)
    # m.add_constraint(m.sum(y_p[i] for i, value in enumerate(PD) if value == 1) >= ED)
    # m.add_constraint(m.sum(y_p[i] for i, value in enumerate(PM) if value == 2) >= EM)
    # m.add_constraint(m.sum(y_p[i] for i, value in enumerate(PF) if value == 3) >= EF) 

    # for i in range(nP):
    #     m.add_constraint(y_p[i] >= x_p[i] - (1 - z))

    m.add_constraint(m.sum(f_p[i] for i in range(nP))== 1)
    m.add_constraint(m.sum(h_p[i] for i in range(nP))== 1)

    for i in range(nP):
        m.add_constraint(h_p[i] + f_p[i] <= 1)

    m.add_constraint(m.sum(g_pl[i, j] for i in range(nP) for j in range(len(L))) <= 1)
    if (week == 1): 
        m.add_constraint((m.sum(CB_pt[i] * x_p[i] for i in range(nP)) - BS + v) == 0)
    
    if (week >= 2):
        m.add_constraint((v_t[week - 1] + m.sum((CS_pt[i] * u_p[i] for i in range(nP)) - 
                                               (CB_pt[i] * e_p[i] for i in range(nP))) - v) == 0)
        m.add_constraints((x_pt[i][week - 1] + e_p[i] - u_p[i] - x_p[i]) == 0 for i in range(nP))
        m.add_constraint(m.sum(u_p[i] for i in range(nP)) <= E)
        m.add_constraint(m.sum(e_p[i] for i in range(nP)) <= E)
    m.add_constraints((e_p[i] + u_p[i]) <= 1 for i in range(nP))
    # if (week == 2): q = Q
    # m.add_constraint(A * (Qp - q) >= al)
    # m.add_constraint(q >= Q)
    # m.add_constraint(q - Qp <= 0)
    # pointNonCaptain = m.sum((P_pt[i] * y_p[i]) for i in range(nP))
    # pointCaptain = m.sum((P_pt[i] * f_p[i]) for i in range(nP)) * 2
    # pointVice = m.sum((P_pt[i] * h_p[i]) for i in range(nP)) * 1.5
    # (2 if m.sum((P_pt[i] * f_p[i]) for i in P) == 0 else 1)
    # deductedPoints = R * al
    m.maximize(m.sum((P_pt[i] * x_p[i]) for i in range(nP)) + m.sum((P_pt[i] * f_p[i]) for i in range(nP)) * 2 + m.sum((P_pt[i] * h_p[i]) for i in range(nP)) * 1.5 - R * al)

    m.solve()
    m.print_solution()




if __name__ == "__main__":
    run_cplex(0)
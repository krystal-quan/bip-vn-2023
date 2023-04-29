
from docplex.mp.model import Model
m = Model()
import numpy as np

# PARAMETERS :
  # Set
# Number of gameweeks:
nT = 38
# Number of players:
nP = 700
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

#VARIABLES  
x_pt = m.binary_var_matrix(nP,nT,"x_pt")
y_pt = m.binary_var_matrix(nP,nT,"y_pt")
f_pt = m.binary_var_matrix(nP,nT,"f_pt")
h_pt = m.binary_var_matrix(nP,nT,"h_pt")
g_ptl = m.binary_var_cube(nP,nT,nL,"g_ptl")
u_pt = m.binary_var_matrix(nP,nT,"u_pt")
e_pt = m.binary_var_matrix(nP,nT,"e_pt")
# Binary auxiliary variable
l_pt =  m.binary_var_matrix(nP,nT,"l_pt")
v_t = m.integer_var_list(nT,0,B,"v_t")
q_t = m.integer_var_list(nT,0,B,"q_t")
al_t = m.integer_var_list(nT,0,B,"al_t")

#CONSTRAINTS:
  #Selected squad constraints: Note: KeyError is error of wrong methods
  #Do the constraints for each week
  #4.8 -> 4.12 : 
j = 1 # j is the order of the gameweek . = 1,2,...38
m.add_constraint((m.sum(x_pt[i, j] for i in PK)== MK) )#for j in T)
m.add_constraint((m.sum(x_pt[i, j] for i in PD)== MD) )#for j in T)
m.add_constraint((m.sum(x_pt[i, j] for i in PM)== MM) )#for j in T)
m.add_constraint((m.sum(x_pt[i, j] for i in PF)== MF) )#for j in T)
m.add_constraint((m.sum(x_pt[i, j] for i in PC)<= MC) )#for j in T)
  #4.18 -> 4.22 # Bench Boost is ignored!
m.add_constraint((m.sum(y_pt[i, j] for i in P)== E) )#for j in T)
m.add_constraint((m.sum(y_pt[i, j] for i in PK)== EK) )#for j in T)
m.add_constraint((m.sum(y_pt[i, j] for i in PD)>= ED) )#for j in T)
m.add_constraint((m.sum(y_pt[i, j] for i in PM)== EM) )#for j in T)
m.add_constraint((m.sum(y_pt[i, j] for i in PF)== EF) )#for j in T)

  #4.23
m.add_constraints(y_pt[i,j] <= x_pt[i,j] for i in P)

  #4.27-> 4.29 #triple captain is ignored
m.add_constraint((m.sum(f_pt[i, j] for i in P)== 1))# for j in T)
m.add_constraint((m.sum(h_pt[i, j] for i in P)== 1) )#for j in T)
m.add_constraint((m.sum(f_pt[i, j] + h_pt[i, j] - y_pt[i,j] for i in P) <= 0))# for i in P <= y_pt[i,j] for i in P )  for j in T)
  #4.30 -> 4.32
  # get P\PK
P = np.array(P)
PK = np.array(PK)
P__PK = np.delete(P, PK) 
  # calculate g_ptl
#sumGptl = m.sum((g_ptl[i,j,k] for i in P__PK for k in T)
sumGptl = 0
for p in P__PK :
  for l in L :
    sumGptl = sumGptl + g_ptl[p,j,l]

#constraints 4.30-> 4.32 :
def sumArray(matrix, arr, week) :
  sum = 0
  for i in arr :
    sum += matrix[i, week]
  return sum
m.add_constraint(sumArray(y_pt, P__PK, j) + sumGptl - sumArray(x_pt, P__PK, j) <= 0)
# ignore 4.31
m.add_constraint(sumGptl <= 1)
# 4.33 -> 4.36
m.add_constraint((m.sum(CB_pt[i] * x_pt[i,1] for i in P) - BS + v_t[1]) == 0)
if j >= 2 :
  m.add_constraint((m.sum(-(CB_pt[i] * e_pt[i,j] for i in P)+(CS_pt[i] * u_pt[i,j] for i in P) + v_t[j-1] - v_t[j]) == 0))
  m.add_constraints((x_pt[i,j-1] + e_pt[i,j] - u_pt[i,j] - x_pt[i,j]) == 0 for i in P)
  # 4.38, 4.39
  m.add_constraint(sumArray(u_pt, P, j) <= E)
  m.add_constraint(sumArray(e_pt, P, j) <= E)
#4.36
m.add_constraints((e_pt[i,j] + u_pt[i,j]) <= 1 for i in P)

#4.40 -> 4.44 :
q_t[2] = Q
if j >= 2 :
  m.add_constraint(q_t[j] - sumArray(e_pt, P, j) + Q + al_t[j] - q_t[j+1] >= 0 )
m.add_constraint(A * (Qp - q_t[j+1]) >= al_t[j])
m.add_constraint(q_t[j+1] >= Q)
m.add_constraint(q_t[j+1] - Qp <= 0)

# Add constraints for testing : Obligatory transfer
m.add_constraint(m.sum(e_pt[i,j] for i in P ) == 1)
m.add_constraint(m.sum(u_pt[i,j] for i in P) == 1)
# Objective function
# points for  'normal' players (except cap, vice-cap)
def calculateSumPoint (arr2D, arr, matrix, week) :
  return m.sum(arr2D[i][week] * matrix[i, week] for i in arr)
pointNonCaptain = calculateSumPoint(P_pt, P, y_pt, j)
#pointNonCaptain = m.sum(P_pt[i][j] * y_pt[i, j] for i in P)
pointForCaptain = calculateSumPoint(P_pt, P, f_pt, j)
#pointForCaptain = m.sum(P_pt[i][j] * f_pt[i, j] for i in P)
pointForViceCap = calculateSumPoint(P_pt, P, h_pt, j)
#pointForViceCap = m.sum(e * P_pt[i][j]  * h_pt[i, j] for i in P)
pointDeducted =  R * al_t[j]
m.maximize(pointNonCaptain + pointForViceCap + pointForCaptain - pointDeducted)

#Choose the first week squad
#550 is Peter Cetch
# 2 GK, 5 DEF, 5 MID, 3 FWD
squad = [550, 172, 273, 60, 643, 132, 663, 569, 503, 81, 575, 651, 267, 577, 473]
starting = [550, 273, 60, 643, 569, 503, 81, 575, 267, 577, 473]
captain = [267]
for i in squad :
  x_pt[i, 1] = 1
for i in starting :
  y_pt[i, 1] = 1
for i in captain : 
  f_pt[i, 1] = 1
print("Points of Week 1 is :")
pointWeek1 = calculateSumPoint(P_pt, starting, y_pt, 1) + calculateSumPoint(P_pt, captain, f_pt, 1)
print(pointWeek1)

  
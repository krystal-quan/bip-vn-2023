class Parameter:
    #Parameters:
    def __init__(self):
        self
        self.eConstant = 1e-5
        self.deductedPoint = 0
        self.goalKeeperSelected = 2
        self.defenderSelected = 5
        self.midFielderSelected = 5
        self.forwardSelected = 3
        self.maxSameTeamSelected = 3
        self.playerRequired = 11
        self.goalKeeperRequired = 1
        self.defenderRequired = 3
        self.midFielderRequired = 3
        self.forwardRequired = 1
        self.startBudget = 100 # do các cầu thủ để giá trị là 5.0, 4.6,
                            #bla bla nên đơn vị tiền để 100 thôi
        self.beta = 1e5
        self.alpha = 1e5
        self.subPlayers = 4
        self.subGoal = 1
        self._q = 1
        self.q_ = 2

    def getEConstant(self):
        return self.eConstant

    def setEConstant(self, value):
        self.eConstant = value

    def getDeductedPoint(self):
        return self.deductionPoint
    
    def setDeductedPoint(self, deductionPoint_):
        self.deductionPoint = deductionPoint_

    def getGoalKeeperSelected(self):
        return self.goalKeeperSelected
    
    def setGoalKeeperSelected(self, goalKeeperSelected_):
        self.goalKeeperSelected = goalKeeperSelected_

    def getDefenderSelected(self):
        return self.defenderSelected
    
    def setDefenderSelected(self, defenderSelected_):
        self.defenderSelected = defenderSelected_

    def getMidFielderSelected(self):
        return self.midFielderSelected
    
    def setMidFielderSelected(self, midFielderSelected_):
        self.midFielderSelected = midFielderSelected_
    
    def getForwardSelected(self):
        return self.forwardSelected
    
    def setForwardSelected(self, forwardSelected_):
        self.forwardSelected = forwardSelected_

    def getMaxSameTeamSelected(self):
        return self.maxSameTeamSelected
    
    def setMaxSameTeamSelected(self, maxSameTeamSelected_):
        self.maxSameTeamSelected = maxSameTeamSelected_

    def getPlayerRequired(self):
        return self.playerRequired
    
    def setPlayerRequired(self, playerRequired_):
        self.playerRequired = playerRequired_

    def getGoalKeeperRequired(self):
        return self.goalKeeperRequired
    
    def setGoalKeeperRequired(self, goalKeeperRequired_):
        self.goalKeeperRequired = goalKeeperRequired_
    
    def getDefenderRequired(self):
        return self.defenderRequired
    
    def setDefenderRequired(self, defenderRequired_):
        self.defenderRequired = defenderRequired_

    def getMidFielderRequired(self):
        return self.midFielderRequired
    
    def setMidFielderRequired(self, midFielderRequired_):
        self.midFielderRequired = midFielderRequired_

    def getForwardRequired(self):
        return self.forwardRequired
    
    def setForwardRequired(self, forwardRequired_):
        self.forwardRequired = forwardRequired_

    def getStartBudget(self):
        return self.startBudget
    
    def setStartBudget(self, startBudget_):
        self.startBudget = startBudget_

    def getBeta(self):
        return self.beta
    
    def setBeta(self, beta_):
        self.beta = beta_

    def getAlpha(self):
        return self.alpha
    
    def setAlpha(self, alpha_):
        self.alpha = alpha_

    def getSubPlayer(self):
        return self.subPlayer
    
    def setSubPlayer(self, subPlayer_):
        self.subPlayer = subPlayer_

    def getSubGoal(self):
        return self.subGoal
    
    def setSubGoal(self, subGoal_):
        self.subGoal = subGoal_

    def get_q(self):
        return self._q
    
    def set_q(self, _q_):
        self._q = _q_

    def getQ_(self):
        return self.q_
    
    def setQ_(self, q__):
        self.q_ = q__

        
point = []
kconstant = []
sellPrice = []
playerValue = []
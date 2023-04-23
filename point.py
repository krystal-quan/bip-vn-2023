class Point:
    totalPoints = 0
    pointList = []
    
    def __init__(self, points):
        self.points = points
        Point.totalPoints += points
        Point.pointList.append(points)
        
    def __str__(self):
        return f"Total points: {Point.totalPoints}\nPoints per game: {Point.getPointsPerGame()}"
        
    def getPoints(self, gameWeek):
        return f"GameWeek {gameWeek}: {Point.pointList[gameWeek - 1]}"
    
    def getTotalPoints(self):
        return Point.totalPoints
    
    def getPointsPerGame(self):
        for i in range(len(Point.pointList)):
            return f"{Point.getPoints(i + 1)}"
    
# TODO: Decide whether this is a good idea or not
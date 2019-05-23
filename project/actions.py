import math
import reader
#figure out a list of actions in order to remove the next block on the same level
#input: final grid, current position
def getNextActions(goal_grid, curPos):
    goingTo = findClosest(goal_grid, curPos)
    #go towards it so get absolute values? and one step forward in that direction unless stuck
    pass


def findClosest(goal_grid, curPos):
    dist = 1
    blocks = getOnY(goal_grid, curPos[0]) 
    while(True):
        for x, y in [(dist, 0), (-dist, 0), (dist, dist), (dist, -dist), (0, dist), (0, -dist), (-dist, dist), (-dist, -dist)]:
            curChecking = (curPos[1] + x, curPos[2] + y)
            if(checkInGrid(goal_grid, curChecking)):
                if(blocks.contains(curChecking)):
                    return curChecking
        dist += 1
def checkInGrid(goal_grid, check):
    return (check[1] > 0) and (check[2] > 0) and (check[1] < goal_grid[0].length) and (check[2] < goal_grid[0][0].length)

def getCost(pos1, pos2, goal_grid):
    return math.sqrt(abs(pos1[0] - pos2[0])**2 + abs(pos1[1] - pos2[1])**2 + abs(pos1[2] - pos2[2])**2 )
#
# def getCostWeighted(pos1, pos2, goal_grid):
#     return (math.sqrt(abs(pos1[0] - pos2[0])**2 + abs(pos1[1] - pos2[1])**2 + abs(pos1[2] - pos2[2])**2))+(1 if (pos1[2]!=pos2[2]) else 0)

def minDistance(dist, goal, sptSet): 
        mini = float('inf')
        # print(dist)
        length = len(goal)
        min_index = 0
        for v in range(length): 
            if dist[v] < mini and sptSet[v] == False: 
                mini = dist[v] 
                min_index = v
        return min_index

def listActions(curPos, goal_grid):
    startingGoal = list(goal_grid.copy())
    startingGoal.insert(0, curPos)
    graph = [[getCost(pos1, pos2, goal_grid) for pos1 in startingGoal]  for pos2 in startingGoal]
    length = len(startingGoal)
    sptSet = [False] * length
    dist = [float('inf')] * length
    dist[0] = 0
    finalList = []
    for cout in range(length): 
        u = minDistance(dist, startingGoal, sptSet) 
        sptSet[u] = True
        for v in range(length): 
            if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v] 
        finalList.append(startingGoal[u])
    return finalList[1:]

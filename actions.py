
#figure out a list of actions in order to remove the next block on the same level
#input: final grid, current position
def getNextActions(goal_grid, curPos):
    goingTo = findClosest(goal_grid, curPos)
    #go towards it so get absolute values? and one step forward in that direction unless stuck
    pass


def findClosest(goal_grid, curPos):
    dist = 1
    blocks = getBlocksSameFloor(goal_grid, curPos[0]) #I think Aditya is writing this command
    while(True):
        for x, y in [(dist, 0), (-dist, 0), (dist, dist), (dist, -dist), (0, dist), (0, -dist), (-dist, dist), (-dist, -dist)]:
            curChecking = (curPos[1] + x, curPos[2] + y)
            if(checkInGrid(goal_grid, curChecking)):
                if(blocks.contains(curChecking)):
                    return curChecking
        dist += 1

def checkInGrid(goal_grid, check):
    return (check[1] > 0) and (check[2] > 0) and (check[1] < goal_grid[0].length) and (check[2] < goal_grid[0][0].length)
    
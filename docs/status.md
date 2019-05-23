---
layout: default
title:  Status
---

##  Project Summary

Our project, the Minecraft Plagiarizer creates a building in Minecraft. The user gives it a building as defined by locations of filled blocks with their corresponding types, and this Plagiarizer generates the best way to create the building. The efficiency for our project is determined by minimizing the distance the agent has to travel while building the provided structure.

The input is a dictionary where keys are the locations for the blocks and they correspond the type of block that needs to be placed. The output is the cost to build the structure, where cost is the total distance travelled by the agent.

## Approach

Currently, we use modified Dijkstra's algorithm in order to figure out the closest blocks to our position and then use that to figure out the order of the placement of blocks. 
Although this algorithm is significantly better than the random case, we understand that there are certain issues with Dijkstra's algorithm, as defined in the Evaluation section, but we seek to improve it as written in the Remaining Goals and Challenges section.

Inputs
* Current position
* Dictionary of all of the blocks that need to be placed
..* key: tuple of the location of the block
..* value: type of block that needs to be placed

Process
We are using Dijkstra's algorithm, which looks at all the blocks and trys to figure out which blocks are closest to the current location, and which are further, and places them in order according to our cost function. The cost function is the distance in 3D space between the block that needs to be placed and the current location.

```python
for v in range(length): 
    if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v] 
    finalList.append(startingGoal[u])
```


Output
* List of blocks that need to be added in the order that they need to be added
* Once the output has been sent, the agent goes to each position sequentially and adds the correct type of block to the correct position.
* Total distance traveled    

## Evaluation

Missions
1. Two separated single blocks on the ground floor
2. Two separate towers, one being wider than the other, both four layers tall
3. Three block tall single block wide tower
4. Two separate towers, one being taller than the other
5. The front facade of a house

![Mission 4 House](https://raw.githubusercontent.com/thebrainygeek/plagiarism/master/docs/images/image1.PNG)

Cost Function
Distance between two points

```python
def getCost(pos1, pos2, goal_grid):
    return math.sqrt(abs(pos1[0] - pos2[0])**2 + abs(pos1[1] - pos2[1])**2 + abs(pos1[2] - pos2[2])**2 )
```

Quantitative Efficiency
We use the total distance traveled, or the sum of all of the distances traveled to place all of the blocks, in order to determine how efficient our algorithm is. 

We compare the total distance traveled to that of a **smart random algorithm**. This algorithm works bottom up, from the bottom layer to the top. Within each layer it chooses the blocks completely randomly.

| Mission Number| Random Algorithm | Our Algorithm  |
| ------------- |:----------------:| :-------------:|
| 1             | 6.78             | 6.78           |
| 2             | 9.89             | 9.89           |
| 3             | 121.4            |      100.9     |
| 4             | 276.9            |      116.6     |

**Dijkstra's algorithm:** Although this works well, one of the issues with our algorithm is that since it compares everything from the central block, the list is radially outward. This does not make much of a difference in the smaller structures, but in larger ones it has the potential to be a significant source of inefficiency as the blocks chosen will be on an outward circle over time, and will have to move a lot to go across the center of the system. This issue occurs in 3D space, which makes everything all the odder.


## Remaining Goals and Challenges
We would like to improve our current algorithm, perhaps by using the [Traveling Salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem) Problem as a guide. Perhaps we can give preference to staying on the same floor, but this would need to be tested.

One major assumption that we have made is that if there is a block that is supposed to be placed we can assume that there are blocks below it through to the ground floor. For example, if there is a block on the 3rd level at position x,y, then there must be a block at position x, y for levels 1 and 2. In other words, we do not account for arches, nor free windows (although glass is okay). 

An issue with our solution is that currently sometimes it creates double blocks. Although this is issue is greatly reduced from the earlier issue where it would sometimes not place the block at the right place, this is something we would like to fix.

We would like to run this algorithm on much taller, larger, and more diverse buildings that allow greater room for error.

## Resources Used

We looked towards Campuswire for solutions to many of our problems. We also Assignment 1 to help with our algorithm.

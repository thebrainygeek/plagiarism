---
layout: default
title:  Status
---

##  Project Summary

Our project, the Minecraft Plagiarizer creates a 3D structure in Minecraft. The input is the list of blocks (location and type) required to build the structure, and the Plagiarizer generates the most efficient order of blocks to build the structure. The efficiency for our project is determined by minimizing the distance the agent has to travel while building the provided structure.

The input is a dictionary where keys are the locations for the blocks and the value is the type of the block that needs to be placed at that particular location. The output is the cost to build the structure, where cost is the total distance travelled by the agent.

## Approach

Currently, we use modified Dijkstra's algorithm in order to figure out the closest blocks to our position and then use that to figure out the order of the placement of blocks. 
Although this algorithm is significantly better than the random case, we understand that there are certain issues with Dijkstra's algorithm, as defined in the Evaluation section, but we seek to improve it as written in the Remaining Goals and Challenges section.

Inputs
* Current position
* Dictionary of all of the blocks that need to be placed
* key: tuple of the location of the block
* value: type of block that needs to be placed

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
1. 2 separated single blocks on the ground floor
2. 3 block tall 1 block wide tower
3. Front facade of a house
4. 2 separate structures
5. 7x7 hollow structure

![Mission 4 Structure](https://raw.githubusercontent.com/thebrainygeek/plagiarism/master/docs/images/image1.PNG)

**Cost Function**
Distance between two points

```python
def getCost(pos1, pos2, goal_grid):
    return math.sqrt(abs(pos1[0] - pos2[0])**2 + abs(pos1[1] - pos2[1])**2 + abs(pos1[2] - pos2[2])**2 )
```

**Quantitative Efficiency**
We use the total distance traveled, or the sum of all of the distances traveled to place all of the blocks, in order to determine how efficient our algorithm is. 

We compare the total distance traveled to that of a **smart random algorithm**. This algorithm starts from the bottom level and works upward. Within each level it chooses the blocks completely randomly.

**Missions**

| Mission Number | Smart Random | Ours | % Difference |
| --------- | ------- | ------- | ------- |
| 1 | 6.78 | 6.78 | 0% |
| 2 | 9.89 | 9.89 | 0% |
| 3 | 121.4 | 100.9 | -16.88633% |
| 4 | 276.9 | 116.6 | -57.8909% |
| 5 | 462.4 | 344.37 | -25.5255% | 

For the really small towers there are not many orders that can be made, so the algorithms work the same. Then, for slightly larger structures we can see our algorithm shine. For larger structures, the algorithm does not work as well because of the issue stated below.

**Dijkstra's algorithm:** 
The biggest issue with our algorithm is that since the algorithm compares everything from the central block, the list is radially outward. This does not make much of a difference in the smaller structures, but in larger ones it has the potential to be a significant source of inefficiency as the blocks chosen will be on an outward circle over time, and will have to move a lot to go across the center of the system. This issue occurs in 3D space, which makes everything all the odder.


## Remaining Goals and Challenges
We would like to improve our current algorithm, perhaps by using the [Traveling Salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem) Problem as a guide. Perhaps we can give preference to staying on the same floor, but this would need to be tested.

One major assumption that we have made is that if there is a block that is supposed to be placed we can assume that there are blocks below it through to the ground floor. For example, if there is a block on the 3rd level at position x,y, then there must be a block at position x, y for levels 1 and 2. In other words, we do not account for arches, nor free windows (although glass is okay). 

An issue with our solution is that currently sometimes it creates double blocks. Although this is issue is greatly reduced from the earlier issue where it would sometimes not place the block at the right place, this is something we would like to fix.

We would like to run this algorithm on much taller, larger, and more diverse buildings.

## Resources Used

We looked towards Campuswire for solutions to many of our problems. We also Assignment 1 to help with our algorithm.

# Status Video

[![](http://img.youtube.com/vi/7LxSEu_OBNw/0.jpg)](https://www.youtube.com/watch?v=hBs6EC-p6tk&feature=share "Plagiarism Video")

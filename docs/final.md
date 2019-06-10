---
layout: default
title:  Home
---

# Plagiarism

## Video
Use speech this time:
Problem description: 3D structure, copier, dictionary, traveling salesman, nearest neighbor, accounts for height, checks item below is already placed.
baseline random: look at this
neearest neighbor: look at the smarts


## Project Summary
Our project, the Minecraft Plagiarizer creates a 3D structure in Minecraft. The input is the list of blocks (location and type) required to build the structure, and the Plagiarizer generates the most efficient order of blocks to build the structure. The efficiency for our project is determined by minimizing the distance the agent has to travel while building the provided structure.

The input is a dictionary where keys are the locations for the blocks and the value is the type of the block that needs to be placed at that particular location. The output is the cost to build the structure, where cost is the total distance travelled by the agent. This problem can be summarized by the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), where  and we used the [Nearest Neighbor Solution](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm?fbclid=IwAR0C8TO1ORfp6sNmwoBE1F9ggGoWsAIZdxSdivXJWpt1BQIZaxFs0FM74Lk) to solve it.

## Approaches
In the beginning, we used modified Dijkstra’s algorithm in order to figure out the closest blocks to our position and then use that to figure out the order of the placement of blocks. Although this algorithm is significantly better than the random case, we understand that there are certain issues with Dijkstra’s algorithm. Since the algorithm compares everything from the central block, the list is radially outward. This does not make much of a difference in the smaller structures, but in larger ones it has the potential to be a significant source of inefficiency as the blocks chosen will be on an outward circle over time, and will have to move a lot to go across the center of the system. This issue occurs in 3D space, which makes everything all the odder. 

``` python
for v in range(length): 
    if graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + graph[u][v]:
        dist[v] = dist[u] + graph[u][v] 
    finalList.append(startingGoal[u])
```


Therefore, we recognize the problem as a Traveling Salesman problem and implement the Nearest neighbour algorithm to solve it. The nearest neighbour algorithm starts at a random block and repeatedly visits the nearest block until all have been visited. However, there are still some problems existing, and we will mention them in the evaluation part.
Inputs
* Current position
* Dictionary of all of the blocks that need to be placed
* key: tuple of the location of the block
* value: type of block that needs to be placed

Process We are using Nearest neighbour algorithm, which initialize all blocks as unvisited, visit an arbitrary block, set it as the current block and mark it as visited, and find out the shortest path connecting the current block and an unvisited block by using our cost functions. The cost function is the distance in 3D space between the block that needs to be placed and the current location. If all the blocks in the dictionary are visited, then terminated. Else, keep visiting the remaining blocks.

Output
* List of blocks that need to be added in the order that they need to be added
* Once the output has been sent, the agent goes to each position sequentially and adds the correct type of block to the correct position.
* Total distance traveled


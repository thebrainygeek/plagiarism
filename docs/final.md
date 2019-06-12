---
layout: default
title:  Home
---

# Plagiarism

## Video
Use speech this time:
Problem description: 3D structure, copier, dictionary, traveling salesman, nearest neighbor, accounts for height, checks item below is already placed, prioritixes staying on the same floor.
baseline random: look at this
neearest neighbor: look at the smarts


##Project Summary
Our project, the Minecraft Plagiarizer creates a 3D structure in Minecraft. The input is the list of blocks (location and type) required to build the structure, and the Plagiarizer generates the most efficient order of blocks to build the structure. The efficiency for our project is determined by minimizing the distance the agent has to travel while building the provided structure.

The input is a dictionary where keys are the locations for the blocks and the value is the type of the block that needs to be placed at that particular location. The output is the cost to build the structure, where cost is the total distance travelled by the agent. 

This problem can be summarized by the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), where  and we used the [Nearest Neighbor Solution](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm?fbclid=IwAR0C8TO1ORfp6sNmwoBE1F9ggGoWsAIZdxSdivXJWpt1BQIZaxFs0FM74Lk) to solve it.

##Approaches

##Evaluation
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

We compare the total distance traveled for three levels:
**smart random**: starts from the bottom level and works upward. Within each level it chooses the blocks completely randomly.
**dijkstra's**: places all of the blocks in order from the current location
**nearest neighbor's**: iteravely finds the closest block from the location at the previous iteration

**add other smaller improvements here**

**Missions**

| Mission Number | Smart Random | Dijkstra's | Nearest Neighbor |
| --------- | ------- | ------- | ------- |
| 1 | 6.78 | 6.78 (0%) | 6.78 (0%) |
| 2 | 9.89 | 9.89 (0%) | 9.89 (0%) |
| 3 | 121.4 | 100.9 (-16.8%) | 70.39 (-42.1%) |
| 4 | 276.9 | 116.6 (-57.9%) | 81.45 (-70.5%) |
| 5 | 462.4 | 344.37 (-25.5%) | 149.6 (-67.6%) | 

![Chart](https://raw.githubusercontent.com/thebrainygeek/plagiarism/master/docs/images/graph1.png)

**insert chart with changes over time**
columns, algorithm level
rows, length
one line per missionn

For the really small towers there are not many orders that can be made, so the algorithms work the same. Then, we see a significant drop of the Dijkstra's and Nearest Neighbor algorithms compared to the smart random algorithm. Then, the Dijkstra's algorithm stops being a significant improvement compared to the smart random algorithm, and Nearest Neighbor is signficantly better than the other two for the largest structures.

##References

https://github.com/topics/travelling-salesman-problem?l=python

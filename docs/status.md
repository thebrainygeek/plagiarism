---
layout: default
title:  Status
---

##  Project Summary

Our project, the Minecraft Plagiarizer, compares efficiency of different methods to build an input structure provided to it. The efficiency for our project is determined by minimizing the distance the agent has to travel while building the provided structure.
The input is a dictionary where keys are the locations for the blocks and they correspond the type of block that needs to be placed. The output is the cost to build the structure, where cost is the total distance travelled by the agent.

## Approach

Currently, we use modified Dijkstra's algorithm in order to figure out the closest blocks to our position and then use that to figure out the order of the placement of blocks. We understand the shortfalls with Dijkstra's for our problem but we use it as our stepping stone as we progress towards utilizing more complex concepts like the Travelling Salesman.

Inputs
* Current position
* Dictionary of all of the blocks that need to be placed
    .. * key: tuple of the location of the block
    .. * value: type of block that needs to be placed


Output
* List of blocks that need to be added in the order that they need to be added
* Once the output has been sent, the agent goes to each position sequentially and adds the correct type of block to the correct position.

Algorithm
    Cost Function: distance between the block that needs to be placed and the current position
    

## Evaluation

Missions
1. Two random separated blocks on the ground floor
2. One moderately tall tower, 1 block wide
3. Two seperate structures, each multiple blocks tall
4. The front facade of a house

Cost Function: distance between the block that needs to be placed and the current position

Creation of the object:
Before testing that the algorithm is effeicient, we need to check the worst-case scenario that it works.

Insert images of each mission here


Efficiency
We use the total distance traveled, or the sum of all of the distances traveled to place all of the blocks, in order to determine how efficient our algorithm is. 

We compare the total distance traveled to that of a **smart random algorithm**. This algorithm works bottom up, from the bottom layer to the top. The randomness is in the fact that within each layer it chooses the blocks completely randomly.

Insert chart of comparisons of time for all missions

Although this works well, one of the issues with our algorithm is that since it compares everything from the central block, the list is radially outward. This does not make much of a difference in the smaller structures, but in larger ones it has the potential to be a significant source of inefficiency as the blocks chosen will be on an outward circle over time, and will have to move a lot to go across the center of the system. This issue occurs in 3D space, which makes everything all the odder.


## Remaining Goals and Challenges
We would like to improve our current algorithm, perhaps by using the [Traveling Salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem) Problem as a guide. Perhaps we can give preference to staying on the same floor, but this would need to be tested.

One major assumption that we have made is that since we are only building towers, if there is a block that is supposed to be placed we can assume that all the blocks below it need to be placed.

An issue with our output is that currently sometimes it creates double blocks. Although this is issue is greatly reduced from the earlier issue where it would sometimes not place the block at the right place, this is something we would like to fix.

We would like to run this algorithm on much taller, larger, and more diverse buildings that allow greater room for error.

## Resources Used

We looked towards Campuswire for solutions to many of our problems.

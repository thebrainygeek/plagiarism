---
layout: default
title:  Status
---

#  Project Summary

Our project is the Minecraft Plagiarizer wherein our AI algorithm will attempt to provide an order to build a Minecraft structure based on the input structure provided to it. The AI will try to determine, through artificial intelligence, a possible order to build the structure which may be impossible for brute-force since it is easy for the agent to not be able to progress if it is built in the wrong order. The algorithm needs to find an order that does not block the agent from building the rest of the structure after putting down a block as it builds the structure and creates a structure in the least total distance traveled. 
The input will be a 3-dimensional array of types of blocks that need to be placed for the final structure. The output will be the order in which the agent needs to place or remove the blocks to correctly build the given structure.

## Approach

Currently, we use **Dijkstra's algorithm** in order to figure out the closest blocks to our position and then use that to figure out the placement of blocks. 

Inputs
* Current position
* Dictionary of all of the blocks that need to be placed
    .. * key: tuple of the location of the block
    .. * value: type of block that needs to be placed (Currently we use "stone" type only)


Output
* List of blocks that need to be added in the order that they need to be added
* Once the output has been sent, the agent goes to each position sequentially and adds the correct type of block to the correct position.

Algorithm
    Cost Function: distance between the block that needs to be placed and the current position
    
## Evaluation

Missions
1. Two random separated blocks on the ground floor
2. Two separated several layer three blocks long towers  <-- please change later with mission 4
3. One three level one block long tower
4. One separated several layer three blocks long towers

Cost Function: distance between the block that needs to be placed and the current position

Creation of the object:
Before testing that the algorithm is effeicient, we need to check the worst-case scenario that it works.

Insert images of each mission here

Efficiency
We use the total distance traveled, or the sum of all of the distances traveled to place all of the blocks, in order to determine how efficient our algorithm is. 

We compare the total distance traveled to that of a smart random algorithm. This algorithm works bottom up, from the bottom layer to the top. The randomness is in the fact that within each layer it chooses the blocks completely randomly.

Insert chart of comparisons of time for all missions

Although this works well, one of the issues with our algorithm is that since it compares everything from the central block, the list is radially outward. This does not make much of a difference in the smaller structures, but in larger ones it has the potential to be a significant source of inefficiency as the blocks chosen will be on an outward circle over time, and will have to move a lot to go across the center of the system. This issue occurs in 3D space, which makes everything all the odder.


## Remaining Goals and Challenges
We would like to improve our current algorithm, perhaps by using the [Traveling Salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem) Problem as a guide. 


One major assumption that we have made is that since we are only building towers, if there is a block that is supposed to be placed we can assume that all the blocks below it need to be placed.

An issue with our output is that currently sometimes it creates double blocks. Although this is issue is greatly reduced from the earlier issue where it would sometimes not place the block at the right place, sometimes this does happen.

We would like to run this algorithm on much taller, larger, and more diverse buildings that allow greater room for error.

## Resources Used

We looked towards Campuswire for solutions to many of our problems.
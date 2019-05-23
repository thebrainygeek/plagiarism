---
layout: default
title:  Status
---

## Project Summary

Our project is the Minecraft Plagiarizer wherein our AI algorithm will attempt to provide an order to build a Minecraft structure based on the input structure provided to it. The AI will try to determine, through artificial intelligence, a possible order to build the structure which may be impossible for brute-force since it is easy for the agent to not be able to progress if it is built in the wrong order. The algorithm needs to find an order that does not block the agent from building the rest of the structure after putting down a block as it builds the structure and creates a structure in the least total distance traveled. 
The input will be a 3-dimensional array of types of blocks that need to be placed for the final structure. The output will be the order in which the agent needs to place or remove the blocks to correctly build the given structure.

## Approach

Currently, we use Dijkstra's algorithm in order to figure out the closest blocks to our position and then use that to figure out the placement of blocks. 

Inputs
* Current position
* Dictionary of all of the blocks that need to be placed
    .. * key: tuple of the location of the block
    .. * value: type of block that needs to be placed (Currently we use "stone" type only)


Output
* List of blocks that need to be added in the order that they need to be added

Algorithm
    Cost Function: distance between the block that needs to be placed and the current position
    Gives preference to the current floor.

## Evaluation

Missions
1. Two random separated blocks on the ground floor
2. Two separated several layer three blocks long towers  <-- please change later with mission 4
3. One three level one block long tower
4. One separated several layer three blocks long towers

Cost Function: distance between the block that needs to be placed and the current position

Evaluation:
total distance traveled (sum of all of the distances traveled to place all of the blocks)


## Remaining Goals and Challenges
We would like to improve our current algorithm, perhaps by using the [Traveling Salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem) Problem as a guide. This would fix the issue that we currently h

One major assumption that we have made is that since we are only building towers, if there is a block that is supposed to be placed we can assume that all the blocks below it need to be placed.

We also currently only work with one type of material and would like to expand our horizons so that the correct type of material is placed at the right time. 

We would like to run this algorithm on much taller buildings that allow greater room for error.

## Resources Used

We looked towards Campuswire for solutions to many of our problems.
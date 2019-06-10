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


##Project Summary
Our project, the Minecraft Plagiarizer creates a 3D structure in Minecraft. The input is the list of blocks (location and type) required to build the structure, and the Plagiarizer generates the most efficient order of blocks to build the structure. The efficiency for our project is determined by minimizing the distance the agent has to travel while building the provided structure.

The input is a dictionary where keys are the locations for the blocks and the value is the type of the block that needs to be placed at that particular location. The output is the cost to build the structure, where cost is the total distance travelled by the agent. This problem can be summarized by the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), where  and we used the [Nearest Neighbor Solution](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm?fbclid=IwAR0C8TO1ORfp6sNmwoBE1F9ggGoWsAIZdxSdivXJWpt1BQIZaxFs0FM74Lk) to solve it.

##Approaches
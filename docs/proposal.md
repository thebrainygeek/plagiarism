---
layout: default
title: Proposal
---
## Summary

Our project is the Minecraft Plagiarizer wherein our AI algorithm will attempt to provide an order to build a Minecraft structure based on the input structure provided to it. The AI will try to determine, through reinforcement learning, a possible order to build the structure which may be impossible for brute-force since it is easy for the agent to not be able to progress if it is built in the wrong order. The Minecraft character (agent) can only act on or move to the blocks that immediately surround it. The algorithm needs to find an order that does not block the agent from building the rest of the structure after putting down a block as it builds the structure. 
The input will be a 3-dimensional array of types of blocks that need to be placed for the final structure. The output will be the order in which the agent needs to place or remove the blocks to correctly build the given structure.

## AI/ML Algorithms

Our AI algorithm will use reinforcement learning, using a reward system determined by the progress made towards the final goal, as builds the structure in multiple attempts, having to restart every time the agent is stuck, dead or unable to progress towards building the input structure. 

## Evaluation

To evaluate this algorithm’s success we plan to start by comparing its speed against the brute-force method. If we are able to successfully decrease our building time drastically over the brute-force method, we would further challenge the algorithm to build much more complex structures which the brute-force method cannot. The baseline provided by the brute-force method will help us improve our reward system and correctly weigh the mistakes.
For our sanity cases, we will be using input structures that do not grow in height or require the agent to change their height while building it. The sanity case structure will only require the agent to move around a 2-dimensional plane and place blocks to match the input.
We can visualize our progress towards the goal by watching the agent build more of the structure every time it has to restart.
Our moonshot case is to build a structure that spans over one hundred levels and requires over one thousand blocks to be placed.


## Appointment

10:45am - 11:00am, Wednesday, April 24, 2019
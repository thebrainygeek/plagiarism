from __future__ import print_function
from future import standard_library

standard_library.install_aliases()
from builtins import range
from builtins import object
import MalmoPython
import json
import logging
import os
import random
import sys
import time
import reader
import math
from mission.mission6 import missionFile
from actions import getCost, listActions, nearestN

if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk


def teleport(agent_host, teleport_x, teleport_y, teleport_z):
    tp_command = "tp " + str(teleport_x) + " " + str(teleport_y) + " " + str(teleport_z)
    # print(tp_command)
    agent_host.sendCommand(tp_command)


MODE = "TSP"

class PlagiarismAgent(object):
    """Tabular Q-learning agent for discrete state/action spaces."""

    def __init__(self):
        self.epsilon = 0.01  # chance of taking a random action instead of the best

        self.logger = logging.getLogger(__name__)
        if False:  # True if you want to see more information
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        self.logger.handlers = []
        self.logger.addHandler(logging.StreamHandler(sys.stdout))

        self.actions = ["movenorth 1", "movesouth 1", "movewest 1", "moveeast 1"]
        self.canvas = None
        self.root = None

    def run(self, agent_host):
        """run the agent on the world"""

        total_cost = 0

        self.prev_s = None
        self.prev_a = None
        input = missionFile
        current_level = 0
        current_blocks = {}
        world_state = agent_host.getWorldState()
        if MODE == "RANDOM":
            while world_state.is_mission_running and current_blocks != input:
                remaining_floor = reader.getOnZ(input, current_level)
                while len(remaining_floor) > 0:
                    target = random.choice(list(remaining_floor.keys()))
                    print("Chosen Block",target)
                    location = []
                    load_location(world_state, location)
                    block_type = input[target]
                    move_to_target(location, target, world_state, current_blocks, block_type)
                    del remaining_floor[target]
                    current_blocks[target] = block_type
                    total_cost += getCost([location[0], location[1], location[2]],
                                          [target[0] - 0.5, target[1] - 0.5, target[2]])
                    print("COST IS", total_cost, "\n")
                current_level += 1
            return total_cost
        elif MODE == "DIK":
            location = []
            load_location(world_state, location)
            actions = listActions((location[0], location[1], location[2]), input)
            while world_state.is_mission_running and current_blocks != input:
                target = actions[0]
                print("Chosen Block",target)
                location = []
                load_location(world_state, location)
                block_type = input[target]
                move_to_target(location, target, world_state, current_blocks, block_type)
                del actions[0]
                current_blocks[target] = block_type
                total_cost += getCost([location[0], location[1], location[2]],
                                      [target[0] - 0.5, target[1] - 0.5, target[2]])
                print("COST IS", total_cost, "\n")
                current_level += 1
            return total_cost
        elif MODE == "TSP":
            location = []
            load_location(world_state, location)
            actions = nearestN((location[0], location[1], location[2]), input)
            while world_state.is_mission_running and current_blocks != input:
                target = actions[0]
                print("Chosen Block", target)
                location = []
                load_location(world_state, location)
                block_type = input[target]
                move_to_target(location, target, world_state, current_blocks, block_type)
                del actions[0]
                current_blocks[target] = block_type
                total_cost += getCost([location[0], location[1], location[2]],
                                      [target[0] - 0.5, target[1] - 0.5, target[2]])
                print("COST IS", total_cost, "\n")
                current_level += 1
            return total_cost


if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools

    print = functools.partial(print, flush=True)

agent = PlagiarismAgent()
agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse(sys.argv)
except RuntimeError as e:
    print('ERROR:', e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)


def load_location(world_state, location):
    while world_state.is_mission_running:
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load loaction.')

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            observations = json.loads(msg)
            location.append(observations[u'XPos'])
            location.append(observations[u'ZPos'])
            location.append(observations[u'YPos'])
            break


def move_to_target(location, target, world_state, exist_floor, block_type):
    location[0] = math.ceil(location[0])
    location[1] = math.ceil(location[1])
    location[2] = math.ceil(location[2])
    teleport(agent_host, target[0] - 0.5, target[2], target[1] - 0.5)
    agent_host.sendCommand('pitch 0.5')
    time.sleep(1)
    agent_host.sendCommand('pitch 0')
    blocks = ["stone", "glass", "brick_block", "emerald_ore"]
    i = blocks.index(block_type) + 1
    agent_host.sendCommand('hotbar.'+str(i)+' 1')
    agent_host.sendCommand('hotbar.'+str(i)+' 0')
    agent_host.sendCommand('use 1')
    agent_host.sendCommand('jump 1')
    time.sleep(0.2)
    agent_host.sendCommand('jump 0')
    time.sleep(0.2)
    load_location(world_state, location)
    ## finish putting
    agent_host.sendCommand('jump 0')
    agent_host.sendCommand('use 0')
    time.sleep(1)
    return False


mission_file = './world/world1.xml'
with open(mission_file, 'r') as f:
    print("Loading mission from %s" % mission_file)
    mission_xml = f.read()
    my_mission = MalmoPython.MissionSpec(mission_xml, True)

max_retries = 3

print()

my_mission_record = MalmoPython.MissionRecordSpec()

for retry in range(max_retries):
    try:
        agent_host.startMission(my_mission, my_mission_record)
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:", e)
            exit(1)
        else:
            time.sleep(2.5)

print("Waiting for the mission to start", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:", error.text)
print()

# -- run the agent in the world -- #
total_cost = agent.run(agent_host)

# -- clean up -- #
time.sleep(0.5)  # (let the Mod reset)

print("Done.")

print()
print("Total Cost of Running Mission", total_cost)
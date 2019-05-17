def teleport(self, agent_host, teleport_x, teleport_y, teleport_z):
        """Directly teleport to a specific position."""
        tp_command = "tp " + str(teleport_x)+ " " + str(teleport_y) + " " + str(teleport_z)
        agent_host.sendCommand(tp_command)
        good_frame = False
        start = timer()
        while not good_frame:
            world_state = agent_host.getWorldState()
            if not world_state.is_mission_running:
                print("Mission ended prematurely - error.")
                exit(1)
            if not good_frame and world_state.number_of_video_frames_since_last_state > 0:
                frame_x = world_state.video_frames[-1].xPos
                frame_z = world_state.video_frames[-1].zPos
                if math.fabs(frame_x - teleport_x) < 0.001 and math.fabs(frame_z - teleport_z) < 0.001:
                    good_frame = True
                    end_frame = timer()
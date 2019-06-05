#!/usr/bin/env python
# coding: utf-8

# WARNING : launch naoqi in a terminal "naoqi-bin"

import sys
import qi

from qibullet import SimulationManager
from qibullet import PepperVirtual
from NaoqibulletWrapper import NaoqibulletWrapper
from takePic import *
from mouvement import *
        


def main():
        # qi App Session
        qiApp = qi.Application(sys.argv)     

        # Bullet Simulator
        simulation_manager = SimulationManager()
        client_id = simulation_manager.launchSimulation(gui=True)
        pepperSim = simulation_manager.spawnPepper(
        client_id,
        translation = [0, 0, 0],
        quaternion = [0, 0, 0, 1],
        spawn_ground_plane = True)        

        # wrap qi App Session with Simulated Pepper     
        wrap = NaoqibulletWrapper.NaoqibulletWrapper(qiApp, pepperSim) # /!\ keep wrap instance to keep thread

       
        qiSession = qiApp.session
        motionService = qiSession.service("ALMotion")  
        #add function here
        move(1,1,motionService)
        #turn(motionService,3.14)

        # block until stop is called.
        qiApp.run()

        # close nicely
        wrap.close()
 


if __name__ == '__main__':
        main()

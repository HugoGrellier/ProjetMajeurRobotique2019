#!/usr/bin/env python
# coding: utf-8

# WARNING : launch naoqi in a terminal "naoqi-bin"

import sys
import qi
import time
import pybullet
import pybullet_data
from qibullet import SimulationManager
from qibullet import PepperVirtual
from NaoqibulletWrapper import NaoqibulletWrapper
from takePic import *
from mouvement import *
from numpy import *     


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

        pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
       
        pybullet.loadURDF(
                "table.urdf",
                basePosition=[-2, 0, 0],
                globalScaling=1,
                physicsClientId=client_id) 
        
        pybullet.loadURDF(
                "totem.urdf",
                basePosition=[-1.5, 0, 1],
                globalScaling=0.7,
                physicsClientId=client_id)
        
        pybullet.loadURDF(
                "totempomme.urdf",
                basePosition=[-1.5, -0.25, 1],
                globalScaling=0.7,
                physicsClientId=client_id)

        pybullet.loadURDF(
                "totemwine.urdf",
                basePosition=[-1.5, 0.25, 1],
                globalScaling=0.7,
                physicsClientId=client_id)
        
        qiSession = qiApp.session
        motionService = qiSession.service("ALMotion")  
        #add function here
        init_cam(pepperSim)
        motionService.setAngles(["LShoulderPitch","RShoulderPitch"],[1,1],[1,1])
        #take photo
        turn(motionService,pi)
        
        take_picture(pepperSim)
        #go to the object
        move_right_obj(motionService)
        #go to the box

        move_to_Blue(motionService)

        # block until stop is called.
        qiApp.run()

        # close nicely
        wrap.close()
 


if __name__ == '__main__':
        main()

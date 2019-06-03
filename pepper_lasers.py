#!/usr/bin/env python
# coding: utf-8

import pybullet
import pybullet_data
from qibullet import PepperVirtual
from qibullet import SimulationManager

def deplacement(X,Y,Theta):
    PepperVirtual.getPosition()
    PepperVirtual.moveTo(X,Y,Theta,0)

def main():
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    pepper = simulation_manager.spawnPepper(client, spawn_ground_plane=True)

    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
       
    pybullet.loadURDF(
        "table.urdf",
        basePosition=[-2, 0, 0],
        globalScaling=1,
        physicsClientId=client) 
 
    pybullet.loadURDF(
        "totem.urdf",
        basePosition=[-1.5, 0, 1],
        globalScaling=1,
        physicsClientId=client)
  
    pybullet.loadURDF(
        "totempomme.urdf",
        basePosition=[-1.5, -0.25, 1],
        globalScaling=1,
        physicsClientId=client)

    pybullet.loadURDF(
        "totemwine.urdf",
        basePosition=[-1.5, 0.25, 1],
        globalScaling=1,
        physicsClientId=client)
    

    pepper.showLaser(True)
    pepper.subscribeLaser()
    pepper.goToPosture("Stand", 0.6)

    while True:
        laser_list = pepper.getRightLaserValue()
        laser_list.extend(pepper.getFrontLaserValue())
        laser_list.extend(pepper.getLeftLaserValue())

        if all(laser == 5.6 for laser in laser_list):
            print("Nothing detected")
        else:
            print("Detected")
            pass


     

if __name__ == "__main__":
    main()

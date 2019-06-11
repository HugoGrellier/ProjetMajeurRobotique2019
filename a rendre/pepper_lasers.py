#!/usr/bin/env python
#coding: utf-8

import pybullet
import pybullet_data
from qibullet import PepperVirtual
from qibullet import SimulationManager
import random 

def deplacement(X,Y,Theta):
    PepperVirtual.getPosition()
    PepperVirtual.moveTo(X,Y,Theta,0)

def main():
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    coord =[-2, 5, 0]
    pepper = simulation_manager.spawnPepper(client, spawn_ground_plane=False)
    pepper2 = simulation_manager.spawnPepper(client, coord, spawn_ground_plane=False)
    
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

    pybullet.loadURDF(
        "plane.urdf",
        basePosition=[0, 0, 0],
        globalScaling=1,
       physicsClientId=client)

    pybullet.loadURDF(
        "table.urdf",
        basePosition=[-2, 0, 0],
        globalScaling=1,
       physicsClientId=client)

    pybullet.loadURDF(
        "bar.urdf",
        basePosition=[0, 5, 0.5],
        baseOrientation=pybullet.getQuaternionFromEuler([1.57, 0, 0]),
        globalScaling=1,
       physicsClientId=client) 

    pybullet.loadURDF(
        "robot.urdf",
        basePosition=[-2,2,0.2],
        baseOrientation=pybullet.getQuaternionFromEuler([0, 0, 1.15]),
        globalScaling=1,
       physicsClientId=client)
 
    pybullet.loadURDF(
        "hat.urdf",
        basePosition=[-2, 5, 0],
        baseOrientation=pybullet.getQuaternionFromEuler([0, 0, 1.15]),
        globalScaling=1,
       physicsClientId=client)

    pybullet.loadURDF(
        "Cagettejaune.urdf",
        basePosition=[1, -1, 0],
        globalScaling=1,
        physicsClientId=client)

    pybullet.loadURDF(
        "Cagetterouge.urdf",
        basePosition=[2.4, -1, 0],
        globalScaling=1,
        physicsClientId=client)

    pybullet.loadURDF(
       "Cagetteverte.urdf",
        basePosition=[1.7, -1, 0],
        globalScaling=1,
        physicsClientId=client)

    pybullet.loadURDF(
       "deco.urdf",
        basePosition=[0, 6, 1.5],
        globalScaling=1,
        physicsClientId=client)

    position=[-0.25,0.0,0.25]
    i=random.choice(position) 

    pybullet.loadURDF(
     	   "totempizza.urdf",
     	   basePosition=[-1.5, i, 1.0],
     	   globalScaling=1,
      	  physicsClientId=client)
    del position[position.index(i)]

    j=random.choice(position)
    pybullet.loadURDF(
        "totembanane.urdf",
        basePosition=[-1.5, j, 1],
	baseOrientation=pybullet.getQuaternionFromEuler([0, 0, 1.57]),
        globalScaling=1,
        physicsClientId=client)
    del position[position.index(j)]

    pybullet.loadURDF(
        "totemwine.urdf",
        basePosition=[-1.5, position[0], 1],
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

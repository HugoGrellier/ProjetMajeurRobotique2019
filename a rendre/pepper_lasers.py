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
    coord =[-2, 5, 0] #coordonnés de placement du deuxieme robot
    pepper = simulation_manager.spawnPepper(client, spawn_ground_plane=False)#premier robot
    pepper2 = simulation_manager.spawnPepper(client, coord, spawn_ground_plane=False)#deuxieme robot
    
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

#changement du sol, mis en plus du parquet 
    pybullet.loadURDF(
        "plane.urdf",
        basePosition=[0, 0, 0],
        globalScaling=1,
       physicsClientId=client)

    pybullet.loadURDF(
        "table.urdf",
        basePosition=[-2, 0, 0],#coordonnés de placement de l'objet:(x,y,z)
        globalScaling=1,
       physicsClientId=client)

    pybullet.loadURDF(
        "bar.urdf",
        basePosition=[0, 5, 0.5],
        baseOrientation=pybullet.getQuaternionFromEuler([1.57, 0, 0]),#rotation de 90° du bar selon l'axe x
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
        basePosition=[2.4, -1, 0],#cagette rouge placée derriere la cagette verte
        globalScaling=1,
        physicsClientId=client)

    pybullet.loadURDF(
       "Cagetteverte.urdf",
        basePosition=[1.7, -1, 0],#cagette verte placée derriere la cagette jaune
        globalScaling=1,
        physicsClientId=client)

    pybullet.loadURDF(
       "deco.urdf",
        basePosition=[0, 6, 1.5],
        globalScaling=1,
        physicsClientId=client)

    position=[-0.25,0.0,0.25]# trois positions possibles des objets
    i=random.choice(position)#choix aléatoire des coordonnés selon y 

    pybullet.loadURDF(
     	   "totempizza.urdf",
     	   basePosition=[-1.5, i, 1.0],#position de l'objet avec coordonné selon y aléatoire
     	   globalScaling=1,
      	  physicsClientId=client)
    del position[position.index(i)]#suppression de la liste du coordonné de cet objet

    j=random.choice(position)
    pybullet.loadURDF(
        "totembanane.urdf",
        basePosition=[-1.5, j, 1],#position de l'objet avec coordonné selon y aléatoire
	baseOrientation=pybullet.getQuaternionFromEuler([0, 0, 1.57]),
        globalScaling=1,
        physicsClientId=client)
    del position[position.index(j)]#suppression de la liste du coordonné de cet objet

    pybullet.loadURDF(
        "totemwine.urdf",
        basePosition=[-1.5, position[0], 1],#position de l'objet avec la dernier coordonnée selon y possible
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

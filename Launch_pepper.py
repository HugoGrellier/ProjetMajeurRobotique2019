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
from pepper_AlMemory import almemory,initalmemory

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

        obj_creation(client_id)
        #memProxy=initalmemory()
        #[choiceObj,choiceBasket,choiceFinish]=almemory(memProxy)
        #while choiceFinish==0:
        #        [choiceObj,choiceBasket,choiceFinish]=almemory(memProxy)
        #print( [choiceObj,choiceBasket,choiceFinish])
        choiceObj="banane"
        choiceBasket="jaune"
        qiSession = qiApp.session
        motionService = qiSession.service("ALMotion")  
        

        init_cam(pepperSim)
        motionService.setAngles(["LShoulderPitch","RShoulderPitch"],[1,1],[1,1])
        #take photo
        turn(motionService,pi)
        move(0.6,0,motionService,False)
        motionService.setAngles(["HipPitch"],[-0.10],[1])
        motionService.setAngles(["HeadPitch", "HeadYaw"], [0.35,0], [1,1]) 
        time.sleep(2)
        result=take_picture(pepperSim)
        motionService.setAngles(["HeadPitch", "HeadYaw"], [0,0], [1,1]) 
        if choiceObj=='banane':
                choiceObj='banana'
        elif choiceObj=='vin':
                choiceObj='bottle'
        else:
                choiceObj='pizza'

        #go to the object
        if choiceObj==result[0][1]:
                move_left_obj(motionService)
        elif choiceObj==result[1][1]:
                move_middle_obj(motionService)
        else:
                move_right_obj(motionService)
        
        
        #go to the box
        if choiceBasket=='rouge':        
                move_to_Red(motionService)
        elif choiceBasket=='vert':        
                move_to_Green(motionService)
        else:       
                move_to_Yellow(motionService)


        # block until stop is called.
        qiApp.run()

        # close nicely
        wrap.close()
 
def obj_creation(client):
        pybullet.loadURDF(
                "plane.urdf",
                basePosition=[0, 0, 0],
                globalScaling=1,
        physicsClientId=client)
        
        pybullet.loadURDF(
                "table.urdf",
                basePosition=[-2, 0, 0],
                #baseOrientation=pybullet.getQuaternionFromEuler([1.57, 0, 0]),
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
                "totem.urdf",
                basePosition=[-1.5, i, 1.0],
                globalScaling=0.7,
                physicsClientId=client)
        del position[position.index(i)]
        
        j=random.choice(position)
        pybullet.loadURDF(
                "totempomme.urdf",
                basePosition=[-1.5, j, 1],
                globalScaling=0.7,
                baseOrientation=pybullet.getQuaternionFromEuler([0, 0, 2]),
                physicsClientId=client)
        del position[position.index(j)]


        pybullet.loadURDF(
                "totemwine.urdf",
                basePosition=[-1.5, position[0], 1],
                globalScaling=0.7,
                physicsClientId=client)

if __name__ == '__main__':
        main()

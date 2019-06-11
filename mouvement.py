#!/usr/bin/env python
# coding: utf-8
from numpy import *
import time

def turn(motionService,Angle):
    motionService.moveTo(0,0,Angle)

def move(X,Y,motionService,resetAngle):
    if X<0 and Y<0:
        Angle=float(-pi+arctan(Y/X))
    elif  X<0 and Y>=0:
        Angle=float(pi+arctan(Y/X))
    elif  X>0 and Y<0: 
        Angle=float(arctan(Y/X))
    elif  X>0 and Y>=0:
        Angle=float(arctan(Y/X))

    elif X==0 and Y>0:
        Angle=float(-pi/2)
    elif X==0 and Y<=0:
        Angle=float(pi/2)

    turn(motionService,Angle)
    Z=float(sqrt(X*X+Y*Y))
    motionService.moveTo(Z,0,0)
    if resetAngle==True:
        turn(motionService,-Angle)

def Grab_obj(motionService):
    

    motionService.setAngles(['LElbowYaw',"HipPitch","LWristYaw"], [0,-0.6,-1.5], [1,1,1])
    time.sleep(2)
    motionService.setAngles(["LShoulderPitch"],[-0.05],[0.1])
    motionService.moveTo(-0.01,-0.14,0)
    motionService.moveTo(0.02,0,0)
    motionService.setAngles(["LHand"],[-3],[0.15])
    time.sleep(1)
    motionService.setAngles(["LShoulderPitch", "LShoulderRoll",'LElbowYaw',"HipPitch","LWristYaw"], [0,0,0,-0.0,-0], [1,1,1,1,1])
    


def move_middle_obj(motionService):
    motionService.setAngles(["LShoulderPitch", "LShoulderRoll","LHand"], [0.02,0,4], [1,1,1])
    move(0.41,0,motionService,True)
    Grab_obj(motionService)
    move(-1,0.15,motionService,True)

def move_right_obj(motionService):
    motionService.setAngles(["LShoulderPitch", "LShoulderRoll","LHand"], [0.02,0,4], [1,1,1])
    move(0,0.27,motionService,True)
    move(0.41,0,motionService,False)
    Grab_obj(motionService)
    move(-1.01,0.42,motionService,True)

def move_left_obj(motionService):
    motionService.setAngles(["LShoulderPitch", "LShoulderRoll","LHand"], [0.02,0,4], [1,1,1])
    move(0,-0.25,motionService,True)
    move(0.41,0,motionService,False)
    Grab_obj(motionService)
    move(-1.02,-0.4,motionService,True)

def move_to_Yellow(motionService):
    move(-1,0.6,motionService,True)
    turn(motionService,pi/2)
    motionService.setAngles(["LHand"],[3],[0.5])
    time.sleep(2)
    motionService.setAngles(["LShoulderPitch","RShoulderPitch"],[1,1],[1,1])
    motionService.setAngles(["LHand"],[-3],[0.5])
    move(-1,1,motionService,True)

def move_to_Red(motionService):
    move(-2.4,0.6,motionService,True)
    turn(motionService,pi/2)
    motionService.setAngles(["LHand"],[3],[0.5])
    time.sleep(2)
    motionService.setAngles(["LShoulderPitch","RShoulderPitch"],[1,1],[1,1])
    motionService.setAngles(["LHand"],[-3],[0.5])
    move(-1.5,1.5,motionService,False)
    
def move_to_Green(motionService):
    move(-1.7,0.6,motionService,True)
    turn(motionService,pi/2)
    motionService.setAngles(["LHand"],[3],[0.5])
    time.sleep(2)
    motionService.setAngles(["LShoulderPitch","RShoulderPitch"],[1,1],[1,1])
    motionService.setAngles(["LHand"],[-3],[0.5])
    move(-1.7,1,motionService,False)

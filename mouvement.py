#!/usr/bin/env python
# coding: utf-8
from numpy import *

def turn(motionService,Angle):
    #Angle=Angle_deg/360*2*pi # Radian
    motionService.moveTo(0,0,Angle)

def move(X,Y,motionService):
    Angle=float(arctan(Y/X))
    
    turn(motionService,Angle)
    Z=float(sqrt(X*X+Y*Y))
    
    motionService.moveTo(Z,0,0)
    turn(motionService,-Angle)

#!/usr/bin/env python
#coding: utf-8

import pybullet
import pybullet_data
from qibullet import PepperVirtual
from qibullet import SimulationManager
from random import*
from naoqi import ALProxy


def initalmemory():
    # create proxy on ALMemory
    memProxy = ALProxy("ALMemory","localhost",9559)
    return memProxy
def almemory(memProxy):
	
	#get data. Val can be int, float, list, string
    val1 = memProxy.getData("my_object")
    val2 = memProxy.getData("my_basket") 

    val3 = memProxy.getData("my_choice") 
    return [val1,val2,val3]

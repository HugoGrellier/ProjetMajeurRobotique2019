#!/usr/bin/env python
# coding: utf-8

import cv2
import time
from qibullet import SimulationManager
from qibullet import PepperVirtual
from qibullet import camera
import detect

image_name='image.png' 

def init_cam(pepper):
    pepper.subscribeCamera(PepperVirtual.ID_CAMERA_TOP,resolution=camera.CameraResolution(1080,1080))
    return True

def take_picture(pepper):
    img = pepper.getCameraFrame() #capture camera frame
    print('photo taken') #debug
    cv2.imwrite(image_name,img) #write the image in the current directory
    score=0.09
    resultSorted=[]

    result=detect.Algo_detect(image_name,score)#COCO 
    resultSorted=detect.sort(result)
    pepper.unsubscribeCamera(PepperVirtual.ID_CAMERA_TOP)
    return resultSorted
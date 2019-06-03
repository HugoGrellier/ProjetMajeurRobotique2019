#!/usr/bin/env python
# coding: utf-8

import cv2
import time
from qibullet import SimulationManager
from qibullet import PepperVirtual
from pynput.keyboard import Key, Listener


#global
flag_pic=0
totem_x=[1,2,3]
totem1=0
totem2=0
totem3=0

def main():
    image_name='image.png'
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    pepper = simulation_manager.spawnPepper(client, spawn_ground_plane=True) 
    pepper.subscribeCamera(PepperVirtual.ID_CAMERA_BOTTOM)
    #pepper.goToPosture("Crouch", 0.6)
    #time.sleep(1)
    pepper.goToPosture("Stand", 0.6)
    time.sleep(1)
    #pepper.goToPosture("StandZero", 0.6)
    #time.sleep(1)
    flag_pic=0
    while True:
        img = pepper.getCameraFrame()
        cv2.imshow("bottom camera", img)
        cv2.waitKey(1)
	flag_pic=flag_pic+1
	if flag_pic==10:
	    print('photo taken')
	    flag_pic=0
	    cv2.imwrite(image_name,img)
	    result=Algo_detect(image_name)
	    
   

def Algo_detect(photo_name):
	import Algorithmia
	from Algorithmia.acl import ReadAcl, AclType
	apiKey = "simUb6EKrYK8xAnJp1gUqqhzTQm1"
	# Create the Algorithmia client
	client = Algorithmia.client(apiKey)

	# Set your Data URI
	nlp_directory = client.dir("data://patate2cherie/nlp_directory")
	# Create your data collection if it does not exist
	if nlp_directory.exists() is False:
	    nlp_directory.create()

	# Create the acl object and check if it's the .my_algos default setting
	acl = nlp_directory.get_permissions()  # Acl object
	acl.read_acl == AclType.my_algos  # True

	# Update permissions to private
	nlp_directory.update_permissions(ReadAcl.private)
	nlp_directory.get_permissions().read_acl == AclType.private # True

	img_file = "data://patate2cherie/nlp_directory/"+photo_name

	# Upload local file
	if client.file(img_file).exists() is False:
	    client.file(img_file).putFile(photo_name)

	# Download contents of file as a string
	if client.file(img_file).exists() is True:
	    input = {
	  "image":img_file,
	  "output":"data://.algo/deeplearning/ObjectDetectionCOCO/temp/"+photo_name,
	  "min_score":0.5,
	  "model":"ssd_mobilenet_v1"
	}
	# Create the algorithm object using the Summarizer algorithm
	algo = client.algo("deeplearning/ObjectDetectionCOCO/0.2.1")
	#algo.set_option(timeout=300)
	# Pass in input required by algorithm
	try:
	    # Get the summary result of your file's contents
	    result=algo.pipe(input).result
	    print(result)
	except Exception as error:
	    # Algorithm error if, for example, the input is not correctly formatted
	    result=0
	    print(error)   
   	return result
  

if __name__ == "__main__":
    main()
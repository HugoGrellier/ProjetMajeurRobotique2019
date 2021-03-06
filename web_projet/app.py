#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


import qi
import argparse
import sys
import time
import signal
from naoqi import ALProxy

def main(session):
    # Get the service ALTabletService.

    try:
        tabletService = session.service("ALTabletService")
        tabletService.loadApplication("web_projet")
        tabletService.showWebview()

    except Exception, e:
        print "Error was: ", e



    try:
  # create proxy on ALMemory
        memProxy = ALProxy("ALMemory","localhost",9559)

  #insertData. Value can be int, float, list, string
        memProxy.insertData("my_object", "pizza")
	memProxy.insertData("my_basket", "bleue")
	memProxy.insertData("my_choice", "0")
	

  #getData
        print "The value of myValueName1 is", memProxy.getData("my_object")

    except RuntimeError,e:
  # catch exception
        print "error insert data", e



# Getting the service ALDialog
    try:
    	ALDialog = session.service("ALDialog")
        ALDialog.resetAll()
    	ALDialog.setLanguage("English")




    	# Loading the topics directly as text strings
    	#topic_name = ALDialog.loadTopic("/home/nao/.local/share/PackageManager/apps/SimpleWebPython/simple_en.top")
	#WARNING TO CHANGE YOUR PATH  
	topic_name = ALDialog.loadTopic("/home/tp/softbankRobotics/apps/web_projet/simpled_en.top")

    	# Activating the loaded topics
    	ALDialog.activateTopic(topic_name)


    	# Starting the dialog engine - we need to type an arbitrary string as the identifier
    	# We subscribe only ONCE, regardless of the number of topics we have activated
    	ALDialog.subscribe('simpled')

    except Exception, e:
        print "Error was: ", e

    try:
        raw_input("\n Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('simpled')

        # Deactivating the topic
        ALDialog.deactivateTopic(topic_name)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload our topic and free the associated memory
        ALDialog.unloadTopic(topic_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)

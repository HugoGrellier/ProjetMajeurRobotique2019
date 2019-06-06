#!/usr/bin/env python
# coding: utf-8

import Algorithmia
from Algorithmia.acl import ReadAcl, AclType

def Algo_detect(photo_name,score):
	
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
	#if client.file(img_file).exists() is False:
	client.file(img_file).putFile(photo_name)

	# Download contents of file as a string
	if client.file(img_file).exists() is True:
	    input = {
	  "image":img_file,
	  "output":"data://.algo/deeplearning/ObjectDetectionCOCO/temp/"+photo_name,
	  "min_score":score,
	  "model":"ssd_mobilenet_v1"
	}
	# Create the algorithm object using the COCO algorithm
	algo = client.algo("deeplearning/ObjectDetectionCOCO/0.2.1")
	#algo.set_option(timeout=300)
	# Pass in input required by algorithm
	try:
	    # Get the result of your file's contents
	    result=algo.pipe(input).result
	    print(result)
	except Exception as error:
	    # Algorithm error if, for example, the input is not correctly formatted
	    result=0
	    print(error)   
   	return result

Algo_detect("image.png",0.5)
# mowmowinc
GUI for data collection

Camera.py
	- Class to connect to webcams
	- Construct Camera(NUM), 	NUM = 0 -> for laptops camera
							NUM = val >= 1 for other USB cameras

mainGui.py
	- Class that has all GUI related stuff, no logic inside

videoSlicer.py
	- Script to read video src from commandline and splices and saves each frame to a folder
	- Output is folder "Resources/Images" inside the folder the images will have the format "image#.png"
	- How to run this script: "python videoSlicer.py PATH-TO-VIDEO/videoName.EXTENSION"

dataCollection.py
	- Class that contains all the logic. main script to run the GUI
	- Variables slices can be manipulated to increase the number of buttons generated. number in slices must be able to get a square root
	- You want to run this script if you already have a video and want to just read the frames and label (Camera.py or cameras needed for this)
	- Before running this you must run videoSlicer.py first

dataCollectionLive.py
	- Class that contains all the logic. main script to run the GUI
	- Variables slices can be manipulated to increase the number of buttons generated. number in slices must be able to get a square root
	- You want to run this script if you want to label as it takes pictures

Any questions please contact me
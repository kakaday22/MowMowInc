# mowmowinc
GUI for data collection

Main usage is open the dataCollection.py (follow instructions below) and press next, label the grass whether is "mowed" "unmowed" "irrelevant" by changing the comboBox (top-left area of the screen) then pressing the corresponding picture and it will save on a csv file for later be used on the Neural Network.

GUI works well with touch screen computers :D

Camera.py
	<br>- Class to connect to webcams
	<br>- Construct Camera(NUM), 	NUM = 0 -> for laptops camera. NUM = val >= 1 for other USB cameras

mainGui.py
	<br>- Class that has all GUI related stuff, no logic inside

videoSlicer.py
	<br>- Script to read video src from commandline and splices and saves each frame to a folder
	<br>- Output is folder "Resources/Images" inside the folder the images will have the format "image#.png"
	<br>- How to run this script: "python videoSlicer.py PATH-TO-VIDEO/videoName.EXTENSION"

dataCollection.py
	<br>- Class that contains all the logic. main script to run the GUI
	<br>- Variables slices can be manipulated to increase the number of buttons generated. number in slices must be able to get a square root
	<br>- You want to run this script if you already have a video and want to just read the frames and label (Camera.py or cameras needed for this)
	<br>- Before running this you must run videoSlicer.py first

dataCollectionLive.py
	<br>- Class that contains all the logic. main script to run the GUI
	<br>- Variables slices can be manipulated to increase the number of buttons generated. number in slices must be able to get a square root
	<br>- You want to run this script if you want to label as it takes pictures

initialVal
	<br>- File that contains the last picture used on GUI
	<br>- Be careful when using this

Any questions please contact me

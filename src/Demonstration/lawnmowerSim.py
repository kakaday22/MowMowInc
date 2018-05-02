from transitions import Machine, State
from picamera import PiCamera
from math import sqrt
import sys
import os
import frameOverlayer as fol
import numpy as np
from pathlib import Path
from CNNsftp import CNNsftp
from easterEgg import easterEgg
import time

try:
	import RPi.GPIO as GPIO
except:
	print("No RPi available\n")

butPin = 13


"""
LawnMower is a class that will host a Finite State Machine (FSM) to determine whether a
particular image is either mowed vs unmowed.

Its output is an image overlay of 100 sections with a label categorizing its status

The class is organized in the following way:
	1) Local variables
	2) Initializer
	3) Local functions
"""
class LawnMower():
	# Local Variables
	delay = 10
	res = (4000, 3000)
	slices = 100
	printFlag = 0
	liveDemo = int(sys.argv[1])
	#list of All States used to initialize the machine!
	states = [
			State(name = 'Limbo', on_enter=[], on_exit=[]),
			State(name = 'CollectData', on_enter=[], on_exit=[]),
			State(name = 'NeuralNetProcess', on_enter=[], on_exit=[]),
			State(name = 'Unknown', on_enter=[], on_exit=[]),
			State(name = 'Irrelevant', on_enter=[], on_exit=[]),
			State(name = 'Mowed', on_enter=[], on_exit=[]),
			State(name = 'Unmowed', on_enter=[], on_exit=[]),
			State(name = 'Execute', on_enter=[], on_exit=[])
		]
	#list of all the transitions used to link each state together!
	transitions =[	#triggerKeyword,		sourceState(s), 	destinationState
				{'trigger':'go2Limbo','source':['Execute', 'NeuralNetProcess'],'dest':'Limbo'},
				{'trigger':'go2NeuralNet','source':['CollectData', 'Execute'],'dest':'NeuralNetProcess'},
				{'trigger':'go2Unknown','source':'NeuralNetProcess','dest':'Unknown'},
				{'trigger':'go2Irrelevant','source':'NeuralNetProcess','dest':'Irrelevant'},
				{'trigger':'go2Mowed','source':'NeuralNetProcess','dest':'Mowed'},
				{'trigger':'go2Unmowed','source':'NeuralNetProcess','dest':'Unmowed'},
				{'trigger':'go2Execute','source':['Irrelevant', 'Unmowed', 'Mowed', 'Unknown'],'dest':'Execute'},
				{'trigger':'go2Collection','source':'Limbo','dest':'CollectData'}
			]

	"""
	Constructors of the class
	@param name: name of the machine
	@param initState: the initial state of the state machine
	"""
	def __init__(self, name=".::.BATMAN.::.", initState="Limbo"):
		self.paths = ""
		self.name = name
		self.machine = Machine(model=self, states=LawnMower.states, transitions=LawnMower.transitions, initial=initState, ignore_invalid_triggers=True)
		self.counter = 0
		self.overlay = fol.frameOverlayer("")
		self.nnFlag = 0
		self.x = 1
		self.y = 1
		self.coin = easterEgg()
		#self.camera = PiCamera() # Uncomment if using Pi camera
		#self.camera.resolution = (1024, 768) #uncomment if using Pi Camera
		self.sftp = CNNsftp(TARGET_IP, TARGET_USERNAME, TARGET_PASSWORD)
		#self.camera.start_preview()

	def __del__(self):
		print("Gracefully closing camera")
		self.camera.close()

	"""
	dictionary function that returns which trigger to perform depending on the key
	@param key: the key to determinate which trigger to return
	@return the trigger function to activate
	"""
	def triggerState(self, key):
		return 	{	1 : self.go2Mowed,
				2 : self.go2Unmowed,
				3 : self.go2Irrelevant,
				4 : self.go2Unknown
			}[key]

	"""
	Dummy state that does nothing until pushbutton is pressed. This way it prevents the FSM to continue without been told
	"""
	def LimboState(self):
		if not LawnMower.printFlag:
			LawnMower.printFlag = 1
			print("Limbo State")

	"""
	State in which picture is taken or an image in the folder is provided (depending on the liveDemo flag)
	"""
	def CollectDataState(self):
		print("CollectData State")
		imgName = "mowmow%0.2d" %(self.counter)
		if LawnMower.liveDemo:
			os.system("python3 fetchImage.py %d" %(self.counter)) #This uses the GoPro camera
			#self.camera.capture("Images/%s.jpg" %(imgName)) # Run on PiCamera
		else:
			self.paths = "mixed/"
			LawnMower.res = (1920, 1080)
		self.overlay.setImage("Images/%s%s.jpg" %(self.paths, imgName))
		self.go2NeuralNet()

	"""
	State that sends image to Neural Network via SSH and waits until a text file is returned via SSH
	"""
	def NeuralNetProcessState(self):
		print("NeuralNetProcess State")
		try:
			if not self.nnFlag:
				imgName = "mowmow%0.2d" %(self.counter)
				self.sftp.send("Images/%s%s.jpg" %(self.paths,imgName),"/home/darthkrenth/PythonWorkspace/mowmowCNN/PredictQueue/%s.jpg" %(imgName))
				print("Image sent to Anchorage, AK, waiting for instructions...")
				self.pre = Path("Output/prediction%0.2d.txt" %(self.counter))
				while not self.pre.is_file(): #waiting until predictios have been capture
					self.coin.flip()
				self.coin.destroy()
				time.sleep(1)
				print("Intel received... Processing")
				self.pre = self.getPredictions(str(self.pre))
				print(self.pre)
				self.nnFlag = 1
			self.triggerState(self.pre[self.x-1][self.y-1])()
		except OSError as err:
			self.overlay.setImage("Images/default.jpg")
			self.overlay.display(5)
			LawnMower.printFlag = 0
			self.go2Limbo()
			sys.exit(0)

	"""
	States that gathers the parameters of what to do when Unknown images is determine 
	"""
	def UnknownState(self):
		print("Unknown State")
		self.overlay.overlayRectangle(4, LawnMower.res, int(sqrt(LawnMower.slices)), (self.x, self.y))
		self.go2Execute()

	"""
	States that gathers the parameters of what to do when Irrelevant images is determine 
	"""
	def IrrelevantState(self):
		print("Irrelevant State")
		self.overlay.overlayRectangle(3, LawnMower.res, int(sqrt(LawnMower.slices)), (self.x, self.y))
		self.go2Execute()

	"""
	States that gathers the parameters of what to do when Mowed images is determine 
	"""
	def MowedState(self):
		print("Mowed State")
		self.overlay.overlayRectangle(1, LawnMower.res, int(sqrt(LawnMower.slices)), (self.x, self.y))
		self.go2Execute()

	"""
	States that gathers the parameters of what to do when Unmowed images is determine 
	"""
	def UnmowedState(self):
		print("Unmowed State")
		self.overlay.overlayRectangle(2, LawnMower.res, int(sqrt(LawnMower.slices)), (self.x, self.y))
		self.go2Execute()

	"""
	State executes the parameters gathered by the previous state (Mowed, Unmowed, Irrelevant, Unknown)
	"""
	def ExecuteState(self):
		print("Execute State")
		val = int(sqrt(LawnMower.slices))
		if self.y != val or self.x != val:
			self.x += 1*(self.y == val)
			self.y = self.y*(self.y != val) + 1
			self.go2NeuralNet()
		else:
			LawnMower.printFlag = 0
			self.overlay.display(LawnMower.delay)
			self.x = 1
			self.y = 1
			self.counter += 1
			self.nnFlag = 0
			print("DONE\n\n\n")
			os.system("rm -r Output/*")
			self.go2Limbo()

	# hardware interrupt that detects if button has been pressed or not!
	def ButtonPressed(self, dummy):
		if self.state == "Limbo":
			self.go2Collection()

	# takes the path where the predictions are and converts it into an array
	def getPredictions(self, path):
		print(path)
		arr = []
		with open(path, "r") as myFile:
			reader = myFile.readlines()
			for val in reader:
				arr.append(int(val))
		return np.array([arr]).reshape(int(sqrt(LawnMower.slices)), int(sqrt(LawnMower.slices)))


def setupPi(robot):
	global butPin
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(butPin, GPIO.RISING, callback=robot.ButtonPressed, bouncetime=500)

def switchState(key):
	return {	"Limbo" : robot.LimboState,
			"CollectData" : robot.CollectDataState,
			"NeuralNetProcess" : robot.NeuralNetProcessState,
			"Unknown" : robot.UnknownState,
			"Irrelevant" : robot.IrrelevantState,
			"Mowed" : robot.MowedState,
			"Unmowed" : robot.UnmowedState,
			"Execute" : robot.ExecuteState,
		}[key]

if __name__ == "__main__":
	direc = os.path.dirname("Images/")
	if not os.path.exists(direc):
		os.makedirs(direc)
	direc = os.path.dirname("Output/")
	if not os.path.exists(direc):
		os.makedirs(direc)
	robot = LawnMower()
	setupPi(robot)

	while(1):
		switchState(robot.state)()

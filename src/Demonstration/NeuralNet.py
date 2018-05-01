from mowmowCNNPredictor import mowmowCNNPredictor as CNN
from pathlib import Path
import os
import sys
import image_slicer as slicer
from CNNsftp import CNNsftp
import time
import cv2 as cv
import numpy as np

counter = 0
myCNN = CNN("saved/bed/8333")
sftp = CNNsftp(TARGET_IP, TARGET_USERNAME, TARGET_PASSWORD)

while True:
	
	# <<< WAIT FOR THE FRAME >>>
	framefile = Path("PredictQueue/mowmow%0.2d.jpg" %(counter))
	print("Waiting for frame...")
	while not framefile.is_file():
		pass
	time.sleep(2)
	print("Got frame.")
	print("Resizing...")
	imgpre = cv.imread("PredictQueue/mowmow%0.2d.jpg" %(counter))
	imgpre = cv.resize(imgpre, (1920,1080), interpolation = cv.INTER_CUBIC)
	cv.imwrite("PredictQueue/mowmow%0.2d.jpg" %(counter), imgpre)
	print("Resized.")
	
	# <<< CALL A MAN'S SLICER WITH THIS FRAME FILE >>>
	try:
		print("Slicing...")
		tiles = slicer.slice("PredictQueue/mowmow%0.2d.jpg" %(counter), 100, False)
		tilepath = os.path.dirname("PredictQueue/Slices/")
		if not os.path.exists(tilepath):
			os.makedirs(tilepath)
		slicer.save_tiles(tiles, prefix="slice", directory = tilepath)
		print("Sliced.")
	except Exception as err:
		print(err)
		sys.exit(1)

	# <<< SET UP NEURAL NETWORK CALL LOOP >>>
	print("Running through CNN...")
	# with open("PredictQueue/Predictions/prediction%0.2d.txt" %(counter), "wb") as writer:
	# 	for i in range(1,11):
	# 		for j in range(1,11):

	# <<< PREDICT... >>>
	prediction = myCNN.predict_type("PredictQueue/Book/slicebook.csv")
	
	np.savetxt("PredictQueue/Predictions/probs%0.2d.txt" %(counter), zip(prediction[:,0],prediction[:,1],prediction[:,2]), fmt=("%i"))

	predicted = np.empty([100])
	# <<< ...AND WRITE TO "prediction%0.2d.txt" IN NEW LINES >>>
	for i in range(0,100):
		predicted[i] = np.argmax(prediction[i,:]>0)+1

	#print(predicted[:,0])
	np.savetxt("PredictQueue/Predictions/prediction%0.2d.txt" %(counter), zip(predicted), fmt=("%i"))
	
	# writer.write("%d\n" %(predicted))
	print("All predictions made.")

	# <<< REMOVE SLICES >>>
	print("Removing slices...")
	os.system("rm -r PredictQueue/Slices/*.png")
	print("Slices removed.")

	# <<< PUSH PREDICTIONS TO PI >>>
	print("Pushing predictions to PI...")
	sftp.send("PredictQueue/Predictions/prediction%0.2d.txt" %(counter),
			  "/home/pi/Desktop/MowMow/Output/prediction%0.2d.txt" %(counter))
	print("Predictions pushed.")
	print("----------------------------------")
	# <<< "GRACEFULLY" INCREASE COUNTER >>>
	counter += 1

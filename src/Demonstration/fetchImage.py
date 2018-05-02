from goprocam import GoProCamera
from goprocam import constants
import cv2
import sys


cam = GoProCamera.GoPro() # initializes gopro camera
#cam.mode("photo")
cam.downloadLastMedia(cam.take_photo(2), "Images/mowmow%0.2d.jpg" %(int(sys.argv[1]))) #saves the image specified directory with specified name

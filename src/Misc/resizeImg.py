from PIL import Image
from resizeimage import resizeimage
import glob, os

i = 0;
newSize = [640, 480] # this is the new size of the image
os.chdir("Resources/Images")
for file in glob.glob("*.jpg"): #for ever file with JPG extension
	img = Image.open(file) # open the image
	img = resizeimage.resize_cover(img, newSize) # resize image with new Size
	img.save(file, img.format) # save image with the same name and format
print("done")
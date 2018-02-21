from PIL import Image
from resizeimage import resizeimage
import glob, os

i = 0;
os.chdir("Resources/Images")
for file in glob.glob("*.jpg"):
	img = Image.open(file)
	img = resizeimage.resize_cover(img, [640, 480])
	img.save(file, img.format)
print("done")
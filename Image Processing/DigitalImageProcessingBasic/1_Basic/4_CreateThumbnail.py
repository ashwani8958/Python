import os,sys
from PIL import Image

# https://pillow.readthedocs.io/en/latest/handbook/tutorial.html#using-the-image-class

# List of the images
images = []
thumbnailSize = (128,128)

os.chdir("./images")

# Make lists contains all the file name in the current working folder
for root, dirs, files in os.walk("."):
   for name in files:
       images.append(name)

# open the images contains in list "images"
for image in images[:2]:
    outfile = os.path.splitext(image)[0] + ".thumbnail"
    if image != outfile:
        try:
            with Image.open(image) as im:
                im.thumbnail(thumbnailSize)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)

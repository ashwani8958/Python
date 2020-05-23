import os, sys
from PIL import Image

# https://pillow.readthedocs.io/en/latest/handbook/tutorial.html#using-the-image-class

os.chdir("./images")
images = []

# Make lists contains all the file name in the current working folder
for root, dirs, files in os.walk("."):
   for name in files:
       images.append(name)

for infile in images:
    f, e = os.path.splitext(infile) # f, e will be the name(f) and extension(e) of each file
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)

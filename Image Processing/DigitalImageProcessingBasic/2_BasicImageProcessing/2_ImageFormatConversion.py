from PIL import Image
import os

filelist=['../images/profile.jpg','../images/moon.jpg']


for infile  in filelist:
    # os.path.splitext(infile)
    # Split the pathname path into(Tuple) a pair (root, ext) such that root + ext == path,
    # and ext is empty or begins with a period and contains at most one period.
    # Leading periods on the basename are ignored; splitext('.cshrc') returns ('.cshrc', '').
    outfile = os.path.splitext(infile)[0]+".png"
    if infile !=outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
                print("Cannot convert"), infile

import os,sys

# Change directory by giving the full path
os.chdir("../")

for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

# The method walk() generates the file names in a directory
# tree by walking the tree either top-down or bottom-up.
#
# os.walk(top[, topdown = True[, onerror = None[, followlinks = False]]])
#
# Parameters
# 1. top − Each directory rooted at directory, yields 3-tuples, i.e., (dirpath, dirnames, filenames)
#
# 2. topdown − If optional argument topdown is True or not specified, directories are scanned from top-down. If topdown is set to False, directories are scanned from bottom-up.
#
# 3. onerror − This can show error to continue with the walk, or raise the exception to abort the walk.
#
# 4. followlinks − This visits directories pointed to by symlinks, if set to true.

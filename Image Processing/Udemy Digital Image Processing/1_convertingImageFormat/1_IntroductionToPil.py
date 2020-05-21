from PIL import Image

img  = Image.open('../images/profile.jpg')
#img.show()
new_img = Image.open('../images/profile.jpg').convert('L')
new_img.show();

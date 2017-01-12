from PIL import Image
import time

#Open an image to use
im = Image.open(r'C:\training\new_logo.jpg')

#Save the image
im_flipped.save(r'c:\training\temp.jpg')

#Rotate an image by an angle
im_rot = im.rotate(180)

#Copy an image
im_rot = im.copy()

#Crop an image
im = im.crop((0,0,128,128))


#Flip an image
im_flipped = im.transpose(Image.FLIP_LEFT_RIGHT)
im_flipped = im.transpose(Image.FLIP_TOP_BOTTOM)

#Create a thumbnail (resize)
im_thumb = im.thumbnail((128,128))

#split the image into bands based on mode (CMYK or RGB)
c, m, y, k = im.split()

#Remerge
im_merged = Image.merge('CMYK', (m, k, m, c))

#Show (Only in OS with a GUI)
im.show()
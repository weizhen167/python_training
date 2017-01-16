from PIL import Image

#Open an image to use
img = Image.open('new_logo.jpg')

#Save the image
img.save('modified_image.jpg')



#Rotate an image by an angle
img_rot = img.rotate(332)


#Copy an image
impage_2 = img.copy()

#Crop an image
im_crop = img.crop((0,0,128,128))


#Flip an image



img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipped_2 = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipped_3 = img.transpose(Image.ROTATE_90)

#Create a thumbnail (resize)
img_thumb= img.thumbnail((128,128))
img.save('thumbnail.jpg')


#Split the image into bands based on mode (CMYK or RGB)
c,m,y,k = img.split()

print c, m
#Remerge

im_merged = Image.merge('CMYK', (y, k, m, c))

im_merged.show()
#Show (Only in OS with a GUI)



#img.show()
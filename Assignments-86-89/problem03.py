from PIL import Image, ImageOps


# Open Image
myImage = Image.open("E:\Programme_Cours\course_2023\Mastering-Python\Assignments-86-89\elzero-pillow.png")


# Crop Image
box = (400, 0, 800, 400)

cutImg = myImage.crop(box)

grayImg = ImageOps.grayscale(cutImg)

# Save Image
grayImg.save("E:\Programme_Cours\course_2023\Mastering-Python\Assignments-86-89\cropImg-L.png")
# Show Image
grayImg.show()

box = (0, 400, 1200, 800)

cutImg = myImage.crop(box)
cutImg = cutImg.rotate(180)
grayImg = ImageOps.grayscale(cutImg)

# Save Image
grayImg.save("E:\Programme_Cours\course_2023\Mastering-Python\Assignments-86-89\cropImg2.png")
# Show Image
grayImg.show()
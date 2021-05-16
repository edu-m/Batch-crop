from PIL import Image

box = (165, 96, 856, 615)

im = Image.open("1.jpg") # just open the first image
region = im.crop(box)
region.save("A.png")


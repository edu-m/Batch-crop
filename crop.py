from PIL import Image

# abox = (361, 210, 1863, 1338)
bbox = (165, 96, 856, 615)
cbox = (136, 1, 1000, 554)
count = 1
while count < 72:
    c = "% s" % count
    im = Image.open(str(c) + ".png")
    region = im.crop(cbox)
    region.save(str(c) + "A.png")
    count = count + 1

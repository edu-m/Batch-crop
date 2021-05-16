from PIL import Image

abox = (361, 210, 1863, 1338)
bbox = (165, 96, 856, 615)
cbox = (136, 1, 1000, 554)
count = 1
while count < 200: # the limit is arbitrary, maybe auto-detect?
    c = "% s" % count
    im = Image.open(str(c) + ".png") # todo: auto-detect file format on target folder
    region = im.crop(cbox)
    region.save(str(c) + "A.png")
    count = count + 1

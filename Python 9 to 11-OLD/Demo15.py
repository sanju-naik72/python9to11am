from PIL import Image as im

from PIL import ImageOps as io

i = im.open("one.jpg")

#img = io.autocontrast(i,20)

img = io.crop(i,60)

img.show()

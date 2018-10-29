from PIL import Image as im

from PIL import ImageFilter as ift

i = im.open("one.jpg")

#im = i.filter(ift.EMBOSS)
#im.show()

#im = i.filter(ift.FIND_EDGES)
#im.show()

im = i.filter(ift.BLUR)
im.show()



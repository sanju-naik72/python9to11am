from PIL import Image as im
ref = im.open("one.jpg")
ref1 = ref.rotate(90)
ref1.show()

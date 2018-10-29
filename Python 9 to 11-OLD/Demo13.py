from PIL import Image as im
ref = im.open("one.jpg")
ref1 = ref.convert("I")
ref1.show()

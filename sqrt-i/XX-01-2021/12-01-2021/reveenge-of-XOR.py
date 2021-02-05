from PIL import Image, ImageChops

im1 = Image.open("sqrt-i\\12-01-2021\\1.jpg")
im2 = Image.open("sqrt-i\\12-01-2021\\2.jpg")

im3 = ImageChops.logical_xor(im1,im2)

im3.show()


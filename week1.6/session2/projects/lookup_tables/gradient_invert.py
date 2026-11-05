from image import Image

table = [9 - x for x in range(10)]
img = Image()
img.read_pgm("../../images/gradient.pgm")

print(img.width)
print(img.height)

for i in range(img.width * img.height):
    img[i] = table[img[i]]

print(img.pixels)

img.write_pgm("inverted_gradient.pgm")
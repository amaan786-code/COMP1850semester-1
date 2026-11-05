from image import Image

table = [255 - x for x in range(256)]
img = Image()
img.read_pgm("../../images/coins.pgm")

print(img.width)
print(img.height)

for i in range(img.width * img.height):
    img[i] = table[img[i]]

img.write_pgm("inverted_coins.pgm")
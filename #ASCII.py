#ASCII

import PIL
from PIL import Image


chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "

im = Image.open("nemo.webp") 
width, height = im.size
pix = im.load()

print(im.mode)
print(f"This is WxL {width},{height}")

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        #print(r)
        h = int((r+ g+ b)/3)
        pix[j,i] = (h,h,h)

im.save ("output.png")
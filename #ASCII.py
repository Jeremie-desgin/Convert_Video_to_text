#ASCII

from PIL import Image, ImageDraw , ImageFont
import math


#chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
chars = " .:;+*#%@"
charArray = list(chars)
charLength = len(charArray)
interval =  charLength/256



scaleFactor = 0.4
onecharWidth = 8
onecharHeight = 18
char_aspect_ratio = onecharWidth/onecharHeight


def getchar(inputint):
    return charArray[math.floor(inputint*interval)]

text_file = open("output.txt", "w")

im = Image.open("nemo.webp").convert("RGB")
width, height = im.size

new_width = int(scaleFactor * width * char_aspect_ratio)
new_height = int(scaleFactor * height * char_aspect_ratio)

im = im.resize((new_width,new_height))
width, height = im.size
pix = im.load()

#print(im.mode)
print(f"This is WxL {width},{height}")

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        #print(r)
        h = int((r + g + b)/3)
        pix[j,i] = (h, h, h)
        text_file.write(getchar(h))
    text_file.write('\n')
text_file.close()
im.save ("output.png")
print("Converted!")
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

fnt = ImageFont.truetype("arial.ttf", 20)

width, height = im.size

print(width,height, height/width )
new_width = int(scaleFactor * width * char_aspect_ratio)
new_height = int(scaleFactor * height * char_aspect_ratio)

im = im.resize((new_width,new_height))
twidth, theight = im.size
pix = im.load()


outputImage = Image.new('RGB', (onecharWidth * twidth, onecharHeight * theight), color = (0,0,0))
print(twidth,theight)

d = ImageDraw.Draw(outputImage)

#print(im.mode)
print(f"This is WxL {width},{height}")

for i in range(theight):
    for j in range(twidth):
        r, g, b = pix[j, i]
        #print(r)
        h = int((r + g + b)/3)
        pix[j,i] = (h, h, h)
        text_file.write(getchar(h))
        d.text((j*onecharHeight, i*onecharWidth), getchar(h), font = fnt, fill = (r,g,b))

    text_file.write('\n')
text_file.close()
outputImage.save ("output.png")
print("Converted!")
from PIL import Image,ImageDraw, ImageFilter, ImageEnhance
import math
import copy

_image_home = "imager/images/"
_image_format = "jpeg"
_pi = math.pi

def generate_adr(name: str) -> str:

    return _image_home + name + "." + _image_format

im = Image.open(generate_adr("donaldduck"))
im2 = Image.open(generate_adr("library"))
im2 = im2.filter(ImageFilter.BLUR)
draw = ImageDraw.Draw(im)
print(im.size)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw


# self.image.putpixel((x, y), rgb)
pi = math.pi


def spiral(im, points=25 ,xmax=100, ymax=100):
    colour = (200,200,0)
    draw = ImageDraw.Draw(im)
    xmax = im.size[0]
    ymax = im.size[1]
    cut_off = max(xmax,ymax)
    interval = (_pi) / points
    value = 0.0
    radius = 1
    origin_x = int(xmax / 2)
    origin_y = int(ymax / 2)
    last_x = int(xmax / 2)
    last_y = int(ymax / 2)
    x = 0
    y = 0
    first_out = True
    holder_l = (0,0)
    holder_c = (0,0)
    x_flag = False
    while radius < cut_off:
        x = origin_x + int(math.cos(value)*radius)
        y = origin_y + int(math.sin(value)*radius)
        if (x >= xmax or y >= ymax) or (y <= 0 or x <= 0):
            holder_l = (last_x, last_y) # holds last values in case of changes
            holder_c = (x, y) # hold current values in case of changes
            last_x = x
            last_y = y
            if(x >= xmax): last_x = xmax ; x_flag = True
            if x <= 0 : last_x = 0 ; x_flag = True
            if(y >= ymax): last_y = ymax
            if y <= 0: last_y = 0

            if first_out:

                first_out = False
                # Calculates where the line would exit the picture
                if x_flag:
                    x_flag = False
                    tan = ((holder_c[1] - holder_l[1])/(holder_c[0] - holder_l[0]))
                    y = holder_l[1] + int(tan*(last_x-holder_l[0]))
                    draw.line(holder_l +(last_x,y),colour)
                else:
                    tan = ((holder_c[0] - holder_l[0]) / (holder_c[1] - holder_l[1]))
                    x = holder_l[0] + int(tan * (last_y - holder_l[1]))
                    draw.line(holder_l + (x, last_y), colour)


        else:
            if not first_out:
                first_out = True
                # Calculates where the line would enter the picture.
                if x_flag:
                    x_flag = False
                    tan = ((y - holder_c[1])/(x - holder_c[0]))
                    last_y = holder_c[1] - int(tan*(holder_c[0]-last_x))
                    draw.line((last_x,last_y) + (x,y),colour)
                else:
                    tan = ((x - holder_c[0]) / (y - holder_c[1]))
                    last_x = holder_c[0] - int(tan * (holder_c[1]-last_y))
                    draw.line((last_x, last_y) + (x, y), colour)
                    pass


            #im.putpixel((x, y), (0,0,0))
            else:
                draw.line((last_x, last_y) + (x,y), colour)
            last_x = x
            last_y = y
        radius += 10/points
        value += interval
    del draw
    return im

def mirror(im, y_lim=1):
    if 0 > y_lim or y_lim > 1:
        y_lim = 1
    for y in range(int(im.size[1]*y_lim)):
        for x in range(int(im.size[0]/2)):
            p1 = im.getpixel((x, y))
            p2 = im.getpixel(((im.size[0] - 1 - x), y))
            im.putpixel((x,y), p2)
            im.putpixel((im.size[0] - 1 - x, y), p1)
    return im

def reflect(im, y_lim=1):
    if 0 > y_lim or y_lim > 1:
        y_lim = 1
    for y in range(int(im.size[1]*y_lim)):
        for x in range(int(im.size[0]/2)):
            p1 = im.getpixel((x, y))
            im.putpixel((im.size[0] - 1 - x, y), p1)
    return im

def fold(im, y_lim=1):
    if 0 > y_lim or y_lim > 1:
        y_lim = 1
    for x in range(int(im.size[0]*y_lim)):
        for y in range(int(im.size[1]/2)):
            p1 = im.getpixel((x, y))
            im.putpixel((x, im.size[1] - 1 -  y), p1)
    return im

w = spiral(Image.open(generate_adr("stairs")),7)
x = reflect(w)
y = fold(x).filter(ImageFilter.BLUR)
y.show()




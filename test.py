from PIL import Image,ImageDraw, ImageFilter, ImageEnhance

_image_home = "imager/images/"
_image_format = "jpeg"

def generate_adr(name: str) -> str:

    return _image_home + name + "." + _image_format

im = Image.open(generate_adr("pinocchio"))
im2 = Image.open(generate_adr("library"))
im2 = im2.filter(ImageFilter.BLUR)
im2.show()
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw
im.show()


from PIL import Image
from imager import imager2
Imager = imager2.Imager
class ArtShow(Image):

    def __init__(self, fname=False, dir=None, ext=None, image=False, width=100, height=100, background='black',
                 mode='RGB'):
        self.init_file_info(fname, dir, ext)
        self.image = image  # A PIL image object
        self.xmax = width;
        self.ymax = height  # These can change if there's an input image or file
        self.mode = mode
        self.init_image(background=background)

    def init_file_info(self, fname=None, dir=None, ext=None):
        self.dir = dir if dir else self._image_dir_
        self.ext = ext if ext else self._image_ext_
        self.fid = self.gen_fid(fname) if fname else None

    def gen_fid(self, fname, dir=None, ext=None):
        dir = dir if dir else self.dir
        ext = ext if ext else self.ext
        return dir + fname + "." + ext


from PIL import Image, ImageFilter
import pathlib
from enum import Enum

HEIGHT_RATIO = 24


class CutMode(Enum):
    KODAK = 17/HEIGHT_RATIO
    OLYMPUS = 18/HEIGHT_RATIO


class Cutter:
    path = None
    mode = None
    originalImage = None
    croppedImage_r = None
    croppedImage_l = None

    def __init__(self, path, mode=CutMode.KODAK):
        self.path = pathlib.Path(path)
        self.mode = mode
        self.__cut()

    def __cut(self):
        # Open the image
        img = Image.open(self.path)
        width, height = img.size

        # Crop the image
        new_width = height * self.mode.value
        area_r = (0, 0, new_width, height)
        area_l = (width - new_width, 0, width, height)
        self.croppedImage_r = img.crop(area_r)
        self.croppedImage_l = img.crop(area_l)

    def save(self,directory=None):
        if directory:
            r_path = pathlib.Path(directory).joinpath(self.path.stem + "_r" + self.path.suffix)
            l_path = pathlib.Path(directory).joinpath(self.path.stem + "_l" + self.path.suffix)
        else:
            r_path = self.path.with_name(self.path.stem + "_r" + self.path.suffix)
            l_path = self.path.with_name(self.path.stem + "_l" + self.path.suffix)
        self.croppedImage_r.save(r_path)
        self.croppedImage_l.save(l_path)

if __name__ == "__main__":
    cutter = Cutter("sample/image1.jpg", CutMode.KODAK)
    cutter.save()

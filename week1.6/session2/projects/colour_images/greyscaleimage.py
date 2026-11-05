from image import Image, ImageError

class GreyscaleImage(Image):
    """
    A greyscale image.
    """

    @classmethod
    def read(cls, filename):
        """
        Creates a GreyscaleImage from data in the specified PGM file.
        """
        image = GreyscaleImage()
        image.read_pgm(filename)
        return image

    def create_pixels(self, width, height, value=0, maximum=255):
        """
        Creates a new array of pixels, replacing any existing image data.

        All pixels are initialized to 0 by default, but you can provide a
        different value as an argument after width and height.

        A maximum allowed value can be also be specified; if not provided,
        it defaults to 255.
        """
        if width < 1:
            raise ImageError("width cannot be < 1")
        if height < 1:
            raise ImageError("height cannot be < 1")

        self.width = width
        self.height = height
        self.max_value = maximum
        self.pixels = [value] * (width * height)

    def _parse_magic_number(self, imgfile):
        line = imgfile.readline().strip()
        if line != "P2":
            raise ImageError("unrecognized magic number")

    def _parse_pixels(self, imgfile):
        self.pixels = [int(value) for value in imgfile.read().split()]

        if len(self.pixels) != self.width * self.height:
            raise ImageError("number of pixels doesn't match image dimensions")

        if any(p < 0 or p > self.max_value for p in self.pixels):
            raise ImageError(f"pixel value outside allowed range (0 to {self.max_value})")

    def _write_header(self, imgfile):
        print("P2", file=imgfile)
        print(self.width, self.height, file=imgfile)
        print(self.max_value, file=imgfile)

    def _write_pixels(self, imgfile):
        for row in range(self.height):
            start = row * self.width
            for value in self.pixels[start:start + self.width]:
                print(f"{value:4d}", end="", file=imgfile)
            print(file=imgfile)
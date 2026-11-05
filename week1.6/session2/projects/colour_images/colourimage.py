from image import Image, ImageError

class ColourImage(Image):
    """
    A colour image.
    """

    @classmethod
    def read(cls, filename):
        """
        Creates a ColourImage from data in the specified PGM file.
        """
        image = ColourImage()
        image.read_pgm(filename)
        return image

    def create_pixels(self, width, height, value=0, maximum=255):
        """
        Creates a new array of pixels, replacing any existing image data.

        All pixels are initialized to (R=0,G=0,B=0) by default, but you can provide a
        different value as an argument after width and height.

        A maximum allowed value can be also be specified; if not provided,
        it defaults to (R=255,G=255,B=255).
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
        if line != "P3":
            raise ImageError("unrecognized magic number")

    def _parse_pixels(self, imgfile):
        self.pixels = []
        raw_parts = imgfile.read().split()

        # since it's RGB colours, it will always be a multiple of 3
        for pixel in range(len(raw_parts) // 3): 
            r = pixel * 3
            g = r + 1
            b = r + 2

            self.pixels.append((int(raw_parts[r]), int(raw_parts[g]), int(raw_parts[b])))


        if len(self.pixels) != self.width * self.height:
            raise ImageError("number of pixels doesn't match image dimensions")

        if any(p < (0,0,0) or p > (self.max_value, self.max_value, self.max_value) for p in self.pixels):
            raise ImageError(f"pixel value outside allowed range (0 to {self.max_value})")

    def _write_header(self, imgfile):
        print("P3", file=imgfile)
        print(self.width, self.height, file=imgfile)
        print(self.max_value, file=imgfile)

    def _write_pixels(self, imgfile):
        for row in range(self.height):
            start = row * self.width
            rowList = []
            for value in self.pixels[start:start + self.width]:
                rowList.append(f"{value[0]:4d}{value[1]:4d}{value[2]:4d}")
            print("  ".join(rowList), file=imgfile)
            
        print(file=imgfile)
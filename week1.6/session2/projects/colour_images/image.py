# Week 1.6, Session 2

"""
Classes for working with images.
"""

import copy
from abc import ABC, abstractmethod

class ImageError(Exception):
    """
    Exception for problems that may occur when working with Image subclass objects.
    """

class Image(ABC):
    """
    A generic image. Cannot be instantiated.
    """

    def read_pgm(self, filename):
        """
        Reads data from the specified PGM image file into this Image.

        Any existing image data will be replaced.
        """
        with open(filename) as imgfile:
            self._parse_magic_number(imgfile)
            self._parse_dimensions(imgfile)
            self._parse_max_value(imgfile)
            self._parse_pixels(imgfile)


    @abstractmethod # Outside spec: this just forces the child to implement the marked methods.
    def _parse_magic_number(self, imgfile):
        pass

    @abstractmethod
    def _parse_pixels(self, imgfile):
        pass

    def _parse_dimensions(self, imgfile):
        line = imgfile.readline().strip()
        if line.startswith("#"):
            # Ignore comment and read another line
            line = imgfile.readline().strip()
        parts = line.split()
        self.width = int(parts[0])
        self.height = int(parts[1])

    @abstractmethod
    def _parse_max_value(self, imgfile):
        pass

    def __getitem__(self, index):
        """
        Returns pixel value at the specified linear index.
        """
        return self.pixels[index]

    def __setitem__(self, index, value):
        """
        Sets pixel at the specified linear index to the specified value.
        """
        self.pixels[index] = value

    def get(self, row, col):
        """
        Returns pixel value at the specified row & column coordinates.
        """
        index = row * self.width + col
        return self.pixels[index]

    def set(self, row, col, value):
        """
        Sets pixel at the specified row & column coordinates to the given value.
        """
        index = row * self.width + col
        self.pixels[index] = value

    def copy(self):
        """
        Returns a new Image that is a copy of this Image.
        """
        return copy.deepcopy(self)

    def write_pgm(self, filename):
        """
        Writes this Image to the specified PGM file.
        """
        with open(filename, "wt") as imgfile:
            self._write_header(imgfile)
            self._write_pixels(imgfile)

    @abstractmethod
    def _write_header(self, imgfile):
        pass

    @abstractmethod
    def _write_pixels(self, imgfile):
        pass


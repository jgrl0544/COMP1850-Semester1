from image import Image, ImageError # we don't even need  to do this; greyscaleimage and colourimage have it all!
from greyscaleimage import GreyscaleImage
from colourimage import ColourImage


image = GreyscaleImage.read("C:/Users/oufta/Desktop/Repos/COMP1850-Semester1/week1.6/session2/images/plus.pgm")
print(image.pixels)
image.write_pgm("C:/Users/oufta/Desktop/Repos/COMP1850-Semester1/week1.6/session2/images/simple2.ppm")

image = ColourImage.read("C:/Users/oufta/Desktop/Repos/COMP1850-Semester1/week1.6/session2/images/simple.ppm")
print(image.pixels)
image.write_pgm("C:/Users/oufta/Desktop/Repos/COMP1850-Semester1/week1.6/session2/images/simple2.ppm")
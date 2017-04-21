#Manipulating images

from __future__ import print_function
from PIL import Image, ImageFilter  # imports the library
import sys, os
image = Image.open('media/images/de_winner.jpg')
image.show()

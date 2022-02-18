## This is a test script for the camera. 
# TODO: 
#   [x] - Get all import stuff to work
#   [x] - Initialize camera
#   [x] - Generate a single bitmap and send to output
#   [] - Generate a stream of bitmaps and send to output as new directory
#   [] - 

#imports
import src
from IPython import embed
from src import camera
from src.camera import *

#intialize camera
cam0 = init_camera()

#capture an image
path = './output/photo.bmp'
capture_one(cam0,path)

#edit from Mark's computer! wahoo


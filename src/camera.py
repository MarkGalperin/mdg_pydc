# This is the module that runs the FLIR camera 
import sys
import cv2 as cv
from time import sleep
from pydc1394 import Camera
from PIL import Image

def init_camera():
    '''
    Docstring
    '''
    
    print("Opening camera")
    cam0 = Camera()

    #those can be automated, the other are manual
    try:
        cam0.brightness.mode = 'auto'
        cam0.exposure.mode = 'auto'
        cam0.white_balance.mode = 'auto'
    except AttributeError: # thrown if the camera misses one of the features
        pass


    for feat in cam0.features:
        print("%s (cam0): %s" % (feat,cam0.__getattribute__(feat).value))

    #choose color mode
    # print(cam0.modes)
    cam0.mode = cam0.modes[0]

    #Change position to 0,0 (we don't want any offset)
    my_pos = (0,0)
    cam0.mode.image_position = my_pos

    #To change resolution of acquisition
    my_size = (2080,1552)
    cam0.mode.image_size = my_size

    return cam0

def capture_one(cam,path=None):
    '''
    This function takes a single photo, and returns either an image object or saves to a path.
    Takes...
        cam: pydc1394 camera object
        path (optional): [str] relative path for saving, with filetype specified. 
    Returns...
        i: PIL image object. Returns only when the path is not specified
    '''
    #start capture
    cam.start_capture()
    cam.start_one_shot()
    matrix = cam.dequeue()

    #image properties
    print("Shape:", matrix.shape)
    i = Image.fromarray(matrix.copy())
    matrix.enqueue()

    #finish capture
    cam.stop_one_shot()
    cam.stop_capture()

    if path is not None:
        #save image
        i.save(path)
    else:
        #return the image as image object
        return i
    

def calibrate():
    #This function calibrates the camera, making use of capture_one() and opencv functions



if __name__ == '__main__':

    #intialize camera
    cam0 = init_camera()

    #capture image
    cam0.start_capture()
    cam0.start_one_shot()
    matrix = cam0.dequeue()

    #image properties
    print("Shape:", matrix.shape)
    i = Image.fromarray(matrix.copy())
    matrix.enqueue()

    #save image
    cam0.stop_one_shot()
    cam0.stop_capture()
    i.save("../output/camera/t.bmp")


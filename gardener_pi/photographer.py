from picamera import PiCamera
import datetime
import csv

# Initial set-up
camera = PiCamera()

# This function takes in no parameters.
# When called, it does two things:
# It takes a picture and stores it locally, with the name of the file ebing teh timestamp the image was taken at.
# It returns the time when the image was called so that the data can be documented in conjunction 
# with the degree of wetness from the moisture detector module.

def start_camera(image_path):
    time_when_called = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
    camera.capture(image_path)
    return time_when_called
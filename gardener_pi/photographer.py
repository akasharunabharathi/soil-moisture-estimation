from picamera import PiCamera
import datetime
import csv

# Initial set-up
camera = PiCamera()
image_data_log_address = './data-logs/images/'

# This function takes in no parameters.
# When called, it does two things:
# It takes a picture and stores it locally, with the name of the file ebing teh timestamp the image was taken at.
# It returns the time when the image was called so that the data can be documented in conjunction 
# with the degree of wetness from the moisture detector module.

def start_camera():
    time_when_called = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
    camera.capture(image_data_log_address % time_when_called)
    return time_when_called
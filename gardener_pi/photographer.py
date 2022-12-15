from picamera import PiCamera
import datetime
from time import sleep

camera = PiCamera()

def start_camera():
    while(True):
        sleep(15)
        camera.capture('./data-logs/image-data' % datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"))
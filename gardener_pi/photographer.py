from picamera import PiCamera
import datetime
from time import sleep

camera = PiCamera()

while(True):
    sleep(15)
    camera.capture('./image-data' % datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"))
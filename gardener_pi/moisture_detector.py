# What the code in this file needs to do:
# We've got to get this file to talk to the arduino which has got the moisture sensor.

#!/usr/bin/env python3

import pyserial

if __name__ == '__main__':
    ser = pyserial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)


#!/usr/bin/env python3

# DO NOT EDIT LINE 1

# Import statements
import serial
import time
import csv
import datetime

# Hardcoded addresses that might need to change with future implementations
data_log_path = "./data-logs/moisture-data.csv"
arduino_serial_port = '/dev/ttyUSB0'

# This function acts as our interface between the Arduino connected to the soil moisture sensor
# and the rest of our modular automated garden.
# It takes in no parameters.
# Returns a list containing class string describing degree of soil wetness, analog value read in from soil moisture sensor, and timestamp of read
# Also writes to data log.
def soil_moisture_reader():
    with open(data_log_path) as file:
        # Initial set-up
        ser = serial.Serial(arduino_serial_port, 9600, timeout=1)
        ser.reset_input_buffer()
        csv_writer = csv.writer(file)

        # This is the crux of our soil mositure detection function
        # In other modules, this function will be called multiple times over and over in a loop
        # Perhaps at the rate of once per second.
        time.sleep(1000)
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            contents = line.split(":")
            # contents.append(datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"))
            csv_writer.writerow(contents)
            return contents

#import libraries
import moisture_detector
import photographer
import time
import csv
import RPi.GPIO as GPIO

#Sensor: Relay 1: GPIO 37
relay_pin = 37
sleep_for = 300 * 3
data_log_address = "./data-logs/image-logs.csv"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin,GPIO.OUT)

try:
    while True:
        # The condition for checkness for degree of wetness of the soil by invoking the moisture_detector module.
        # We're presently treating both "Wet" and "Very wet" as the same, but they can certainly be distinguished between later on.
        if ((moisture_detector.soil_moisture_reader()[0]) == "Wet" or moisture_detector.soil_moisture_reader()[0] == "Very wet"):
            # print('Wet')
            
            write_to_file = open(data_log_address)
            writer = csv.writer(write_to_file)
            contents = moisture_detector.soil_moisture_reader().append(photographer.start_camera())
            writer.writerow(contents)
            write_to_file.close()

            # If the soil is already wet, we leave the pin closed.
            GPIO.output(relay_pin,True)
            
        elif (moisture_detector.soil_moisture_reader()[0] == "Dry"):
            # print('Dry')

            write_to_file = open(data_log_address)
            writer = csv.writer(write_to_file)
            contents = moisture_detector.soil_moisture_reader().append(photographer.start_camera())
            writer.writerow(contents)
            write_to_file.close()

            # If our soil is dry, we open the solenoid valve, i.e. release water for three minutes
            # and then, we shut the valve.
            GPIO.output(relay_pin,False)
            time.sleep(sleep_for/5)
            GPIO.output(relay_pin, True)

        time.sleep(sleep_for)

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
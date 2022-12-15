# import libraries
import time
import csv
import os
import numpy as np
import RPi.GPIO as GPIO

# custom dependencies
import moisture_detector
import photographer

# Relay Pin: GPIO 37
relay_pin = 37
sleep_for = 300 * 3
data_log_address = "./data-logs/image-logs.csv"
image_data_log_address = './data-logs/images/'
train_test_randomizer = ["train/", "test/"]

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
            # We're randomly picking whether we should right the image to test or to train.
            # We want an 85%-15% split.
            train_vs_test = np.random.choice(train_test_randomizer, 1, [0.85, 0.15])
            image_path = os.path.join(image_data_log_address, train_vs_test + "wet_soil")
            # The below line of code may seem complex given that it calls multiple functions and appears to be doing multiple things.
            # We're first reading in the moisture again.
            # There will be no significant difference in value between when we read it in the condition and when we read it here.
            # The call to the moisture reader functions returns a list containing the class of soil wetness and analog value of wetness.
            # The call to the photographer function returns the timestamp at which the picture was taken, which is what we're appending
            # before writing to our CSV file.
            contents = moisture_detector.soil_moisture_reader().append(photographer.start_camera(image_path = image_path))
            # The parameter passed to the photographer module is the path at which we store the image
            writer.writerow(contents)
            # The contents, of, well, "contents", have been written to the CSV file.
            write_to_file.close()

            # If the soil is already wet, we leave the pin closed.
            GPIO.output(relay_pin,True)
            
        elif (moisture_detector.soil_moisture_reader()[0] == "Dry"):
            # print('Dry')

            write_to_file = open(data_log_address)
            writer = csv.writer(write_to_file)
            # We're randomly picking whether we should right the image to test or to train.
            # We want an 85%-15% split.
            train_vs_test = np.random.choice(train_test_randomizer, 1, [0.85, 0.15])
            image_path = os.path.join(image_data_log_address, train_vs_test + "dry_soil")
            contents = moisture_detector.soil_moisture_reader().append(photographer.start_camera(image_path = image_path))
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
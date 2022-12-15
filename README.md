# visual-soil-moisture-estimator

The project involves data collection on soil moisture content (from a traditional soil moisture measurement probe), temperature data, and images of topsoil to achieve to design new, cost-effective and reliable way(s) of detecting soil moisture to solve the problem of gradual corrosion and dropping reliability that users experience with traditional soil-measurement probes available on the market today.

The approach taken to solving this problem is that we're trying to determine if estimates of soil moisture levels can be reliably gleaned from images of topsoil alone using Computer Vision – by using topsoil images taken at regular intervals and attempting to correlate temporal, ground-truth data from the soil moisture measurement probe and the temperature sensor.

# Hardware Setup

This project uses a Raspberry Pi 4, an Arduino Uno, a DFROBOT Capacitive V1.0 Soil Moisture sensor,

![alt_text](https://dfimg.dfrobot.com/nobody/wiki/33a9b85e364788554501f1dd493ba846.png)

The Arduino Uno is connected via USB to the Raspberry Pi and communicates via Serial Communication. We are currently connected to `/dev/ttyUSB0`, which is a hardcoded address that might need to be changed depending on the the user.

![alt_text](https://roboticsbackend.com/wp-content/uploads/2019/11/raspberrypi_arduino_uno_serial_usb.png)

(To ensure Serial Communication works, head to Menu -> Prefernces -> Interfaces and toggle Serial Communication "on". Reboot Raspberry Pi to make changes take effect.)

The solenoid valve to control water flow is connected to a relay hat that is mounted on top of the Raspberry Pi, and the camera is connnected directly to the Raspberry Pi through the camera port.

# File Structure

The project is organized into different dircectories depending on their specific utilities. Enclosed below is a brief overview of the contents of each directory.

• gardener_pi: Contains all Python code for the moisture detection, image capture, and data logging. For Raspberry Pi.
• arduino: Code for interfacing with soil moisture sensor and sending data to Raspberry Pi via Serial Communication.
• data-logs: Contains all CSV files, and images sub-folder for Computer Vision model training. The sub folder is organized into `train` and `test` subfolders, each of which are further organized into `wet_soil` and `dry_soil` folders. Image capture data is split into an 85%-15% ratio between the `train` and `test` modules respectively.

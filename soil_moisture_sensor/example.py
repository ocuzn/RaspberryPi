#https://38-3d.co.uk/blogs/blog/using-a-soil-moisture-sensor-with-the-raspberry-pi

import RPi.GPIO as GPIO
import time

SENSOR_PIN = 17  # GPIO Pin connected to D0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(SENSOR_PIN):
            print("Soil is Dry!")
        else:
            print("Soil is Moist!")
        time.sleep(2)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()

#See https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-traffic-light

import RPi.GPIO as GPIO
import time

# Define GPIO pins
PIN_RED = 7     # The Raspberry Pi GPIO pin connected to the R pin of the traffic light module
PIN_YELLOW = 8  # The Raspberry Pi GPIO pin connected to the Y pin of the traffic light module
PIN_GREEN = 25  # The Raspberry Pi GPIO pin connected to the G pin of the traffic light module

# Define time durations
RED_TIME = 4     # RED time in seconds
YELLOW_TIME = 4  # YELLOW time in seconds
GREEN_TIME = 4   # GREEN time in seconds

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_YELLOW, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)

try:
    while True:
        # Red light on
        GPIO.output(PIN_RED, GPIO.HIGH)
        GPIO.output(PIN_YELLOW, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.LOW)
        time.sleep(RED_TIME)

        # Yellow light on
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_YELLOW, GPIO.HIGH)
        GPIO.output(PIN_GREEN, GPIO.LOW)
        time.sleep(YELLOW_TIME)

        # Green light on
        GPIO.output(PIN_RED, GPIO.LOW)
        GPIO.output(PIN_YELLOW, GPIO.LOW)
        GPIO.output(PIN_GREEN, GPIO.HIGH)
        time.sleep(GREEN_TIME)

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()

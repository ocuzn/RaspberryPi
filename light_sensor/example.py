import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
DIGITAL_PIN = 18
GPIO.setup(DIGITAL_PIN, GPIO.IN)
time.sleep(2)
print('[Press CTRL + C to end the script!]')
try: # Main program loop
        while True:
                if GPIO.input(DIGITAL_PIN)==0:
                        print('Light detected!')
                        time.sleep(2)
                else:
                        print('No light!')
                        time.sleep(2)
except KeyboardInterrupt:
        print('\nScript end!')
finally:
        GPIO.cleanup()

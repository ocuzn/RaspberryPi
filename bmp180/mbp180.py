import time
import Adafruit_BMP.BMP085 as BMP085

# Specify busnum=1 for Raspberry Pi 4
sensor = BMP085.BMP085(busnum=1)

while True:
    try:
        temp = sensor.read_temperature()
        pressure = sensor.read_pressure()
        altitude = sensor.read_altitude()

        print(f"Temperature: {temp:.2f} °C")
        print(f"Pressure: {pressure / 100:.2f} hPa")
        print(f"Altitude: {altitude:.2f} m")
        print("-" * 30)

        time.sleep(2)

    except KeyboardInterrupt:
        print("Exiting...")
        break
    except Exception as e:
        print(f"Error: {e}")

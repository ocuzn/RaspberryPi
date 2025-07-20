# RaspberryPi

A collection of example tests for different raspberry pi modules:

Raspberry pi 4B

| Pin | BCM | Name    | Name    | BCM | Pin |
|-----|-----|---------|---------|-----|-----|
|  1  |     | 3.3V    | 5V      |     |  2  |
|  3  |  2  | GPIO2   | 5V      |     |  4  |
|  5  |  3  | GPIO3   | GND     |     |  6  |
|  7  |  4  | GPIO4   | GPIO14  | 14  |  8  |
|  9  |     | GND     | GPIO15  | 15  | 10  |
| 11  | 17  | GPIO17  | GPIO18  | 18  | 12  |
| 13  | 27  | GPIO27  | GND     |     | 14  |
| 15  | 22  | GPIO22  | GPIO23  | 23  | 16  |
| 17  |     | 3.3V    | GPIO24  | 24  | 18  |
| 19  | 10  | GPIO10  | GND     |     | 20  |
| 21  |  9  | GPIO9   | GPIO25  | 25  | 22  |
| 23  | 11  | GPIO11  | GPIO8   |  8  | 24  |
| 25  |     | GND     | GPIO7   |  7  | 26  |
| 27  |     | ID_SD   | ID_SC   |     | 28  |
| 29  |  5  | GPIO5   | GND     |     | 30  |
| 31  |  6  | GPIO6   | GPIO12  | 12  | 32  |
| 33  | 13  | GPIO13  | GND     |     | 34  |
| 35  | 19  | GPIO19  | GPIO16  | 16  | 36  |
| 37  | 26  | GPIO26  | GPIO20  | 20  | 38  |
| 39  |     | GND     | GPIO21  | 21  | 40  |

---

**MP180**: Barometric sensor module, measures pressure altitude and temperature

**DHT11**: Measures temperature and humidity

**OV5647**: Camera module.
Easy way to test steam over VLC -> 

```
libcamera-vid -t 0 --width 640 --height 480 --framerate 25 --inline --listen -o - | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8080}' :demux=h264
```

 Open VLC → Media → Open Network Stream → enter: `http://<raspberry_pi_ip>:8080`
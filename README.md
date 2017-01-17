# Full-color-RGB-LED-Strip-Driver
Example driver for DX ledstrip module
http://www.dx.com/p/full-color-rgb-led-strip-driver-module-w-dc-jack-for-arduino-440804#.WH6XEPnhCUk

the arduino driver seemed very complex for adding values to a number and sending it as binary.

#Example usage
* SetColor(1,1,1)  -> turns on all tree colors
* SetColor(1,0,0) -> Red only
* SetColor(0,1,1) -> Green + Blue

```python
import rgb
import time
while True:
	rgb.SetColor(1,0,0)
	time.sleep(2)
	rgb.SetColor(0,1,0)
	time.sleep(2)
	rgb.SetColor(0,0,1)
	time.sleep(2)
	rgb.SetColor(1,1,0)
	time.sleep(2)
	rgb.SetColor(1,1,1)
	time.sleep(2)
	rgb.SetColor(0,1,1)
	time.sleep(2)
	rgb.SetColor(1,0,1)
```


* 000 off
* 100 red
* 010 green
* 001 blue
* 110 light green
* 011 turquoise
* 101 purple
* 111 white

spi communication hardcoded spi1  port 19 + 23 and using lib
https://github.com/doceme/py-spidev

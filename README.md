# Full-color-RGB-LED-Strip-Driver
Example driver for DX ledstrip module
http://www.dx.com/p/full-color-rgb-led-strip-driver-module-w-dc-jack-for-arduino-440804#.WH6XEPnhCUk



#Example usage
* SetColor(255,255,255)  -> turns on all tree colors
* SetColor(255,0,0) -> Red only
* SetColor(0,255,255) -> Green + Blue

```python
import rgb
import time
while True:
	rgb.SetColor(255,0,255)
	time.sleep(2)
	rgb.SetColor(100,255,0)
	time.sleep(2)
	
```


spi communication hardcoded spi1  port 19 + 23 and using lib
https://github.com/doceme/py-spidev

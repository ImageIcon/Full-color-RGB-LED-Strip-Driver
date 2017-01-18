#!/usr/bin/python
import spidev
spi = spidev.SpiDev()
spi.open(0, 0)

def SetColor(red, green, blue):
	#"0000 1 1 /B7 /B6 /G7 /G6 /R7 /R6 0000"
	prefix = (1 << 6) | (1 << 7);
	if ((blue & 0x80) == 0): prefix |= (1 << 5);
	if ((blue & 0x40) == 0): prefix |= (1 << 4);
	if ((green & 0x80) == 0): prefix |= (1 << 3);
	if ((green & 0x40) == 0): prefix |= (1 << 2);
	if ((red & 0x80) == 0): prefix |= (1 << 1);
	if ((red & 0x40) == 0): prefix |= (1 << 0);
	spi.writebytes([0,0,0,0,prefix,blue,green,red,0,0,0,0,])
  
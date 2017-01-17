#!/usr/bin/python
import spidev
spi = spidev.SpiDev()
spi.open(0, 0)

def bitfield(n):
  return [1 if digit=='1' else 0 for digit in bin(n)[2:]]

  
def SetColor(Red,Green,Blue):
#magic starting number.
  dx = 4227858464;
  dx += Red << 2;             
  dx += Green << 3;
  dx += Blue << 4;	
  spi.writebytes(bitfield(dx))

 
SetColor(1,1,1)



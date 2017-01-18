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
	spi.writebytes([0,0,0,0,prefix,blue,green,red,0,0,0,0,]);
	
#Rest is just for HSV colors and can be skipped..
def myconstrain(input, min, max):
	if(input > max): input = max;
	if(input < min): input = min;
	return input;
	
def hue2rgb(p, q, t):
	if (t < 0.0):
		t += 1.0;
	if(t > 1.0):
		t -= 1.0;
	if(t < 1.0/6.0):
		return p + (q - p) * 6.0 * t;
	if(t < 1.0/2.0):
		return q;
	if(t < 2.0/3.0):
		return p + (q - p) * (2.0/3.0 - t) * 6.0;
	return p;
	
def SetColorHSV(hue, saturation, brightness):
	r, g, b;
	myconstrain(hue, 0.0, 1.0);
	myconstrain(saturation, 0.0, 1.0);
	myconstrain(brightness, 0.0, 1.0);
	if(saturation == 0.0): 
		r = g = b = brightness;
    	else:
			if(brightness < 0.5):
				q = brightness * (1.0 + saturation); 
			else: 
				q =brightness + saturation - brightness * saturation;
			p = 2.0 * brightness - q;
			r = hue2rgb(p, q, hue + (1.0/3.0));
			g = hue2rgb(p, q, hue);
			b = hue2rgb(p, q, hue - 1.0/3.0);
	SetColor(255.0*r,255.0*g,255.0*b);
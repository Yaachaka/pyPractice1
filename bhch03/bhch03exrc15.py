from math import sin, cos, pi

for i in range(0, 360, 15):
	j = i*pi/180
	print(i, ' --- ', round(sin(j),4), '   ', round(cos(j), 4))
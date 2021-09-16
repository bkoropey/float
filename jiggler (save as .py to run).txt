#!/us/bin/env python
# coding: utf-8

import ctypes
import time
import datetime

mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTIF_MOVE = 0x0001

print("press ctrl-c to end mouse jiggler")

try:

	while True:
		choices = [(1,0,0,0,), (0,1,0,0,), (-1,0,0,0), (0,-1,0,0)]

		# dir = randome.choice(choices)
		for dir in choices:
			mouse_event(MOUSEEVENTIF_MOVE, *dir)


except KeyboardInterrupt:
	pass

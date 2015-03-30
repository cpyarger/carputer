import time

import gaugette.rotary_encoder
import gaugette.switch
import os

A_PIN  = 7
B_PIN  = 9
SW_PIN = 8

encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()
switch = gaugette.switch.Switch(SW_PIN)
last_state = None

while True:
    delta = encoder.get_delta()
    if delta!=0:
        print "rotate %d" % delta
        if delta >= 1:
           os.system("vol +")
        if delta <= -1:
           os.system("vol -")
    sw_state = switch.get_state()
    if sw_state != last_state:
        if sw_state == 1: 
           #toggle()
           os.system("vol T")
        print "switch %d" % sw_state
        last_state = sw_state

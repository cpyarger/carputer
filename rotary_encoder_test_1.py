import time

import gaugette.rotary_encoder
import gaugette.switch
import os
A_PIN  = 7
B_PIN  = 9
SW_PIN = 8
 
encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
switch = gaugette.switch.Switch(SW_PIN)
last_state = None
 
while True:
    time.sleep(.1)
    delta = encoder.get_delta()
    if delta!=0:
        print "rotate %d" % delta
        if delta == 1:
           os.system("mpc prev")
        if delta == -1:
           os.system("mpc next")
    sw_state = switch.get_state()
    if sw_state != last_state:
        if sw_state == 1: 
           os.system("mpc toggle")
        print "switch %d" % sw_state
        last_state = sw_state

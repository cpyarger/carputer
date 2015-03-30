import time

import gaugette.rotary_encoder
import gaugette.switch
import os

A_PIN  = 7
B_PIN  = 9
SW_PIN = 8
encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
switch = gaugette.switch.Switch(SW_PIN)


while True:
    time.sleep(.1)
    delta = encoder.get_delta()
    print "rotate %d" % delta
    sw_state = switch.get_state()
    print "switch %d" % sw_state

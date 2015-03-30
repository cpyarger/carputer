import time

import gaugette.rotary_encoder
import gaugette.switch
import os
global t

A_PIN  = 9
B_PIN  = 7
SW_PIN = 3
t = True 
encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
switch = gaugette.switch.Switch(SW_PIN)
last_state = None

def toggle ():
    global t
    print ("toggle")
    if t == True:
        print("true")
        os.system("mpc pause")
        t = not t

    if t != True:
        print("not true")
        os.system("mpc play")

        t = not t


while True:
    time.sleep(.1)
    delta = encoder.get_delta()
    if delta!=0:
        print "rotate %d" % delta
        if delta == 1:
           os.system("mpc prev")
           time.sleep(.1)
        if delta == -1:
           os.system("mpc next")
           time.sleep(.1)
    sw_state = switch.get_state()
    if sw_state != last_state:
        if sw_state == 1: 
           toggle()
           time.sleep(.1)
        print "switch %d" % sw_state
        last_state = sw_state

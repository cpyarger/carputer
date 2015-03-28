#!/bin/bash
# GPS startup script for uBlox LEA-6H
# Generated off on info pulled from the interwebs
# By: cpyarger <cpyarger@gmail.com>

sudo killall gpsd
stty -F /dev/ttyAMA0 115200
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
cgps -s

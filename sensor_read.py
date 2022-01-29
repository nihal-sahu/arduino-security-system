#!/usr/bin/env python3

import pyfirmata
import time

if __name__ == '__main__':
    arduino = pyfirmata.Arduino('/dev/ttyUSB0')
    print("Communication Successfully started")
    
    #same as void loop();
    while True:
        
#THE FOLLOWING TEST CODE IS FROM https://roboticsbackend.com/control-arduino-with-python-and-pyfirmata-from-raspberry-pi/
#!/usr/bin/env python3

import pyfirmata
import time

if __name__ == '__main__':
    board = pyfirmata.Arduino('/dev/ttyUSB0')
    board.digital[13].mode = pyfirmata.OUTPUT
    print("Communication Successfully started")
    

    while True:
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
        time.sleep(1)
    

import sys
import time

from pymata4 import pymata4

DIGITAL_PIN = 13  # arduino pin number


def blink(my_board, pin):
 
    # set the pin mode
    my_board.set_pin_mode_digital_output(pin)
    my_board.digital_write(pin, 1)

    # toggle the pin 4 times and exit
    while True:
        print('ON')
        my_board.digital_write(pin, 1)
        time.sleep(1)
        print('OFF')
        my_board.digital_write(pin, 0)
        time.sleep(1)


board = pymata4.Pymata4()

blink(board, DIGITAL_PIN)

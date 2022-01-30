import sys
import time
from pymata4 import pymata4

board = pymata4.Pymata4()
triggerPin = 10
echoPin = 11
DISTANCE_CM = 2

# A callback function to display the distance
def display(data):
    """
    The callback function to display the change in distance
    :param data: [pin_type=12, trigger pin number, distance, timestamp]
    """
    print(f'Distance in cm: {data[DISTANCE_CM]}')

def get_distance(callback):

    # set the pin mode for the trigger and echo pins
    board.set_pin_mode_sonar(triggerPin, echoPin, callback)
    # wait forever
    while True:
        time.sleep(.01)
        print(f'data read: {board.sonar_read(triggerPin)}')

get_distance(display)


import sys
import time
from pymata4 import pymata4

board = pymata4.Pymata4()
triggerPin = 10
echoPin = 11
DISTANCE_CM = 2

# A callback function to display the distance
def display(data):
    print(f'Distance in cm: {data[DISTANCE_CM]}')

def get_distance(callback):
    board.set_pin_mode_sonar(triggerPin, echoPin, callback)
    #loops forever
    while True:
        time.sleep(.01)
        print(f'data read: {board.sonar_read(triggerPin)}')

print("The pymata4 library can be found at https://github.com/MrYsLab/pymata4\nThe following code was developed by Nihal Sahu and Nishan Sivakumar\n")

get_distance(display)


import sys
import time
from pymata4 import pymata4
import mail_protocol

board = pymata4.Pymata4()
triggerPin = 12
echoPin = 13

RED = 8
YELLOW = 9
GREEN = 11

board.set_pin_mode_digital_output(RED)
board.set_pin_mode_digital_output(YELLOW)
board.set_pin_mode_digital_output(GREEN)

def red():
    board.digital_write(RED, 1)
    board.digital_write(YELLOW, 0)
    board.digital_write(GREEN, 0)

def yellow():
    board.digital_write(YELLOW, 1)
    board.digital_write(RED, 0)
    board.digital_write(GREEN, 0)

def green():
    board.digital_write(GREEN, 1)
    board.digital_write(RED, 0)
    board.digital_write(YELLOW, 0)

def get_distance():
    board.set_pin_mode_sonar(triggerPin, echoPin)
    max_distance = 0;
    startTime = time.time()
    emailNotif = True
    yellow()

    #loops forever
    while True:
        time.sleep(0.2)
        print(board.sonar_read(triggerPin)[0], "cm")
        currentTime = time.time()

        #condition only executes for first 15 seconds of program execution
        if (currentTime - startTime < 15):
            if (board.sonar_read(triggerPin)[0] > max_distance):
                max_distance = board.sonar_read(triggerPin)[0]
            currentTime = time.time()
        elif (currentTime - startTime >= 15 and emailNotif == True):
            green()

        if ((max_distance - board.sonar_read(triggerPin)[0] >= 30) and emailNotif == True):
            print("MOVEMENT DETECTED. ALERT SENT.")
            red()
            time.sleep(3)
            mail_protocol.alert_email()
            emailNotif = False
            startTime2 = time.time()
            currentTime2 = time.time()
        elif (emailNotif == False):
            yellow()
            if (currentTime2 - startTime2 > 15):
                emailNotif = True
                green()
            currentTime2 = time.time()
            
print("The pymata4 library can be found at https://github.com/MrYsLab/pymata4 \nThe following code was developed by Nihal Sahu and Nishan Sivakumar\n")

get_distance()


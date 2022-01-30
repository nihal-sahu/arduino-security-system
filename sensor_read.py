import sys
import time
from pymata4 import pymata4
import mail_protocol

board = pymata4.Pymata4()
triggerPin = 10
echoPin = 11

def get_distance():
    board.set_pin_mode_sonar(triggerPin, echoPin)
    max_distance = 0;
    startTime = time.time()
    emailNotif = True

    #loops forever
    while True:
        time.sleep(0.2)
        print(board.sonar_read(triggerPin)[0], "cm")
        currentTime = time.time()

        #condition only executes for first 20 seconds of program execution
        if (currentTime - startTime < 15):
            if (board.sonar_read(triggerPin)[0] > max_distance):
                max_distance = board.sonar_read(triggerPin)[0]
            currentTime = time.time()

        elif ((max_distance - board.sonar_read(triggerPin)[0] >= 30) and emailNotif == True):
            print("MOVEMENT DETECTED. ALERT SENT.")
            mail_protocol.alert_email()
            emailNotif = False
            startTime = time.time()
            currentTime = time.time()
        
        elif (emailNotif == False):
            if (currentTime - startTime < 25):
                emailNotif = True
            currentTime = time.time()
            
print("The pymata4 library can be found at https://github.com/MrYsLab/pymata4 \nThe following code was developed by Nihal Sahu and Nishan Sivakumar\n")

get_distance()


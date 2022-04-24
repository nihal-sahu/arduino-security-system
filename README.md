# Smart Arduino Home Security System
## First place overall winner of Hoya Hacks 2022, DigiKey best hardware hack, and Pandemic year 2 social impact award
Check out the devpost submission here: https://devpost.com/software/arduino-security-system

![IMG_3116](https://user-images.githubusercontent.com/87585163/164988272-6008a59c-5d31-47a3-9d0a-7b9918a6f378.jpg)

## About the Project:
Smart Arduino Home Security System is exactly what it sounds like. It's a portable security system using a Raspberry Pi as the main computer system. When the sensors are tripped by unwanted intruders, an Arduino signal causes an immediate email to be sent by the Pi to an address of your choosing. 

We used PyFirmata libraries to interface between the Pi and Arduino, and an ultrasonic ranging module as the sensor. The sensor takes a few seconds to calibrate the distance between itself and the nearest wall, and reports and irregularities it finds while it is running. 

## How to set up:
### Step 1. Installing FirmataExpress to Arduino board (pymata4)
### Step 2. Download .zip file of repository main branch
### Step 3. Insert receiver email, and sender email and password into mail_protocol.py (this is needed to send the alerts) 
(don't worry, the password in the repo is just a dummy password)
### Step 3. Make "sensor_read.py" executable and run!
    chmod +x sensor_read.py
    python3 sensor_read.py
### Step 4. Stay safe friends, and make sure no one is going into your stuff!

## Sources: 
Credits to Alan Yorinks for the PyFirmata library: https://github.com/MrYsLab/pymata4

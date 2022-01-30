import time 
import smtplib
import ssl

def alert_email(receiver = "youremail@gmail.com"):
    # receiver needs to be passed in the beginning but we can pass a default parameter for now 
    port = 465 
    smtp_server = "smtp.gmail.com"
    sender = "alert6273@gmail.com" #enter your sender gmail here
    password = "1234%^&*ASdf" #enter your sender password of choice here
    receiving_email = receiver
    message = """Subject: Alarm Triggered!
        \n
        Hi,

        We would like to inform you that your sensors were just tripped. If this was not you, someone or something is in the vicinity of your room.

        Regards,
        Arduino Security System
    """

    #send mail protocol 
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print("SENSOR TRIGGERED - EMAIL SENT")
        server.login(sender, password)
        server.sendmail(sender, receiving_email, message)
    
    
import time 
import smtplib
import ssl

def alert_email(receiver = "nihi2003@gmail.com"):
    # receiver needs to be passed in the beginning but we can pass a default parameter for now 
    port = 465 
    smtp_server = "smtp.gmail.com"
    sender = "alert6273@gmail.com"
    password = "1234%^&*ASdf"
    receiving_email = receiver
    message = """Subject: Sensors Triggered!"""

    #send mail protocol 
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print("Sensor triggered - sending email")
        server.login(sender, password)
        server.sendmail(sender, receiving_email, message)
    
    
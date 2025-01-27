import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(sender, password, recipient, subject, body, attach):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(attach, 'rb') as file:
        msg.attach(MIMEApplication(file.read(), Name=attach.split("/")[-1]))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")
    print("Send sucessfully")




def send_notification():
    send_email(
    'diwashshrestha108@gmail.com', 
    'dadm qkme aosq upjq',  
    'adishjoshi56@gmail.com', 
    'Simple Email', 
    'Hello from Python!',
    "F:\Screenshot 2025-01-25 183156.png")
    
    print("This is your scheduled notification!")

# Schedule the notification every 10 seconds
schedule.every(1).seconds.do(send_notification)

print("Schedular started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
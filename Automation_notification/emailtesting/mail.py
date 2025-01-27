# pw : dadm qkme aosq upjq



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, recipient, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender, recipient, message)
        print("Email send sucessfully!!")
        


send_email(
    'diwashshrestha108@gmail.com', 
    'dadm qkme aosq upjq', 
    'bbhattarai770@gmail.com', 
    'Simple Email', 
    'Hello from Python!'
)
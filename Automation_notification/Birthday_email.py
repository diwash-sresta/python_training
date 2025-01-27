import csv
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# File path to the CSV containing birthday data
file_path = r"E:\python_training\Automation_notification\Birthday_date.csv"

# Function to send email
def send_email(sender, password, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
            print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

# Function to check birthdays and send wishes
def check_and_send_birthday_wishes():
    today = datetime.now().strftime("%m-%d")  # Current date in MM-DD format
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                birthday = row['Birthday']
                email = row['Email']

                # Match today's date with the birthday
                if today == datetime.strptime(birthday, "%Y-%m-%d").strftime("%m-%d"):
                    subject = f"Happy Birthday, {name}!"
                    body = f"Hi {name},\n\nWishing you a fantastic birthday! 🎉\n\nBest Regards,\nYour Friend"
                    send_email('diwashshrestha108@gmail.com', 'dadm qkme aosq upjq', email, subject, body)
    except Exception as e:
        print(f"Error processing the file: {e}")

# Main execution
if __name__ == "__main__":
    print("Checking for birthdays...")
    check_and_send_birthday_wishes()




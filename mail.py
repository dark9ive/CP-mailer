import sys
import smtplib
from email.mime.text import MIMEText
from constant import EMAIL_ADDR, EMAIL_KEY, SENDER_NAME, SENDER, SMTP_SERVER, SMTP_PORT

smtp_server = None

def mail_init():
    global smtp_server
    smtp_server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp_server.login(EMAIL_ADDR, EMAIL_KEY)

def send_email(subject, body, recipient):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = recipient
    
    if smtp_server is None:
        mail_init()

    try:
        smtp_server.sendmail(SENDER, recipient, msg.as_string())
        print(f"Mail send to {recipient} successfully!", file=sys.stderr)
    except Exception as e:
        print(f"Failed to send mail to {recipient}. error: {e}")
        

def self_test():
    send_email("TEST.", "This is a self python SMTP test.", EMAIL_ADDR)

if __name__ == "__main__":
    self_test()

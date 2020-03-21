import smtplib
from email.mime.text import MIMEText

from config import USERNAME, PASSWORD

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = "smtp.mailtrap.io"

    # credentials from mailtrap.io
    login = USERNAME
    password = PASSWORD

    # message of the email
    message = f"<h3>Feedback</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comment: {comments}</li></ul>"

    # set up the content of the email
    sender_email = "wriboat1@mail.com"
    receiver_email = "wriboat2@mail.com"
    msg = MIMEText(message, "html")
    msg["Subject"] = "WRIboat Feedback"
    msg["From"] = sender_email
    msg["To"] = receiver_email
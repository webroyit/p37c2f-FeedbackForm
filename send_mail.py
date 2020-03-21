import smtplib
from email.mime.text import MINEText

from config import USERNAME, PASSWORD

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = "smtp.mailtrap.io"

    # credentials from mailtrap.io
    login = USERNAME
    password = PASSWORD
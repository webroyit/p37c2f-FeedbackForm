import smtplib
from email.mime.text import MINEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = "smtp.mailtrap.io"
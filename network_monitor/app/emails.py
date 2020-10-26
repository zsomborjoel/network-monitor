import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .logs import add_to_log


def send_mail(fromaddr, toaddr, subject, password, text):
    """
    :param fromaddr: string
    :param toaddr: string
    :param subject: string
    :param password: string
    :return: None
    """

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = subject

    # string to store the body of the mail
    body = "Warning! Unknown devices on the network: \n " + text

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

    add_to_log('Email sent successfully')

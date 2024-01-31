from email.message import EmailMessage
import smtplib


def create_message(email_name, subject, content_message):
    """
    This function takes three arguments email_name, subject,
    content_message, and then it return a message object.
    """

    message = EmailMessage()
    message["From"] = email_name
    message["To"] = email_name
    message["Subject"] = subject
    message.set_content(content_message)
    return message

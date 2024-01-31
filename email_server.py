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

def login_server(email_name, email_pass):
    """
    The function takes two arguments email_name and email_pass,
    and it tries to log in to GMAIL smtp server, if it succeeds
    then it return the mail_server otherwise returns False.
    """

    try:
        mail_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        mail_server.set_debuglevel(1)
        mail_server.login(email_name, email_pass)
        return mail_server
    except:
        return False

def send_message(email_name, email_pass, message):
    """
    This function takes three arguments email_name, email_pass,
    message, then it call the login_server() function with email name and
    password as arguments to log in, and by using send_message() method
    with message as argument from server_response object to send the message,
    and finally return True if it succeeds otherwise False.
    """

    try:
        server_response = login_server(email_name, email_pass)
        server_response.send_message(message)
        server_response.quit()
        return True
    except:
        return False
from gui import App
from email_server import *
from tkinter import *
from tkinter.messagebox import showinfo
from web_scraper import *
import time


def validate_product_item():
    """
    This function validates the product item
    name entry from gui module.
    """

    product_item = app.product_entry.get().lower()
    if len(product_item) == 0:
        app.label_product_error.config(text="*Enter the product name")
    else:
        app.label_product_error.config(text="")
        return True

def validate_price():
    """
    This function validates the product item
    price entry from gui module,
    it makes the entry accept only float data.
    """

    price = app.price_entry.get()
    if len(price) == 0:
        app.label_price_error.config(text="*Enter Max Price")
    else:
        try:
            float(app.price_entry.get())
            app.label_price_error.config(text="")
            return True
        except:
            app.label_price_error.config(text="*Invalid Input")

def validate_email():
    """
    This function validates the email entry from gui module,
    it checks if in the entered email is present the word @gmail.
    """

    email = app.email_entry.get().lower()
    if len(email) == 0:
        app.label_email_error.config(text="*Enter the email")
    else:
        if "@gmail" not in app.email_entry.get().lower():
            app.email_entry.get().lower()
            app.label_email_error.config(text="*Enter a valid GMAIL account")
        else:
            app.label_email_error.config(text="")
            return True

def validate_password():
    """
    This function validates the email password
    entry from gui module.
    """

    password = app.password_entry.get().lower()
    if len(password) == 0:
        app.label_password_error.config(text="*Enter the password")
    else:
        app.label_password_error.config(text="")
        return True

def start_process():
    pass

if __name__ == "__main__":
    app = App(start_process)
    app.mainloop()
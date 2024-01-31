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

def popup_window(message):
    """
    This function creates a popup window.
    """

    pop = Toplevel()
    pop.grab_set()
    pop.configure(bg="#131921")
    pop.resizable(False, False)
    pop.overrideredirect(True)
    pop_label = Label(pop, text=message, font="Italic 14", bg="#131921", fg="white")
    pop_label.pack(pady=10, padx=10)
    pop_button = Button(pop, text="OK",
                        background="#232f3e",
                        foreground="white",
                        activebackground="#283f5b",
                        activeforeground="white",
                        highlightcolor='red',
                        width=8,
                        font="Italic 16",
                        command=pop.destroy)
    pop_button.pack(pady=30)
    pop.update_idletasks()
    posx = str((pop.winfo_screenwidth() // 2) - (pop.winfo_width() // 2))
    posy = str((pop.winfo_screenheight() // 2) - (pop.winfo_height() // 2))
    pop.geometry(f"{pop.winfo_width()}x{pop.winfo_height()}+{posx}+{posy}")

def start_process():
    """
    This is the main function when the button start is clicked
    first it validates all entries after that it enter in a while loop and tries to connect
    to the specified gmail account if it can't a popup message appear,
    otherwise the main window are hide and an icon appear in system tray bar,
    now it try to search the specified product if it returns False
    then a popup is called and a message appear, otherwise it continue
    searching for the specified product name and price it returns
    the data and tries to send them to the specified email,
    otherwise it tries again after 30 minutes.
    """

    if all((validate_product_item(), validate_price(), validate_email(), validate_password())):
        app.system_tray_window()
        while True:
            product_item = app.product_entry.get()
            product_price = float(app.price_entry.get())
            email_name = app.email_entry.get()
            email_pass = app.password_entry.get()
            login = login_server(email_name, email_pass)
            if login:
                if check_server_availability(product_item):
                    data = search_item(product_price, product_item)
                    if data != False:
                        if data != {}:
                            fstring_message = "Hi here are all the products less or egual to the specified Price:\n\n"
                            for k, v in data.items():
                                fstring_message += v[0] + "\n" + k + "\n" + "Price: " + v[1] + "\n" + "Amazon Page: " + v[2] + "\n\n"
                            message = create_message(email_name,
                                                 "Amazon Notifier Price Go Down",
                                                 fstring_message)
                            send_message(email_name, email_pass, message)
                            break
                    else:
                        popup_window(f"No Results for {product_item}")
                        break
                else:
                    popup_window("Amazon Server Not Available!")
                    break
            else:
                popup_window("Can't connect to Gmail,\n check your email and password!")
                break
            time.sleep(60)

if __name__ == "__main__":
    app = App(start_process)
    app.mainloop()
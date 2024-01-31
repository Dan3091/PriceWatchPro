from tkinter import *
from PIL import Image
from pystray import MenuItem as item
import pystray


class App(Tk):
    """
    This class is used to define the main window by using tkinter graphic interface module.
    """

    def __init__(self, start_process):
        self.start_process = start_process

        super().__init__()
        self.title("PriceWatchPro")
        self.resizable(False, False)
        self.configure(bg="#131921")
        self.overrideredirect(True)

        # Calculation of the main window position
        posx = str(self.winfo_screenwidth() // 2 - 300 // 2)
        posy = str(self.winfo_screenheight() // 2 - 530 // 2)
        self.geometry(f"300x530+{posx}+{posy}")

        # Label App Name and Canvas
        label_title = Label(self,
                            text="PriceWatchPro",
                            font="Italic 18",
                            bg="#131921",
                            fg="white")
        label_title.pack()
        canvas = Canvas(self,
                        width=280,
                        height=5,
                        bg="#ff9900",
                        highlightthickness=0)
        canvas.pack()

        # Added all necessary labels and entries
        self.label_product = Label(self,
                                   text="Product Item Name:",
                                   font="Italic 14",
                                   bg="#131921",
                                   fg="white")
        self.label_product.pack(pady=(20, 0))
        self.label_product_error = Label(self,
                                         text="",
                                         font="Italic 10",
                                         bg="#131921",
                                         fg="red")
        self.label_product_error.pack()
        self.product_entry = Entry(self, font="Italic 14", bg="#232f3e", fg="white")
        self.product_entry.pack()

        self.label_price = Label(self,
                                 text="Max Price:",
                                 font="Italic 14",
                                 bg="#131921",
                                 fg="white")
        self.label_price.pack()
        self.label_price_error = Label(self,
                                       text="",
                                       font="Italic 10",
                                       bg="#131921",
                                       fg="red")
        self.label_price_error.pack()
        self.price_entry = Entry(self, font="Italic 14", bg="#232f3e", fg="white")
        self.price_entry.pack()

        self.label_subtitle = Label(self,
                                    text="Now  enter your email credencial\n to receive the notification:",
                                    font="Italic 12",
                                    bg="#131921",
                                    fg="white")
        self.label_subtitle.pack(pady=(20, 10))

        self.label_email = Label(self,
                                 text="Email:",
                                 font="Italic 14",
                                 bg="#131921",
                                 fg="white")
        self.label_email.pack()
        self.label_email_error = Label(self,
                                       text="",
                                       font="Italic 10",
                                       bg="#131921",
                                       fg="red")
        self.label_email_error.pack()
        self.email_entry = Entry(self, font="Italic 14", bg="#232f3e", fg="white")
        self.email_entry.pack()

        self.label_password = Label(self,
                                    text="Password:",
                                    font="Italic 14",
                                    bg="#131921",
                                    fg="white")
        self.label_password.pack()
        self.label_password_error = Label(self,
                                          text="",
                                          font="Italic 10",
                                          bg="#131921",
                                          fg="red")
        self.label_password_error.pack()
        self.password_entry = Entry(self, font="Italic 14", bg="#232f3e", fg="white", show="*")
        self.password_entry.pack()
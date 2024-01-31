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

        # Created two buttons start_btn and quit_btn
        self.start_btn = Button(self,
                                text='Start',
                                background="#232f3e",
                                foreground="white",
                                activebackground="#283f5b",
                                activeforeground="white",
                                highlightcolor='red',
                                width=8,
                                font="Italic 16",
                                command=self.start_process)
        self.start_btn.place(x=38, y=470)
        self.quit_btn = Button(self,
                               text='Quit',
                               background="#232f3e",
                               foreground="white",
                               activebackground="#283f5b",
                               activeforeground="white",
                               highlightcolor='red',
                               width=8,
                               font="Italic 16",
                               command=self.destroy)
        self.quit_btn.place(x=157, y=470)

    # Create a system to minimize the window to system tray bar
    def show_window(self, icon, item):
        """
        This function quit the icon from system tray bar,
        and call the self.deiconify() function
        that make the main window appear.
        """

        icon.stop()
        self.after(0, self.deiconify())

    def quit_window(self, icon, item):
        """
        Instead of the previous function this one
        quit the icon from system tray bar and
        destroy the main window.
        """

        icon.stop()
        self.destroy()

    def system_tray_window(self):
        """
        This function hide the main window and creates
        a system tray icon with a menu Show, Quit buttons,
        then it run in a detached mode.
        """

        self.withdraw()
        image = Image.open("favicon.ico")
        menu = item("Quit", self.quit_window), item("Show", self.show_window)
        icon = pystray.Icon("name", image, "My System Tray Icon", menu)
        icon.run_detached()



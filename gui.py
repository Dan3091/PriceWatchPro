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



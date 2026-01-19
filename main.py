import customtkinter as ctk
from config.settings import *

pantalla = MainView()
pantalla.title(APP_NAME)
pantalla.geometry(WINDOW_SIZE)
pantalla.mainloop()
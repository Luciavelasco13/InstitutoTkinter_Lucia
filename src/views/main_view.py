import customtkinter as ctk

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._crear_interfaz()

    def _crear_interfaz(self):
        label = ctk.CTkLabel(
            self,
            text="HOLA",
            font=("Arial", 48, "bold")
        )
        label.pack(expand=True)
import tkinter as tk
from tkinter import ttk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class RestauranteApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Restaurante App")
        self.root.geometry("1000x650")
        self.root.minsize(850, 550)

        self.servicio = RestauranteServicio()

        self.mostrar_login()

    def limpiar_ventana(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):

        self.limpiar_ventana()

        login = LoginView(
            self.root,
            self.servicio,
            self.login_exitoso
        )

        login.pack(
            fill="both",
            expand=True
        )

    def login_exitoso(self, usuario):

        self.limpiar_ventana()

        main_view = MainView(
            self.root,
            self.servicio,
            usuario,
            self.mostrar_login
        )

        main_view.pack(
            fill="both",
            expand=True
        )

def main():

    root = tk.Tk()

    style = ttk.Style()

    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    app = RestauranteApp(root)

    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(ttk.Frame):

    def __init__(self, parent, servicio, on_login_success):
        super().__init__(parent)

        self.servicio = servicio
        self.on_login_success = on_login_success

        self.usuario_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        contenedor = ttk.Frame(self, padding=40)
        contenedor.pack(expand=True)

        titulo = ttk.Label(
            contenedor,
            text="Restaurante App",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=(0, 10))

        subtitulo = ttk.Label(
            contenedor,
            text="Inicio de sesión",
            font=("Arial", 12)
        )
        subtitulo.pack(pady=(0, 25))

        formulario = ttk.LabelFrame(
            contenedor,
            text="Acceso al sistema",
            padding=20
        )
        formulario.pack()

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=8
        )

        usuario_entry = ttk.Entry(
            formulario,
            textvariable=self.usuario_var,
            width=30
        )
        usuario_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=8
        )

        ttk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=8
        )

        password_entry = ttk.Entry(
            formulario,
            textvariable=self.password_var,
            show="*",
            width=30
        )
        password_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=8
        )

        boton = ttk.Button(
            formulario,
            text="Iniciar sesión",
            command=self.iniciar_sesion
        )
        boton.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=(20, 5)
        )

        password_entry.bind(
            "<Return>",
            lambda event: self.iniciar_sesion()
        )
        usuario_entry.focus()

    def iniciar_sesion(self):
        usuario = self.usuario_var.get()
        password = self.password_var.get()

        user = self.servicio.autenticar_usuario(
            usuario,
            password
        )

        if user:
            self.on_login_success(user)
        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )

import tkinter as tk
from tkinter import ttk, messagebox

class MainView(ttk.Frame):

    def __init__(self, parent, servicio, usuario_actual, on_logout):
        super().__init__(parent)

        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout

        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.stock_var = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.crear_encabezado()
        self.crear_navegacion()

        self.contenido = ttk.Frame(self, padding=15)
        self.contenido.grid(
            row=2,
            column=0,
            sticky="nsew"
        )

        self.contenido.columnconfigure(0, weight=1)
        self.contenido.rowconfigure(0, weight=1)

        self.mostrar_productos()

    def crear_encabezado(self):

        encabezado = ttk.Frame(
            self,
            padding=(20, 15)
        )

        encabezado.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        encabezado.columnconfigure(0, weight=1)

        titulo = ttk.Label(
            encabezado,
            text="Restaurante App",
            font=("Arial", 20, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            sticky="w"
        )

        nombre_usuario = ttk.Label(
            encabezado,
            text=f"Usuario: {self.usuario_actual.nombre}"
        )

        nombre_usuario.grid(
            row=0,
            column=1,
            padx=10
        )

    def crear_navegacion(self):

        navegacion = ttk.Frame(
            self,
            padding=(15, 8)
        )

        navegacion.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        ttk.Button(
            navegacion,
            text="Productos",
            command=self.mostrar_productos
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            navegacion,
            text="Usuarios",
            command=self.mostrar_usuarios
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            navegacion,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        ).pack(
            side="right",
            padx=5
        )

    def mostrar_productos(self):

        self.limpiar_contenido()

        titulo = ttk.Label(
            self.contenido,
            text="Gestión de Productos",
            font=("Arial", 16, "bold")
        )

        titulo.pack(
            anchor="w",
            pady=(0, 10)
        )

        cuerpo = ttk.Frame(self.contenido)
        cuerpo.pack(
            fill="both",
            expand=True
        )

        cuerpo.columnconfigure(1, weight=1)
        cuerpo.rowconfigure(0, weight=1)

        self.crear_formulario_producto(cuerpo)

        self.crear_tabla_productos(cuerpo)

        self.cargar_tabla_productos()

    def crear_formulario_producto(self, parent):

        formulario = ttk.LabelFrame(
            parent,
            text="Datos del producto",
            padding=15
        )

        formulario.grid(
            row=0,
            column=0,
            sticky="ns",
            padx=(0, 15)
        )

        ttk.Label(
            formulario,
            text="Código:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=5
        )

        ttk.Entry(
            formulario,
            textvariable=self.codigo_var,
            width=25
        ).grid(
            row=1,
            column=0,
            pady=(0, 10)
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=5
        )

        ttk.Entry(
            formulario,
            textvariable=self.nombre_var,
            width=25
        ).grid(
            row=3,
            column=0,
            pady=(0, 10)
        )

        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=4,
            column=0,
            sticky="w",
            pady=5
        )

        ttk.Entry(
            formulario,
            textvariable=self.categoria_var,
            width=25
        ).grid(
            row=5,
            column=0,
            pady=(0, 10)
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=6,
            column=0,
            sticky="w",
            pady=5
        )

        ttk.Entry(
            formulario,
            textvariable=self.precio_var,
            width=25
        ).grid(
            row=7,
            column=0,
            pady=(0, 10)
        )

        ttk.Label(
            formulario,
            text="Stock:"
        ).grid(
            row=8,
            column=0,
            sticky="w",
            pady=5
        )

        ttk.Entry(
            formulario,
            textvariable=self.stock_var,
            width=25
        ).grid(
            row=9,
            column=0,
            pady=(0, 10)
        )

        ttk.Button(
            formulario,
            text="Registrar",
            command=self.registrar_producto
        ).grid(
            row=10,
            column=0,
            sticky="ew",
            pady=4
        )

        ttk.Button(
            formulario,
            text="Actualizar",
            command=self.actualizar_producto
        ).grid(
            row=11,
            column=0,
            sticky="ew",
            pady=4
        )

        ttk.Button(
            formulario,
            text="Eliminar",
            command=self.eliminar_producto
        ).grid(
            row=12,
            column=0,
            sticky="ew",
            pady=4
        )

        ttk.Button(
            formulario,
            text="Limpiar",
            command=self.limpiar_formulario
        ).grid(
            row=13,
            column=0,
            sticky="ew",
            pady=4
        )

    def crear_tabla_productos(self, parent):

        contenedor = ttk.LabelFrame(
            parent,
            text="Productos registrados",
            padding=10
        )

        contenedor.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        contenedor.columnconfigure(0, weight=1)
        contenedor.rowconfigure(0, weight=1)

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings"
        )

        self.tabla_productos.heading(
            "codigo",
            text="Código"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_productos.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.heading(
            "stock",
            text="Stock"
        )

        self.tabla_productos.column(
            "codigo",
            width=90
        )

        self.tabla_productos.column(
            "nombre",
            width=180
        )

        self.tabla_productos.column(
            "categoria",
            width=130
        )

        self.tabla_productos.column(
            "precio",
            width=90
        )

        self.tabla_productos.column(
            "stock",
            width=80
        )

        self.tabla_productos.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar = ttk.Scrollbar(
            contenedor,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_productos.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_producto
        )

    def cargar_tabla_productos(self):

        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = self.servicio.obtener_productos()

        for producto in productos:

            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"{producto.precio:.2f}",
                    producto.stock
                )
            )

    def registrar_producto(self):

        exito, mensaje = self.servicio.registrar_producto(
            self.codigo_var.get(),
            self.nombre_var.get(),
            self.categoria_var.get(),
            self.precio_var.get(),
            self.stock_var.get()
        )

        if exito:
            messagebox.showinfo(
                "Registro",
                mensaje
            )

            self.cargar_tabla_productos()
            self.limpiar_formulario()

        else:
            messagebox.showerror(
                "Error",
                mensaje
            )

    def actualizar_producto(self):

        exito, mensaje = self.servicio.actualizar_producto(
            self.codigo_var.get(),
            self.nombre_var.get(),
            self.categoria_var.get(),
            self.precio_var.get(),
            self.stock_var.get()
        )

        if exito:
            messagebox.showinfo(
                "Actualización",
                mensaje
            )

            self.cargar_tabla_productos()
            self.limpiar_formulario()

        else:
            messagebox.showerror(
                "Error",
                mensaje
            )

    def eliminar_producto(self):

        codigo = self.codigo_var.get()

        if not codigo.strip():
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un producto para eliminar"
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar este producto?"
        )

        if not confirmar:
            return

        exito, mensaje = self.servicio.eliminar_producto(
            codigo
        )

        if exito:
            messagebox.showinfo(
                "Eliminación",
                mensaje
            )

            self.cargar_tabla_productos()
            self.limpiar_formulario()

        else:
            messagebox.showerror(
                "Error",
                mensaje
            )

    def seleccionar_producto(self, event):

        seleccion = self.tabla_productos.selection()

        if not seleccion:
            return

        valores = self.tabla_productos.item(
            seleccion[0],
            "values"
        )

        self.codigo_var.set(valores[0])
        self.nombre_var.set(valores[1])
        self.categoria_var.set(valores[2])
        self.precio_var.set(valores[3])
        self.stock_var.set(valores[4])

    def limpiar_formulario(self):

        self.codigo_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")

        if hasattr(self, "tabla_productos"):
            seleccion = self.tabla_productos.selection()

            if seleccion:
                self.tabla_productos.selection_remove(
                    *seleccion
                )

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        titulo = ttk.Label(
            self.contenido,
            text="Usuarios registrados",
            font=("Arial", 16, "bold")
        )

        titulo.pack(
            anchor="w",
            pady=(0, 10)
        )

        contenedor = ttk.Frame(
            self.contenido,
            padding=10
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        contenedor.columnconfigure(0, weight=1)
        contenedor.rowconfigure(0, weight=1)

        columnas = (
            "identificacion",
            "nombre",
            "usuario"
        )

        tabla = ttk.Treeview(
            contenedor,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "identificacion",
            text="Identificación"
        )

        tabla.heading(
            "nombre",
            text="Nombre"
        )

        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.column(
            "identificacion",
            width=150
        )

        tabla.column(
            "nombre",
            width=250
        )

        tabla.column(
            "usuario",
            width=150
        )

        tabla.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar = ttk.Scrollbar(
            contenedor,
            orient="vertical",
            command=tabla.yview
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        tabla.configure(
            yscrollcommand=scrollbar.set
        )

        usuarios = self.servicio.obtener_usuarios()

        for usuario in usuarios:

            tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():
            widget.destroy()

    def cerrar_sesion(self):

        confirmar = messagebox.askyesno(
            "Cerrar sesión",
            "¿Seguro de cerrar sesión?"
        )

        if confirmar:
            self.on_logout()

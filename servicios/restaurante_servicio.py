import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:

    def __init__(self):
        self.archivo_servicio = ArchivoServicio()

        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.ruta_productos = os.path.join(
            base_dir,
            "datos",
            "productos.json"
        )

        self.ruta_usuarios = os.path.join(
            base_dir,
            "datos",
            "usuarios.json"
        )

        self.productos = []
        self.usuarios = []

        self.cargar_productos()
        self.cargar_usuarios()

    def cargar_productos(self):
        datos = self.archivo_servicio.leer_json(
            self.ruta_productos
        )

        self.productos = [
            Producto.from_dict(item)
            for item in datos
        ]

    def guardar_productos(self):
        datos = [
            producto.to_dict()
            for producto in self.productos
        ]

        self.archivo_servicio.escribir_json(
            self.ruta_productos,
            datos
        )

    def obtener_productos(self):
        return self.productos.copy()

    def buscar_producto(self, codigo):
        codigo = str(codigo).strip()

        for producto in self.productos:
            if str(producto.codigo) == codigo:
                return producto

        return None

    def registrar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):
        codigo = str(codigo).strip()
        nombre = str(nombre).strip()
        categoria = str(categoria).strip()

        if not codigo:
            return False, "El código es obligatorio"

        if not nombre:
            return False, "El nombre es obligatorio"

        if not categoria:
            return False, "La categoría es obligatoria"

        if self.buscar_producto(codigo):
            return False, "Ya existe un producto con ese código"

        try:
            precio = float(precio)
        except ValueError:
            return False, "El precio debe ser numérico"

        try:
            stock = int(stock)
        except ValueError:
            return False, "El stock debe ser un número entero"

        if precio < 0:
            return False, "El precio no puede ser negativo"

        if stock < 0:
            return False, "El stock no puede ser negativo"

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self.productos.append(producto)
        self.guardar_productos()

        return True, "Producto registrado correctamente"

    def actualizar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):
        codigo = str(codigo).strip()

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "No se encontró el producto"

        nombre = str(nombre).strip()
        categoria = str(categoria).strip()

        if not nombre:
            return False, "El nombre es obligatorio"

        if not categoria:
            return False, "La categoría es obligatoria"

        try:
            precio = float(precio)
        except ValueError:
            return False, "El precio debe ser numérico"

        try:
            stock = int(stock)
        except ValueError:
            return False, "El stock debe ser un número entero"

        if precio < 0:
            return False, "El precio no puede ser negativo"

        if stock < 0:
            return False, "El stock no puede ser negativo"

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock

        self.guardar_productos()

        return True, "Producto actualizado correctamente"

    def eliminar_producto(self, codigo):
        codigo = str(codigo).strip()

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "No se encontró el producto"

        self.productos.remove(producto)

        self.guardar_productos()

        return True, "Producto eliminado correctamente"

    def cargar_usuarios(self):
        datos = self.archivo_servicio.leer_json(
            self.ruta_usuarios
        )

        self.usuarios = [
            Usuario.from_dict(item)
            for item in datos
        ]

    def obtener_usuarios(self):
        return self.usuarios.copy()

    def autenticar_usuario(self, usuario, password):
        usuario = str(usuario).strip()
        password = str(password)

        for user in self.usuarios:
            if (
                user.usuario == usuario
                and user.password == password
            ):
                return user
        return None

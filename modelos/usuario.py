class Usuario:
    def __init__(self, identificacion, nombre, usuario, password):
        self.identificacion = identificacion
        self.nombre = nombre
        self.usuario = usuario
        self.password = password

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            data["identificacion"],
            data["nombre"],
            data["usuario"],
            data["password"]
        )

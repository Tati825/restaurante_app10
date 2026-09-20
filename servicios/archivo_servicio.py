import json
import os

class ArchivoServicio:

    def leer_json(self, ruta):
        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, OSError):
            return []

    def escribir_json(self, ruta, datos):
        directorio = os.path.dirname(ruta)

        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

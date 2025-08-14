class Personaje:
    def __init__(self, nombre, dialogo):
        self.nombre = nombre
        self.dialogo = dialogo

    def hablar(self):
        return f"{self.nombre}: {self.dialogo}"
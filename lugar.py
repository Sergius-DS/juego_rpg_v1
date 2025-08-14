class Lugar:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetos = []
        self.personajes = []
        self.conexiones = {}

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def quitar_objeto(self, nombre_objeto):
        for objeto in self.objetos:
            if objeto.nombre.lower() == nombre_objeto.lower():
                self.objetos.remove(objeto)
                return objeto
        return None 
    
    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)

    def conectar(self, direccion, lugar):
        self.conexiones[direccion] = lugar 
        

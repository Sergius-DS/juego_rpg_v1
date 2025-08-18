class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.inventario = []
        self.lugar_actual = None 

    def recoger_objeto(self, nombre_objeto):
        objeto = self.lugar_actual.quitar_objeto(nombre_objeto)
        if objeto:
            self.inventario.append(objeto)
            if objeto.emoji:
                return f"Has recogido: {objeto.emoji} {objeto.nombre}"
            else:
                return f"Has recogido: {objeto.nombre}"
        return f"Non hay ningún '{nombre_objeto}' aquí"
    
    def mostrar_inventario(self):
        if not self.inventario:
            return "Tu inventario está vacío"
        items = [obj.nombre for obj in self.inventario]
        return f"Inventario: {', '.join(items)}"
    
    def mover(self, direccion):
        if direccion in self.lugar_actual.conexiones:
            self.lugar_actual = self.lugar_actual.conexiones[direccion]
            return f"Te has movido a: {self.lugar_actual.nombre}"
        return "No puedes ir en esta dirección"
    

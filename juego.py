from lugar import Lugar 
from objeto import Objeto
from personaje import Personaje 
from jugador import Jugador 
import flet as ft 

class Juego:
    def __init__(self):
        self.jugador = None 
        self.lugares = {}
        self.inicializar_mundo()

    def inicializar_mundo(self):
        entrada = Lugar("Entrada del Bosque", "Una clara entrada a un misterioso bosque")
        bosque = Lugar("Bosque Profundo", "Un bosque denso lleno de sombras")
        cueva = Lugar("Cueva Misteriosa", "Una cueva oscura con ecos extraños")
        aldea = Lugar("Aldea Pacífica", "Una pequeña aldea con casas de madera")

        espada = Objeto("espada", "Una espada brillante de acero")
        pocion = Objeto("poción", "una poción de curación de colro verde")
        llave = Objeto("llave", "Una llave antigua y misteriosa")

        goblin = Personaje("Goblin", "Grr! No pases por aquí, humano!")
        aldeano = Personaje("Aldeano", "Bienvenido a nuestra humilde aldea")

        # Agregar objetos a los lugares
        entrada.agregar_objeto(espada)
        bosque.agregar_objeto(pocion)
        cueva.agregar_objeto(llave)

        # Agregar personajes a lugares
        bosque.agregar_personaje(goblin)
        aldea.agregar_personaje(aldeano)

        # Conectar lugares
        entrada.conectar("norte", bosque)
        bosque.conectar("sur", entrada)
        bosque.conectar("este", cueva)
        bosque.conectar("oeste", aldea)

        cueva.conectar("oeste", bosque)
        aldea.conectar("este", bosque)

        # Guardar lugares
        self.lugares = {
            "entrada": entrada,
            "bosque": bosque,
            "cueva": cueva,
            "aldea": aldea
        }

        # Cread jugador
        self.jugador = Jugador("Aventurero")
        self.jugador.lugar_actual = entrada 

    def procesar_comando(self,comando):
        comando = comando.lower().strip()

        if comando.startswith("ir "):
            direccion = comando[3:]
            return self.jugador.mover(direccion)
        
        elif comando.startswith("recoger "):
            objeto = comando[8:]
            return self.jugador.recoger_objeto(objeto)

        elif comando.startswith("hablar "):
            nombre = comando[7:]
            for personaje in self.jugador.lugar_actual.personajes:
                if personaje.nombre.lower() == nombre.lower():
                    return personaje.hablar()
            return f"No hay ningún '{nombre}' aquí"
        
        elif comando == "inventario":
            return self.jugador.mostrar_inventario()
        
        elif comando == "mirar":
            lugar = self.jugador.lugar_actual
            info = f"🏞️ {lugar.nombre}\n{lugar.descripcion}\n"
            
            if lugar.objetos:
                objetos = [obj.nombre for obj in lugar.objetos]
                info += f"Objetos: {', '.join(objetos)}\n"

            if lugar.personajes:
                personajes = [p.nombre for p in lugar.personajes]
                info += f"Personajes: {', '.join(personajes)}\n"

            direcciones = list(lugar.conexiones.keys())
            if direcciones:
                info += f"Salidas: {', '.join(direcciones)}"
            return info 
        
        else:
            return "Comando no reconocido. Usar: ir [direccion], recoger [objeto], hablar [personaje], inventario, mirar"
    
def main(page: ft.Page):
    page.title = "🕹️ RPG Adventure Game"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False

    # Crear instancia del juego
    juego = Juego()

    # Componentes de la UI
    output_text = ft.Text(
        value = " Bienvenido al RPG Adventure!\n\nEscribe 'mirar' para observar tu entorno.\nComandos disponibles: ir [dirección], recoger [objeto], hablar [personaje], inventario, mirar",
        size = 14,
        selectable = True,
        width = 750,
        color = ft.Colors.GREEN_300
    )
    input_field = ft.TextField(
        hint_text = "Escribe tu comando aquí...",
        width = 600,
        autofocus = True,
        text_size = 14
    )

    def ejecutar_comando(e):
        comando = input_field.value.strip()
        if comando:
            resultado = juego.procesar_comando(comando)
            output_text.value += f"\n\n> {comando}\n{resultado}"
            input_field.value = ""
            page.update()

    def on_key_down(e):
        if e.key == "Enter":
            ejecutar_comando(e)

    input_field.on_submit = ejecutar_comando
    page.on_keyboard_event = on_key_down

    execute_button = ft.ElevatedButton(
        text = "Ejecutar",
        on_click = ejecutar_comando,
        height = 40
    )

    def limpiar_pantalla(e):
        output_text.value = "Pantalla limpiada. Escriber 'mirar' para ver tu entorno."
        page.update()
    
    clear_button = ft.ElevatedButton(
        text = "Limpiar",
        on_click = limpiar_pantalla,
        height = 40,
        color = ft.Colors.RED_300
    )
    # Layout de la interfaz
    page.add(
        ft.Container(
            content = ft.Column([
                ft.Text("🕹️ RPG ADVENTURE GAME", size = 24, weight = ft.FontWeight.BOLD, color = ft.Colors.BLUE_300),
                ft.Divider(),
                ft.Container(
                    content = output_text,
                    bgcolor = ft.Colors.GREY_900,
                    padding = 15,
                    border_radius = 10,
                    height = 350,
                    border = ft.border.all(2, ft.Colors.BLUE_300)

                ),
                ft.Row([
                    input_field,
                    execute_button,
                    clear_button],
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Text(" Tip: Usa 'mirar' para explorar, 'ir [dirección]', para moverte",
                        size = 12, color = ft.Colors.GREY_400)
        ], spacing = 10),
        padding = 20
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
        
            



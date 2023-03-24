import arcade
from random import randint
import time

class Juego(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title, fullscreen=True)
        arcade.set_background_color(arcade.color.EERIE_BLACK)

        self.vegetacion_ubicacion=[]
        self.start_time=time.time()

    def iniciar_pantalla(self):
        arcade.draw_text("Winter", 850, 985, arcade.color.AQUA, 50)
        arcade.draw_rectangle_filled(960, 640, 1920, 600, arcade.color.WHITE)

    def draw_vegetacion(self,cantidad=10):
        vegetacion = 0
        while vegetacion <= cantidad :
            print(f"vegetacion = {vegetacion}")
            punto_y=randint(380,900)
            punto_x=randint(00,1900)
            vegetacion += 1
            self.vegetacion_ubicacion.append((punto_x,punto_y))
            arcade.draw_rectangle_filled(punto_x, punto_y, 30, 60, arcade.color.GREEN)

    def eliminar_vegetacion(self):
        pass

    def on_update(self,delta_time):
        print(delta_time)



pantalla=Juego(1920,1080, 'Evolutron')
arcade.start_render()
pantalla.iniciar_pantalla()
pantalla.draw_vegetacion(40)
print(pantalla.vegetacion_ubicacion)
arcade.finish_render()
arcade.run()
        
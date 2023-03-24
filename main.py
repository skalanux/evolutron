import arcade
from random import randint

class Juego(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title, fullscreen=True)
        arcade.set_background_color(arcade.color.EERIE_BLACK)

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
            arcade.draw_rectangle_filled(punto_x, punto_y, 30, 60, arcade.color.GREEN)



pantalla=Juego(1920,1080, 'Evolutron')
arcade.start_render()
pantalla.iniciar_pantalla()
pantalla.draw_vegetacion(600)
arcade.finish_render()
arcade.run()
        
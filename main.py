import arcade

class Juego(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title, fullscreen=True)
        arcade.set_background_color(arcade.color.EERIE_BLACK)

    def iniciar_pantalla(self):
        arcade.start_render()
        arcade.draw_text("Winter", 850, 985, arcade.color.AQUA, 50)
        arcade.draw_rectangle_filled(960, 640, 1920, 600, arcade.color.WHITE)
        arcade.finish_render()




pantalla=Juego(1920,1080, 'Evolutron')
pantalla.iniciar_pantalla()
arcade.run()
        
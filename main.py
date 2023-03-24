import arcade

class Juego(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title, fullscreen=True)
        arcade.set_background_color(arcade.color.EERIE_BLACK)

    def iniciar_pantalla(self):
        arcade.start_render()
        arcade.draw_text("draw_filled_rect", 363, 3, arcade.color.WHITE, 10)
        arcade.draw_rectangle_filled(960, 540, 1920, 600, arcade.color.BLUSH)
        #arcade.draw_rectangle_filled(420, 160, 20, 40, arcade.color.BLUSH, 45)
        arcade.finish_render()




pantalla=Juego(1920,1080, 'Evolutron')
pantalla.iniciar_pantalla()
arcade.run()
        
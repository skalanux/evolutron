import arcade

class Juego(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title, fullscreen=True)
        arcade.set_background_color(arcade.color.EERIE_BLACK)






Juego(1920,1080, 'Evolutron')
arcade.run()
        
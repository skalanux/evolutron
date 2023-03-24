import arcade
from random import randint,shuffle
import time

class Juego(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title, fullscreen=True)
        arcade.set_background_color(arcade.color.EERIE_BLACK)

        self.vegetacion_ubicacion=[]
        self.start_time=time.time()
        self.create_vegetacion(60)
        self.fire=False

    def iniciar_pantalla(self):
        arcade.draw_text("Winter", 850, 985, arcade.color.AQUA, 50)
        arcade.draw_rectangle_filled(960, 640, 1920, 600, arcade.color.WHITE)

    def create_vegetacion(self,cantidad=10):
        vegetacion = 0
        while vegetacion <= cantidad :
            #print(f"vegetacion = {vegetacion}")
            punto_y=randint(380,900)
            punto_x=randint(00,1900)
            vegetacion += 1
            self.vegetacion_ubicacion.append((punto_x,punto_y))
            

    def draw_vegetation(self):
        for coordenada in self.vegetacion_ubicacion:
            arcade.draw_rectangle_filled(coordenada[0], coordenada[1], 30, 60, arcade.color.GREEN)

    def on_draw(self):
        arcade.start_render()
        pantalla.iniciar_pantalla()
        pantalla.draw_vegetation()
        print(pantalla.vegetacion_ubicacion)
        #arcade.finish_render()

    def create_fire(self):
        if len(self.vegetacion_ubicacion) > 0:
            plantas_moriran=int(len(self.vegetacion_ubicacion)/100 *10)
            shuffle(self.vegetacion_ubicacion)
            for i in range(plantas_moriran):
                fire=self.vegetacion_ubicacion.pop()
        self.fire=False
            

    def on_update(self,delta_time):
        if self.fire:
            self.create_fire()


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.fire=True

        return super().on_key_press(symbol, modifiers)
    



pantalla=Juego(1920,1080, 'Evolutron')

arcade.run()
        
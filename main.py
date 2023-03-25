import time
from itertools import cycle
from random import randint,shuffle
import glob

import arcade

from bioma import Bioma, TIPO_CLIMA_CALIDO, TIPO_CLIMA_TEMPLADO, TIPO_CLIMA_FRIO
from individual import Individual


ARBOL="sprites/vegetation/arbol.png"
HONGO="sprites/vegetation/honguito.png"

class Juego(arcade.Window):
    def __init__(self, width, heigth, title, bioma, individual):
        super().__init__(width, heigth, title, fullscreen=True)
        arcade.set_background_color(arcade.color.EERIE_BLACK)

        self.vegetacion_ubicacion=[]
        self.start_time=time.time()
        self.plantas_sprites=cycle([ARBOL,ARBOL,ARBOL,ARBOL,ARBOL,ARBOL,ARBOL,HONGO,HONGO,HONGO])
        self.fire=False
        self.individual_type = individual
        self.cant_individual = 1
        self.reproducirse = False
        self.status_individual = 'vivo'


        self.papa_sprite = self.load_images_sequence(sorted(glob.glob("sprites/PapaPlayer/Papa*.png")), 100)
        self.rana_sprite = self.load_images_sequence(sorted(glob.glob("sprites/PresaRana/Rana*.png")), 100)
        self.roca_sprite = self.load_images_sequence(sorted(glob.glob("sprites/DepredadorRoca/Roca*.png")), 100)

        self.papa_sprite.center_x = 194
        self.papa_sprite.center_y = 634
        self.papa_sprite.scale = 0.5

        self.rana_sprite.center_y = randint(380,900)
        self.rana_sprite.center_x = randint(50,1900)
        self.rana_sprite.scale = 0.5

        self.roca_sprite.center_x =randint(50,1900)
        self.roca_sprite.center_y = randint(380,900)
        self.roca_sprite.scale = 0.3

        # Defino bioma
        self.create_vegetacion(bioma.cant_plantas)
        self.has_predators = bioma.has_predators
        self.tipo_clima = bioma.tipo_clima



    def iniciar_pantalla(self):
        arcade.draw_text("Selva", 850, 985, arcade.color.AQUA, 50)
        arcade.draw_rectangle_filled(960, 640, 1920, 600, arcade.color.WHITE)

    def create_vegetacion(self,cantidad=10):
        vegetacion = 0
        while vegetacion <= cantidad :
            #print(f"vegetacion = {vegetacion}")
            punto_y=randint(380,900)
            punto_x=randint(00,1900)
            self.vegetacion_ubicacion.append((punto_x,punto_y, next(self.plantas_sprites)))
            vegetacion += 1

    def draw_vegetation(self):
        for coordenada in self.vegetacion_ubicacion:
            arbol = arcade.Sprite(coordenada[2], center_x=coordenada[0], center_y=coordenada[1], scale=0.5)
            arbol.draw()
            #arcade.draw_rectangle_filled(coordenada[0], coordenada[1], 30, 60, arcade.color.GREEN)

    def on_draw(self):
        arcade.start_render()
        pantalla.iniciar_pantalla()
        self.rana_sprite.draw()
        self.roca_sprite.draw()
        pantalla.draw_vegetation()
        self.papa_sprite.draw()
        

        arcade.draw_text(self.status_individual, 850, 85, arcade.color.AQUA, 50)
        arcade.draw_text(f"Tiempo: {self.tiempo_transcurrido}", 50, 185, arcade.color.AQUA, 50)

        arcade.draw_text(f"Individuos: {self.cant_individual}", 2, 135, arcade.color.AQUA, 50)
        #arcade.finish_render()

    def create_fire(self):
        if len(self.vegetacion_ubicacion) > 0:
            plantas_moriran=int(len(self.vegetacion_ubicacion)/100 *10)
            shuffle(self.vegetacion_ubicacion)
            for i in range(plantas_moriran):
                fire=self.vegetacion_ubicacion.pop()
        self.fire=False


    def on_update(self,delta_time):
        cant_plantas = len(self.vegetacion_ubicacion)
        print(cant_plantas)
        survival = self.individual_type.get_survival(self.cant_individual, cant_plantas, self.has_predators, self.tipo_clima)
        print(survival)

        if survival == 1:
            self.status_individual = "vivo"
        elif survival == 0.5:
            self.status_individual = "sobrevivo"
        else:
            self.status_individual = "extinto"

        self.tiempo_transcurrido = int(time.time() - self.start_time)
        if(self.tiempo_transcurrido)>=10:
            if self.status_individual == 'vivo':
                self.cant_individual += 1
            self.start_time = time.time()

        if self.fire:
            self.create_fire()

        self.papa_sprite.update_animation(delta_time)
        self.rana_sprite.update_animation(delta_time)
        self.roca_sprite.update_animation(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.fire=True
        if symbol == arcade.key.Q:
            arcade.exit()
        return super().on_key_press(symbol, modifiers)
    
    def load_images_sequence(self,filenames, frame_duration):
        print(filenames)
        sprite = arcade.AnimatedTimeBasedSprite()
        for fname in filenames:
            texture = arcade.load_texture(fname)
            sprite.textures.append(texture)
            frame = arcade.AnimationKeyframe(0, frame_duration, texture)
            sprite.frames.append(frame)

        #sprite.texture = sprite.textures[0]
        return sprite


individual = Individual(herbivoro=True)
cant_plantas = 160
tipo_clima = TIPO_CLIMA_TEMPLADO
has_predators = True
cant_preys = 100

bioma = Bioma(cant_plantas, tipo_clima, has_predators, cant_preys)
pantalla = Juego(1920,1080, 'Evolutron', bioma, individual)

arcade.run()

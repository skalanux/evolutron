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

        self.lista_roca = arcade.SpriteList()

        self.lista_papa = arcade.SpriteList()

        self.lista_rana = arcade.SpriteList()

        self.fondo=arcade.Sprite("sprites/map/map.png",center_x=960,center_y=540,scale=1.1)

        for i in range(3):
            roca_sprite = self.load_images_sequence(sorted(glob.glob("sprites/DepredadorRoca/Roca*.png")), 100)
            roca_sprite.center_x =randint(50,1900)
            roca_sprite.center_y = randint(380,900)
            roca_sprite.scale = 0.3 
            self.lista_roca.append(roca_sprite)

        for i in range(bioma.cant_preys):
            rana_sprite = self.load_images_sequence(sorted(glob.glob("sprites/PresaRana/Rana*.png")), 100)
            rana_sprite.center_y = randint(380,900)
            rana_sprite.center_x = randint(50,1900)
            rana_sprite.scale = 0.5
            self.lista_rana.append(rana_sprite)


        self.crear_individuo()
        

        # Defino bioma
        self.create_vegetacion(bioma.cant_plantas)
        self.has_predators = bioma.has_predators
        self.tipo_clima = bioma.tipo_clima
        self.nombre_bioma=bioma.nombre


    def crear_individuo(self):
        papa_sprite = self.load_images_sequence(sorted(glob.glob("sprites/PapaPlayer/Papa*.png")), 100)
        self.lista_papa.append(papa_sprite)
    
        papa_sprite.center_x = randint(125,355) 
        papa_sprite.center_y = randint(200,350) 
        papa_sprite.scale = 0.5



    def dibujar_fondo(self):
        arcade.draw_text(self.nombre_bioma, 850, 985, arcade.color.ORANGE, 50,font_name="Kenney Pixel Square")
        self.fondo.draw()
        #arcade.draw_rectangle_filled(960, 540, 1920, 800, arcade.color.WHITE)

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
        pantalla.dibujar_fondo()
        self.lista_rana.draw()
        self.lista_roca.draw()
        self.draw_vegetation()
        self.lista_papa.draw()
        

        arcade.draw_text(self.status_individual, 850, 85, arcade.color.AQUA, 50)
        arcade.draw_text(f"Tiempo: {self.tiempo_transcurrido}", 50, 80, arcade.color.AQUA, 40,font_name="Kenney Pixel Square")

        arcade.draw_text(f"Individuos: {self.cant_individual}", 10, 20, arcade.color.AQUA, 40,font_name="Kenney Pixel Square")
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
        survival = self.individual_type.get_survival(self.cant_individual, cant_plantas, self.has_predators, self.tipo_clima)

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
                self.crear_individuo()
            self.start_time = time.time()

        if self.fire:
            self.create_fire()

        self.lista_papa.update_animation(delta_time)
        self.lista_rana.update_animation(delta_time)
        self.lista_roca.update_animation(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.F:
            self.fire=True
        if symbol == arcade.key.Q:
            arcade.exit()
        return super().on_key_press(symbol, modifiers)

    def load_images_sequence(self,filenames, frame_duration):
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
tipo_clima = TIPO_CLIMA_FRIO
has_predators = True
cant_preys = 25
nombre= "Bosque"

bioma = Bioma(cant_plantas, tipo_clima, has_predators, cant_preys,nombre)
pantalla = Juego(1920,1080, 'Evolutron', bioma, individual)

arcade.run()

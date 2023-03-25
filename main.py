import time
from itertools import cycle
from random import randint,shuffle
import glob

import arcade

from bioma import selva, bosque, tundra
from individual import Individual


ARBOL="sprites/vegetation/arbol_{}.png"
HONGO="sprites/vegetation/honguito_{}.png"
VIVE="vive"
SOBREVIVE="sobrevive"
EXTINGUE="Kaput"


dibujar = arcade.SpriteList()

class Juego(arcade.Window):
    def __init__(self, width, heigth, title, bioma, individual):
        super().__init__(width, heigth, title, fullscreen=True)
        arcade.set_background_color(arcade.color.EERIE_BLACK)

        self.vegetacion_ubicacion=[]
        self.start_time=time.time()
        arbol_1 = ARBOL.format(bioma.tipo_clima)
        arbol_2 = HONGO.format(bioma.tipo_clima)
        self.plantas_sprites=cycle([arbol_1,arbol_1,arbol_1,arbol_1,arbol_1,arbol_1,arbol_1,arbol_2,arbol_2,arbol_2])
        self.fire=False
        self.flood=False
        self.individual_type = individual
        self.cant_individual = 1
        self.reproducirse = False
        self.status_individual = VIVE

        self.lista_roca = arcade.SpriteList()
        self.lista_papa = arcade.SpriteList()
        self.lista_rana = arcade.SpriteList()
        self.lista_vegetation = arcade.SpriteList()
        self.lista_fx = arcade.SpriteList()
        self.lista_flood = arcade.SpriteList()

        self.fondo=arcade.Sprite(f"sprites/map/{bioma.tipo_clima}.png",center_x=700,center_y=540,scale=1.1)
        self.papa_bien=arcade.Sprite("sprites/PapasEstados/PapaBien.png",center_x=700,center_y=70)
        self.papa_mal=arcade.Sprite("sprites/PapasEstados/PapaMal.png",center_x=700,center_y=70)
        self.papa_muerta=arcade.Sprite("sprites/PapasEstados/PapaMuerta.png",center_x=700,center_y=70)


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
        self.bioma = bioma
        self.create_vegetacion(bioma.cant_plantas)
        self.has_predators = bioma.has_predators
        self.tipo_clima = bioma.tipo_clima
        self.nombre_bioma=bioma.nombre


    def crear_individuo(self):
        papa_sprite = self.load_images_sequence(sorted(glob.glob("sprites/PapaPlayer/Papa*.png")), 100)

        papa_scale = 1 if self.individual_type.is_big else 0.5

        papa_sprite.center_x = randint(125,355)
        papa_sprite.center_y = randint(200,350)
        papa_sprite.scale = papa_scale
        self.lista_papa.append(papa_sprite)

    def dibujar_fondo(self):
        self.fondo.draw(pixelated=True)

    def show_bioma_attrs(self):
        arcade.draw_text(self.nombre_bioma, 150, 985, arcade.color.ORANGE, 50,font_name="Kenney Pixel Square")
        tipo_clima = self.bioma.tipo_clima
        tiene_depredadores = "si" if self.bioma.has_predators else "no"
        cant_presas = self.bioma.cant_preys
        cant_plantas = self.bioma.cant_plantas

        arcade.draw_text(f"Cantidad de presas: {cant_presas}", 1550, 1040, arcade.color.WHITE, 15,font_name="Kenney Pixel Square")
        arcade.draw_text(f"Vegetación: {cant_plantas}", 1550, 1010, arcade.color.ORANGE, 15,font_name="Kenney Pixel Square")
        arcade.draw_text(f"Clima: {tipo_clima}", 1550, 980, arcade.color.WHITE, 15,font_name="Kenney Pixel Square")
        arcade.draw_text(f"Depredadores: {tiene_depredadores}", 1550, 950, arcade.color.ORANGE, 15,font_name="Kenney Pixel Square")

    def create_vegetacion(self,cantidad=10):
        vegetacion = 0
        while vegetacion <= cantidad :
            punto_y=randint(380,900)
            punto_x=randint(00,1900)
            arbol = arcade.Sprite(next(self.plantas_sprites), center_x=punto_x, center_y=punto_y, scale=0.5)
            self.lista_vegetation.append(arbol)
            vegetacion += 1

    def show_individual_attributes(self):
        carnivoro = "si" if self.individual_type.carnivoro else "no"
        herbivoro = "si" if self.individual_type.herbivoro else "no"
        tiene_pelo = "si" if self.individual_type.has_hair else "no"
        es_grande = "si" if self.individual_type.is_big else "no"

        arcade.draw_text(f"Carnívoro: {carnivoro}", 1550, 110, arcade.color.ORANGE, 15,font_name="Kenney Pixel Square")
        arcade.draw_text(f"Herbívoro: {herbivoro}", 1550, 80, arcade.color.WHITE, 15,font_name="Kenney Pixel Square")
        arcade.draw_text(f"Tiene Pelo: {tiene_pelo}", 1550, 50, arcade.color.ORANGE, 15,font_name="Kenney Pixel Square")
        arcade.draw_text(f"Es grande: {es_grande}", 1550, 20, arcade.color.WHITE, 15,font_name="Kenney Pixel Square")

        arcade.draw_text(f"{self.individual_type.name}", 800, 15, arcade.color.ORANGE, 25,font_name="Kenney Pixel Square")


    def show_individual_status(self):
        arcade.draw_text(self.status_individual, 800, 70, arcade.color.WHITE, 50,font_name="Kenney Pixel Square")

    def show_game_stats(self):
        arcade.draw_text(f"Tiempo: {self.tiempo_transcurrido}", 50, 80, arcade.color.ORANGE, 40,font_name="Kenney Pixel Square")

        arcade.draw_text(f"Individuos: {self.cant_individual}", 10, 20, arcade.color.WHITE, 40,font_name="Kenney Pixel Square")

    def on_draw(self):
        arcade.start_render()
        self.dibujar_fondo()

        dibujar.extend(self.lista_vegetation)
        dibujar.extend(self.lista_rana)
        dibujar.extend(self.lista_roca)
        dibujar.extend(self.lista_fx)
        dibujar.sort(key=lambda x: -x.center_y)
        dibujar.extend(self.lista_flood)
        dibujar.extend(self.lista_papa)


        dibujar.draw(pixelated=True)

        dibujar.clear()

        self.cambiar_carita()
        self.show_individual_status()
        self.show_individual_attributes()
        self.show_game_stats()
        self.show_bioma_attrs()

        arcade.finish_render()
    def cambiar_carita(self):
        if self.status_individual == VIVE:
            self.papa_bien.draw()
        elif self.status_individual == SOBREVIVE:
            self.papa_mal.draw()
        elif self.status_individual == EXTINGUE:
            self.papa_muerta.draw()

    def create_fire(self):
        if len(self.lista_vegetation) > 0:
            plantas_moriran=int(len(self.lista_vegetation)/100 *10)

            for i in range(plantas_moriran):
                plant_to_remove = self.lista_vegetation.pop()

                fire = self.load_images_sequence(sorted(glob.glob("sprites/Fuego/Fuego*.png")), 50)
                fire.center_x = plant_to_remove.center_x
                fire.center_y = plant_to_remove.center_y
                fire.scale = 0.3
                fire.ttl = 0

                self.lista_fx.append(fire)


        self.fire=False

    def create_flood(self):
        if len(self.lista_rana) > 0:
            ranas_moriran=int(len(self.lista_rana)/100*20)

            for i in range(ranas_moriran):
                rana_to_remove = self.lista_rana.pop()

                flood = self.load_images_sequence(sorted(glob.glob("sprites/ola.png")), 50)
                flood.center_x = 0
                flood.center_y = 600
#               flood.center_y = rana_to_remove.center_y
                flood.scale = 0.8
                flood.ttl = -5


                self.lista_flood.append(flood)


        self.flood=False

    def on_update(self,delta_time):
        cant_plantas = len(self.lista_vegetation)
        survival = self.individual_type.get_survival(self.cant_individual, cant_plantas, self.has_predators, self.tipo_clima, self.bioma.cant_preys)

        prev_status = self.status_individual

        self.move_individuos()

        if survival == 1:
            self.status_individual = VIVE
        elif survival == 0.5:
            self.status_individual = SOBREVIVE
        else:
            self.status_individual = EXTINGUE

        self.change_individuos(self.status_individual)

        self.tiempo_transcurrido = int(time.time() - self.start_time)
        if(self.tiempo_transcurrido)>=10:
            if self.status_individual == VIVE:
                self.cant_individual += 1
                self.crear_individuo()
            self.start_time = time.time()

        if self.fire:
            self.create_fire()

        if self.flood:
            self.create_flood()


        self.lista_papa.update_animation(delta_time)
        self.lista_rana.update_animation(delta_time)
        self.lista_roca.update_animation(delta_time)
        self.lista_fx.update_animation(delta_time)
        self.lista_flood.update_animation(delta_time)

        for fx in self.lista_fx:
            if fx.ttl > 1: # en un segundo se elimina.
                self.lista_fx.remove(fx)
            else:
                fx.ttl += delta_time

        for fx in self.lista_flood:
            if fx.ttl > 1: # en un segundo se elimina.
                self.lista_flood.remove(fx)
            else:
                fx.ttl += delta_time
                fx.center_x += 20

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.flood=True
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

    def move_individuos(self):
        if self.status_individual == VIVE:
            desplazamiento = 6
        elif self.status_individual == SOBREVIVE:
            desplazamiento = 5
        else:
            desplazamiento = 0

        if desplazamiento != 0:
            for papa in self.lista_papa:
                if papa.center_x >= 1920:
                    papa.center_x = 0
                else:
                    papa.center_x += desplazamiento

    def change_individuos(self, survival_type):
        if survival_type == VIVE:
            color = (255,255,255,255)
        elif survival_type == SOBREVIVE:
            color = (255,255,255,120)
        else:
            color = (255,255,255,0)

        lista_papas = arcade.SpriteList()

        for papa in self.lista_papa:
            papa.color = color
            lista_papas.append(papa)

        self.lista_papa = lista_papas

individual = Individual(herbivoro=True, has_hair=False, is_big=True, name="Pycampustropus")
pantalla = Juego(1920,1080, 'Evolutron', bosque, individual)
arcade.run()

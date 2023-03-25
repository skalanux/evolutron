from dataclasses import dataclass


TIPO_CLIMA_CALIDO = 'calido'
TIPO_CLIMA_TEMPLADO = 'templado'
TIPO_CLIMA_FRIO = 'frio'


@dataclass
class Bioma:
    cant_plantas: int
    tipo_clima: str
    has_predators: bool
    cant_preys: int
    nombre: str

    def reset():
        ...


cant_plantas = 160
tipo_clima = TIPO_CLIMA_CALIDO
has_predators = True
cant_preys = 25
nombre= "Selva"
selva = Bioma(cant_plantas, tipo_clima, has_predators, cant_preys,nombre)


cant_plantas = 120
tipo_clima = TIPO_CLIMA_TEMPLADO
has_predators = False
cant_preys = 15
nombre= "Bosque"
bosque = Bioma(cant_plantas, tipo_clima, has_predators, cant_preys,nombre)


cant_plantas = 50
tipo_clima = TIPO_CLIMA_FRIO
has_predators = True
cant_preys = 10
nombre= "Tundra"
tundra = Bioma(cant_plantas, tipo_clima, has_predators, cant_preys,nombre)


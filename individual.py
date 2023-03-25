from dataclasses import dataclass

from bioma import TIPO_CLIMA_CALIDO, TIPO_CLIMA_TEMPLADO, TIPO_CLIMA_FRIO


SURVIVAL_HERB_THRESHOLD_MAX_PLANTS = 40
SURVIVAL_HERB_THRESHOLD_MIN_PLANTS = 20

SURVIVAL_CARN_THRESHOLD_MAX_PREYS = 20
SURVIVAL_CARN_THRESHOLD_MIN_PREYS = 40


@dataclass
class Individual:
    herbivoro: bool = False
    carnivoro: bool = False
    has_hair: bool = False
    is_big: bool = False

    def get_survival(self, cant_individuals, cant_plantas, has_predators, tipo_clima, cant_presas):
        survival_herbivoro = 1
        survival_carnivoro = 1
        survival_big = 1
        survival_hair = 1


        if self.herbivoro:
            plantas_disponibles = cant_plantas / cant_individuals

            if plantas_disponibles > SURVIVAL_HERB_THRESHOLD_MAX_PLANTS:
                survival_herbivoro = 1
            elif plantas_disponibles <=SURVIVAL_HERB_THRESHOLD_MAX_PLANTS and plantas_disponibles > SURVIVAL_HERB_THRESHOLD_MIN_PLANTS:
                survival_herbivoro = 0.5
            else:
                survival_herbivoro = 0

        if self.carnivoro:
            presas_disponibles = cant_presas / cant_individuals

            if presas_disponibles > SURVIVAL_CARN_THRESHOLD_MAX_PREYS:
                survival_carnivoro = 1
            elif presas_disponibles <=SURVIVAL_CARN_THRESHOLD_MAX_PREYS and presas_disponibles > SURVIVAL_CARN_THRESHOLD_MIN_PREYS:
                survival_carnivoro = 0.5
            else:
                survival_carnivoro = 0

        if self.has_hair:
            if tipo_clima == TIPO_CLIMA_CALIDO:
                survival_hair = 0
            elif tipo_clima == TIPO_CLIMA_TEMPLADO:
                survival_hair = 0.5
            else:
                survival_hair = 1


        reproduce = False
        sobrevive = False
        muere = False

        if survival_herbivoro == 1 and survival_carnivoro == 1 and survival_big == 1 and survival_hair == 1:
            reproduce = True
        elif survival_herbivoro >= 0.5 and survival_carnivoro >= 0.5 and survival_big >= 0.5 and survival_hair >= 0.5:
            sobrevive = True
        else:
            muere = True

        if reproduce:
            survival = 1
        elif sobrevive:
            survival = 0.5
        else:
            survival = 0

        return survival





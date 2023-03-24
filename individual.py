from dataclasses import dataclass



@dataclass
class Individual:
    herbivoro: bool

    def get_survival(self, cant_individuals, cant_plantas):
        plantas_disponibles = cant_plantas / cant_individuals

        if plantas_disponibles > 40:
            survival = 1
        elif plantas_disponibles <=40 and plantas_disponibles > 20:
            survival = 0.5
        else:
            survival = 0

        return survival


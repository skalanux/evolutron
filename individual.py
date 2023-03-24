from dataclasses import dataclass



@dataclass
class Individual:
    herbivoro: bool

    def get_survival(self, cant_plantas):
        if cant_plantas > 20:
            survival = 1
        elif cant_plantas <=20 and cant_plantas > 10:
            survival = 0.5
        else:
            survival = 0

        return survival


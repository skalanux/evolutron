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

    def reset():
        ...



from individual import Individual, TIPO_CLIMA_TEMPLADO, TIPO_CLIMA_CALIDO, TIPO_CLIMA_FRIO, SURVIVAL_HERB_THRESHOLD_MAX_PLANTS, SURVIVAL_HERB_THRESHOLD_MIN_PLANTS

def test_all_ok_reproduce():
    individual = Individual(herbivoro=True,
                            carnivoro=True,
                            is_big=True,
                            has_hair=True)


    survival = individual.get_survival(
                            cant_individuals=1,
                            cant_plantas=100,
                            has_predators=True,
                            tipo_clima=TIPO_CLIMA_TEMPLADO)

    print(survival)
    assert survival == 1


def test_any_medium_all_none_zero_survives():
    individual = Individual(herbivoro=True,
                            carnivoro=True,
                            is_big=True,
                            has_hair=True)


    survival = individual.get_survival(
                            cant_individuals=1,
                            cant_plantas=SURVIVAL_HERB_THRESHOLD_MAX_PLANTS,
                            has_predators=True,
                            tipo_clima=TIPO_CLIMA_TEMPLADO)

    print(survival)
    assert survival == 0.5


def test_any_zero_dies():
    individual = Individual(herbivoro=True,
                            carnivoro=True,
                            is_big=True,
                            has_hair=True)


    survival = individual.get_survival(
                            cant_individuals=1,
                            cant_plantas=SURVIVAL_HERB_THRESHOLD_MIN_PLANTS,
                            has_predators=True,
                            tipo_clima=TIPO_CLIMA_TEMPLADO)

    print(survival)
    assert survival == 0

def test_planta_9_dies():
    individual = Individual(herbivoro=True,
                            carnivoro=True,
                            is_big=True,
                            has_hair=True)


    survival = individual.get_survival(
                            cant_individuals=1,
                            cant_plantas=9,
                            has_predators=True,
                            tipo_clima=TIPO_CLIMA_TEMPLADO)

    print(survival)
    assert survival == 0


"""
Defina uma constante EXPECTED_BAKE_TIME que retorne quantos minutos a lasanha deve assar no forno.
De acordo com o seu livro de receitas, a lasanha deve ficar no forno por 40 minutos:

>>> lasagna.EXPECTED_BAKE_TIME
40

Implemente a função bake_time_remaining() que leva os minutos reais que a lasanha esteve no forno como um argumento
e retorna quantos minutos a lasanha ainda precisa assar com base no EXPECTED_BAKE_TIME.

>>> bake_time_remaining(30)
10

Implemente a função prepare_time_in_minutes() que leva o número de camadas que você deseja adicionar à lasanha como
um argumento e retorna quantos minutos você gastaria para criá-los. Suponha que cada camada leve 2 minutos para preparar..

>>> preparation_time_in_minutes(2)
4

Implemente a função elapsed_time_in_minutes() que possui dois parâmetros: number_of_layers (o número de camadas
adicionadas à lasanha) e elapsed_bake_time (o número de minutos que a lasanha está assando no forno). Esta função
deve retornar o número total de minutos que você está cozinhando, ou a soma do seu tempo de preparo e o tempo que
a lasanha já passou assando no forno.

>>> elapsed_time_in_minutes(3, 20)
26

Volte pela receita, adicionando notas e documentação.

"""

"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 40


class Lasagna:
    """
    Foi necessário criar a classe Lasagna para poder testar, mas na página Exercism não é necessário
    """
    def __init__(self, EXPECTED_BAKE_TIME = 40):
        self.EXPECTED_BAKE_TIME = EXPECTED_BAKE_TIME


lasagna = Lasagna()
lasagna.EXPECTED_BAKE_TIME

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(t):
    """
    function takes one number and return the total preparation time
    """
    return t * 2


def elapsed_time_in_minutes(numbers_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return numbers_of_layers * 2 + elapsed_bake_time

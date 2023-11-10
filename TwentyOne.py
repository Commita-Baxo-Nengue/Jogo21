class Jogador:
    def __init__(self, nome, fichas, idade):
        self.__nome = nome 
        self.__fichas = fichas
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_fichas(self):
        return self.__fichas

    def set_fichas(self, fichas):
        self.__fichas = fichas

    def get_idade(self):
        return self.__idade


jogador_1 = Jogador("Emanuelle", 237, 18)
jogador_2 = Jogador("Spotify", 213, 17)

print("Olá jogador", jogador_1.get_nome(),"! >.<", "seu número de fichas é de: ", jogador_1.get_fichas())
print("Olá jogador", jogador_2.get_nome(),"! >.<", "seu número de fichas é de: ", jogador_2.get_fichas())

""""
print()
print()
"""


class Deck:
    def cartasla():

        cartas = {1: {"carta": "A", "valor": 1},   2: {"carta": "A", "valor": 1},   3: {"carta": "A", "valor": 1},   4: {"carta": "A", "valor": 1},
                  5: {"carta": "10", "valor": 10}, 6: {"carta": "10", "valor": 10}, 7: {"carta": "10", "valor": 10}, 8: {"carta": "10", "valor": 10},
                  9: {"carta": "Q", "valor": 10}, 10: {"carta": "Q", "valor": 10}, 11: {"carta": "Q", "valor": 10}, 12: {"carta": "Q", "valor": 10},
                 13: {"carta": "J", "valor": 10}, 14: {"carta": "J", "valor": 10}, 15: {"carta": "J", "valor": 10}, 16: {"carta": "J", "valor": 10},
                 17: {"carta": "K", "valor": 10}, 18: {"carta": "K", "valor": 10}, 19: {"carta": "K", "valor": 10}, 20: {"carta": "K", "valor": 10}
}
        



    



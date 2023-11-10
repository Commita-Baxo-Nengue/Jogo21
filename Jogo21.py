# Importa a função shuffle do módulo random para embaralhar as cartas
from random import shuffle

# Classe que representa um jogador
class Jogador:
    # Método de inicialização que define os atributos do jogador
    def __init__(self, nome, fichas, idade):
        self.__nome = nome
        self.__fichas = fichas
        self.__idade = idade
        self.__mao = []  # Lista que armazena as cartas na mão do jogador

    # Propriedade (getter) para obter o nome do jogador
    @property
    def nome(self):
        return self.__nome

    # Propriedade (getter) para obter as fichas do jogador
    @property
    def fichas(self):
        return self.__fichas

    # Propriedade (setter) para definir as fichas do jogador
    @fichas.setter
    def fichas(self, valor):
        self.__fichas = valor

    # Propriedade (getter) para obter as cartas na mão do jogador
    @property
    def mao(self):
        return self.__mao

    # Propriedade (setter) para definir as cartas na mão do jogador
    @mao.setter
    def mao(self, nova_mao):
        self.__mao = nova_mao

    # Método para realizar uma aposta
    def apostar(self, valor):
        # Verifica se o jogador tem fichas suficientes para a aposta
        if valor <= self.__fichas:
            self.__fichas -= valor
            return valor  # Retorna o valor da aposta
        else:
            print(f"{self.__nome}, você não tem fichas suficientes para apostar {valor}.")

    # Método para receber fichas
    def receber_fichas(self, valor):
        self.__fichas += valor

# Classe que representa o jogo
class Jogo:
    # Método de inicialização que cria jogadores, o baralho e define o vencedor como None
    def __init__(self, num_jogadores):
        # Lista de jogadores criada com base na quantidade informada
        self.__jogadores = [Jogador(input(f"Digite o nome do Jogador {i+1}: "), 100, 25) for i in range(num_jogadores)]
        self.__baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4  # Baralho padrão com valores das cartas
        self.__vencedor = None  # Inicializa o vencedor como None

    # Método privado para embaralhar as cartas do baralho
    def __embaralhar_cartas(self):
        shuffle(self.__baralho)

    # Método privado para calcular a pontuação de uma mão de cartas
    def __calcular_pontuacao(self, mao):
        pontuacao = sum(mao)
        # Se estourou e há um Ás (carta de valor 1), troca o valor do Ás para 11
        if pontuacao > 21 and 1 in mao:
            mao.remove(1)
            mao.append(11)
            pontuacao = sum(mao)
        return pontuacao

    # Método privado para verificar o vencedor com base nas pontuações dos jogadores
    def __verificar_vencedor(self):
        # Lista de pontuações dos jogadores
        pontuacoes = [self.__calcular_pontuacao(jogador.mao) for jogador in self.__jogadores]
        # Índice do jogador com a maior pontuação
        vencedor_index = pontuacoes.index(max(pontuacoes))
        # Define o vencedor como o jogador com a maior pontuação
        self.__vencedor = self.__jogadores[vencedor_index]

    # Método principal para executar o jogo
    def jogar(self):
        # Embaralha as cartas no início de cada rodada
        self.__embaralhar_cartas()

        # Distribui duas cartas para cada jogador
        for jogador in self.__jogadores:
            jogador.mao = [self.__baralho.pop(), self.__baralho.pop()]

        while True:
            for jogador in self.__jogadores:
                # Exibe informações do jogador (nome, fichas, mão, pontuação)
                print(f"\n{ jogador.nome }, suas fichas: { jogador.fichas }, sua mão: { jogador.mao }")
                print(f"Total de pontos: {self.__calcular_pontuacao(jogador.mao)}")
                aposta = jogador.apostar(20)  # Jogador realiza uma aposta

                while True:
                    # Exibe informações da mão atual do jogador
                    print(f"\nCartas na mão: { jogador.mao }")
                    print(f"Total de pontos: {self.__calcular_pontuacao(jogador.mao)}")

                    # Opções disponíveis para o jogador
                    print("\nOpções:")
                    print("1. Pedir mais uma carta")
                    print("2. Parar")
                    escolha = input("Escolha sua ação (1/2): ")

                    if escolha == '1':
                        carta = self.__baralho.pop()  # Tira uma carta do baralho
                        jogador.mao.append(carta)  # Adiciona a carta à mão do jogador
                        print(f"Você tirou a carta {carta}.")
                        pontuacao = self.__calcular_pontuacao(jogador.mao)

                        # Condição de vitória (Blackjack)
                        if pontuacao == 21:
                            print("Blackjack! Você venceu!")
                            jogador.receber_fichas(aposta * 2)  # Jogador recebe o dobro da aposta
                            self.__verificar_vencedor()  # Verifica se há um vencedor
                            return
                        # Condição de derrota (Estourou)
                        elif pontuacao > 21:
                            print("Estourou! Você perdeu.")
                            break
                    elif escolha == '2':
                        break

            self.__verificar_vencedor()  # Verifica o vencedor ao final da rodada
            if self.__vencedor:
                print(f"\n{self.__vencedor.nome} venceu!")
                self.__vencedor.receber_fichas(aposta * 2)  # Vencedor recebe o dobro da aposta
                break

# Bloco de execução principal quando o script é executado
if __name__ == "__main__":
    print("Bem-vindo ao Jogo 21!")

    # Escolher quantidade de jogadores

    num_jogadores = int(input("Digite a quantidade de jogadores: "))

    # Criação do jogo
    jogo = Jogo(num_jogadores)

    while True:
        jogo.jogar()

        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

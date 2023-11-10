from random import shuffle


class Player:

    def __init__(self, nome, fichas, idade):
        self.__nome = nome
        self.__fichas = fichas
        self.__idade = idade
        self.__mao = []  # Lista que armazena as cartas na mão do jogador

    # "pegar"
    @property
    def nome(self):
        return self.__nome

    # "pegar"
    @property
    def fichas(self):
        return self.__fichas

    # define
    @fichas.setter
    def fichas(self, valor):
        self.__fichas = valor

    # obter as cartas na mão do jogador
    @property
    def mao(self):
        return self.__mao

    # define
    @mao.setter
    def mao(self, nova_mao):
        self.__mao = nova_mao

    def apostar(self, valor):
        # Verifica se o jogador tem fichas suficientes para a aposta
        if valor <= self.__fichas:
            self.__fichas -= valor
            return valor  # Retorna o valor da aposta
        else:
            print(f"{self.__nome}, você não tem fichas suficientes para apostar {valor}.")

    def receber_fichas(self, valor):
        self.__fichas += valor


class Jogo:

    def __init__(self, numero_players):

        self.__jogadores = [Player(input(f"Digite o nome do Player {i + 1}: "), 100, 25) for i in
                            range(numero_players)]
        self.__baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.__vencedor = None

    def __embaralhar_cartas(self):
        shuffle(self.__baralho)

    def __calcular_pontuacao(self, mao):
        pontuacao = sum(mao)
        if pontuacao > 21 and 1 in mao:
            mao.remove(1)
            mao.append(11)
            pontuacao = sum(mao)
        return pontuacao

    def __verificar_vencedor(self):

        pontuacoes = [self.__calcular_pontuacao(jogador.mao) for jogador in self.__jogadores]

        vencedor_index = pontuacoes.index(max(pontuacoes))

        self.__vencedor = self.__jogadores[vencedor_index]

    def jogar(self):

        self.__embaralhar_cartas()

        for jogador in self.__jogadores:
            jogador.mao = [self.__baralho.pop(), self.__baralho.pop()]

        while True:
            for jogador in self.__jogadores:

                print(f"\n{jogador.nome}, suas fichas: {jogador.fichas}, sua mão: {jogador.mao}")
                print(f"Total de pontos: {self.__calcular_pontuacao(jogador.mao)}")
                aposta = jogador.apostar(20)  # Player realiza uma aposta

                while True:

                    print("Cartas na mão: ", jogador.mao)
                    print(f"Total de pontos: {self.__calcular_pontuacao(jogador.mao)}")

                    print("\nOpções:")
                    print("1. Pedir mais uma carta")
                    print("2. Não jogar mais")
                    acao_escolhida = input("Escolha sua ação (1/2): ")

                    if acao_escolhida == '1':
                        carta = self.__baralho.pop()
                        jogador.mao.append(carta)
                        print(f"Você tirou a carta", carta, ".")
                        pontuacao = self.__calcular_pontuacao(jogador.mao)

                        # GANHOUUUU
                        if pontuacao == 21:
                            print("Blackjack! Você venceu!")
                            jogador.receber_fichas(aposta * 2)  # Player recebe o dobro da aposta
                            self.__verificar_vencedor()  # Verifica se há um vencedor
                            return
                        # Condição de derrota (Estourou)
                        elif pontuacao > 21:
                            print("Estourou! Você perdeu.")
                            break
                    elif acao_escolhida == '2':
                        break

            self.__verificar_vencedor()
            if self.__vencedor:
                print(self.__vencedor.nome, " venceu!")
                self.__vencedor.receber_fichas(aposta * 2)
                break


if __name__ == "__main__":
    print("Bem-vindo ao da Manella de BlackJack!")
    print("Espero que você esteja pronto...")
    print("LET'S START THIS PARTY! ! (referancia de valorant kk)")
    num_jogadores = int(input("Quantos jogadores temos aqui?: "))

    jogo = Jogo(num_jogadores)

    while True:
        jogo.jogar()

        jogar_novamente = input("\nQuieres jugar de nuevo manito? (sim/nao): ").lower()
        if jogar_novamente != 'nao' or 'n' or 'na' or 'no':
            print("Não gostou do jogo foi? Ok T.T")
            break

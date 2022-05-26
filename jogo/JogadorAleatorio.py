from random import randint
from jogo.Jogador import Jogador


class JogadorAleatorio(Jogador):
    """
      jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
    """

    def _regras_para_pagamento(self, propriedade):
        if randint(0, 1) != 0:
            return True
        return False
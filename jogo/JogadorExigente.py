from jogo.Jogador import Jogador


class JogadorExigente(Jogador):
    """
    O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
    """

    def _regras_para_pagamento(self, propriedade):
        if propriedade.aluguel > 50:
            return True
        return False


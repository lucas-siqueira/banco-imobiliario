from jogo.Jogador import Jogador


class JogadorImpulsivo(Jogador):
    """
    O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
    """

    def _regras_para_pagamento(self, propriedade):
        return True

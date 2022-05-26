from jogo.Jogador import Jogador

RESERVA_MINIMA_SALDO = 80


class JogadorCauteloso(Jogador):
    """
    O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
depois de realizada a compra.
    """

    def _regras_para_pagamento(self, propriedade):
        if (self.dinheiro - propriedade.valor_imovel) >= RESERVA_MINIMA_SALDO:
            return True
        return False


from abc import abstractmethod


SALDO_JOGADOR = 300.0
INCRMENTO_SALDO_RODADA = 100.0

JOGADOR_IMPULSIVO = 1
JOGADOR_EXIGENTE = 2
JOGADOR_CAUTELOSO = 3
JOGADOR_ALEATORIO = 4

DESC_TIPO_ESTRATEGIA_DICT = {
    JOGADOR_IMPULSIVO: 'Jogador Impulsivo',
    JOGADOR_EXIGENTE: 'Jogador Exigente',
    JOGADOR_CAUTELOSO: 'Jogador Cauteloso',
    JOGADOR_ALEATORIO: 'Jogador Aleatório',
}


class Jogador:
    def __init__(self, estrategia, posicao=0, dinheiro=SALDO_JOGADOR):
        self.posicao = posicao
        self.dinheiro = dinheiro
        self.estrategia = estrategia
        self.perdeu = False

    def __str__(self):
        return str(self.estrategia)

    def vender_ou_alugar(self, propriedade):
        """
        Aqui que define se vai ser vendida a propriedade ou se vai ser pago o aluguel
        :param propriedade:
        """
        if propriedade.dono:
            if self != propriedade.dono:
                self.paga(propriedade.aluguel, propriedade.dono)
        else:
            # Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda.
            if self.verifica_se_tem_saldo(propriedade.valor_imovel) and self._regras_para_pagamento(propriedade):
                self.paga(propriedade.valor_imovel, propriedade.dono)
                propriedade.dono = self

    def ganha_bonus(self):
        """
        Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo.
        """
        self.dinheiro += float(INCRMENTO_SALDO_RODADA)

    @abstractmethod
    def _regras_para_pagamento(self, propriedade, tabuleiro):
        raise NotImplementedError()

    def verifica_se_tem_saldo(self, valor):
        """
            Verifica se tem dinheiro
        :param valor:
        :return: True caso tenha dinheiro e False caso não tenha
        """
        return self.dinheiro >= valor

    def paga(self, valor_imovel, tipo_de_estrategia=None):
        self.dinheiro -= valor_imovel
        if tipo_de_estrategia:
            tipo_de_estrategia.dinheiro += valor_imovel
        if self.dinheiro <= 0:
            self.perdeu = True

    def joga(self, tabuleiro):
        """
        Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto podem ser
        compradas por qualquer outro jogador.
        """
        if self.dinheiro <= 0:
            self.perdeu = True
            return
        valor_dado = tabuleiro.jogar_dados()
        posicao_tabuleiro = tabuleiro.andar_casa(self, valor_dado)
        propriedade = tabuleiro.__getitem__(posicao_tabuleiro)
        self.vender_ou_alugar(propriedade)


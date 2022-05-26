from datetime import datetime
from random import randint

from jogo.Propriedade import Propriedade

QTD_PROPRIEDADES = 20
QTD_JOGADAS = 1000


class Tabuleiro:

    def __init__(self, *args, **kwargs):
        self._ganhador = None
        self._jogou = 0
        self._jogadores = []
        self.tempo_inicial = datetime.now()
        self._casas_do_tabuleiro = [Propriedade(index, None) for index in range( int(QTD_PROPRIEDADES))]

    @property
    def jogou(self):
        return self._jogou

    @jogou.setter
    def jogou(self, jogou):
        self._jogou = jogou

    @property
    def jogadores(self):
        return self._jogadores

    @jogadores.setter
    def jogadores(self, jogadores):
        self._jogadores = jogadores

    @property
    def ganhador(self):
        return self._ganhador

    @ganhador.setter
    def ganhador(self, ganhador):
        self._ganhador = ganhador

    def jogar_dados(self):
        """
        Essa função representa o ato de jogar o dado
        """
        return randint(1, 6)

    def __getitem__(self, posicao):
        return self._casas_do_tabuleiro[posicao]

    def __setitem__(self, posicao, propriedade):
        self._casas_do_tabuleiro[posicao] = propriedade

    def __len__(self):
        return len(self._casas_do_tabuleiro)

    def __str__(self):
        return f"{self._casas_do_tabuleiro}"

    def __repr__(self):
        return self.__str__()

    def sai_do_jogo(self, jogador):
        for propriedade in self._casas_do_tabuleiro:
            if propriedade.dono == jogador:
                propriedade.dono = None
        self._jogadores.remove(jogador)

    def andar_casa(self, jogador, _qtd_casas=0):
        prox_posicao = jogador.posicao + _qtd_casas
        if prox_posicao >= int(QTD_PROPRIEDADES):
            """
            Ao completar uma volta no tabuleiro,
            o jogador ganha 100 de bonus.
            """
            jogador.ganha_bonus()
            prox_posicao -= int(QTD_PROPRIEDADES)
        jogador.posicao = prox_posicao
        return prox_posicao

    def verifica_ganhador(self, jogador):
        """
        Termina quando restar somente um jogador
        com saldo positivo, a qualquer momento da
        partida. Esse jogador é declarado o
        vencedor.
        """
        if len(self.jogadores) == 1:
            return jogador
        if int(QTD_JOGADAS) <= self.jogou:
            dinheiro = 0
            ganhador = None
            for _jogador in self._jogadores:
                if _jogador.dinheiro > dinheiro:
                    dinheiro = _jogador.dinheiro
                    ganhador = _jogador
            return ganhador

        elements = [
            _jogador.dinheiro for _jogador in self._jogadores if _jogador != jogador
        ]
        if sum(elements) < 0:
            return jogador

        return None

    def situacao(self):
        return {
            "jogou": self.jogou,
            "estrategia": self.ganhador,
            "time_out": self.jogou > int(QTD_JOGADAS),
        }


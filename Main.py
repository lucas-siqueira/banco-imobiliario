from jogo.Jogador import JOGADOR_IMPULSIVO, JOGADOR_EXIGENTE, JOGADOR_CAUTELOSO, JOGADOR_ALEATORIO, \
    DESC_TIPO_ESTRATEGIA_DICT
from jogo.JogadorAleatorio import JogadorAleatorio
from jogo.JogadorCauteloso import JogadorCauteloso
from jogo.JogadorExigente import JogadorExigente
from jogo.JogadorImpulsivo import JogadorImpulsivo
from jogo.Saida import Saida
from jogo.Tabuleiro import Tabuleiro

QTD_SIMILACOES = 300


def criar_jogador(estrategia: int, *args, **kwargs):
    if estrategia == JOGADOR_IMPULSIVO:
        return JogadorImpulsivo(estrategia=estrategia, *args, **kwargs)
    elif estrategia == JOGADOR_EXIGENTE:
        return JogadorExigente(estrategia=estrategia, *args, **kwargs)
    elif estrategia == JOGADOR_CAUTELOSO:
        return JogadorCauteloso(estrategia=estrategia, *args, **kwargs)
    elif estrategia == JOGADOR_ALEATORIO:
        return JogadorAleatorio(estrategia=estrategia, *args, **kwargs)


def cria_tabuleiro():
    tabuleiro = Tabuleiro()
    jogadores = [
        criar_jogador(estrategia) for estrategia in DESC_TIPO_ESTRATEGIA_DICT.keys()
    ]
    tabuleiro.jogadores = jogadores
    return tabuleiro


def main():
    """
    Uma execução do programa proposto deve rodar 300 simulações(QTD_SIMILACOES) , imprimindo no console os dados
    referentes às execuções.
    """

    saida = Saida()
    for index in range(int(QTD_SIMILACOES)):
        tabuleiro = cria_tabuleiro()
        while tabuleiro.ganhador is None:
            for jogador in tabuleiro.jogadores:
                if jogador.perdeu:
                    tabuleiro.sai_do_jogo(jogador)
                ganhador = tabuleiro.verifica_ganhador(jogador)
                if ganhador:
                    tabuleiro.ganhador = ganhador
                    break
                jogador.joga(tabuleiro)
            tabuleiro.jogou += 1
        saida.add(tabuleiro.situacao())
    saida.mostrar_resultados()


if __name__ == "__main__":
    main()

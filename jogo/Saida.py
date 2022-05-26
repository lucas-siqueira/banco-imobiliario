from jogo.Jogador import DESC_TIPO_ESTRATEGIA_DICT


class Saida:
    def __init__(self):
        self._resultados = []

    def add(self, resultado):
        return self._resultados.append(resultado)

    def list_resultados(self):
        return self._resultados.copy()

    def __len__(self):
        return len(self._resultados)

    def __str__(self):
        return f"{self.mostrar_resultados()}"

    def contabilizar_vitoria(self):
        countador_vitorias = {}
        for resultado in self.list_resultados() :
            estrategia = resultado['estrategia'].estrategia
            if not estrategia in countador_vitorias:
                countador_vitorias[estrategia] = 0
            countador_vitorias[estrategia] += 1
        return countador_vitorias

    def mostrar_saida_partida_por_tempo(self):
        """
           Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes
           às execuções. Esperamos encontrar nos dados as seguintes informações:
           - Quantas partidas terminam por time out (1000 rodadas);
           """
        qtd_partidas_por_tempo = sum([1 for result in self.list_resultados() if result["time_out"]])
        print(f"Quantas partidas terminam por time out (1000 rodadas): {qtd_partidas_por_tempo}")

    def mostrar_saida_turnos_jogados(self):
        """
        Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes
        às execuções. Esperamos encontrar nos dados as seguintes informações:
            - Quantos turnos em média demora uma partida;
        """
        turnos_jogados = sum([result["jogou"] for result in self.list_resultados() ])
        print( f"Quantos turnos em média demora uma partida: {turnos_jogados / len(self.list_resultados() ):.2f}")

    def mostra_saida_vitorias_e_vencedor(self):
        """
        Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes
        às execuções. Esperamos encontrar nos dados as seguintes informações:
            - Qual a porcentagem de vitórias por comportamento dos jogadores;
            - Qual o comportamento que mais vence.
        """
        print("Qual a porcentagem de vitórias por comportamento dos jogadores")
        countador_vitorias = self.contabilizar_vitoria()
        estrategia_vencedora = 0
        for estrategia, vitorias in countador_vitorias.items():
            if estrategia_vencedora == 0 or countador_vitorias[estrategia_vencedora] < vitorias:
                estrategia_vencedora = estrategia
            print("  - {}: {}%"
                  .format(DESC_TIPO_ESTRATEGIA_DICT[estrategia], (vitorias * 100) // len(self.list_resultados())))
        print("Qual o comportamento que mais vence: '{}' Venceu: {} vezes"
              .format(DESC_TIPO_ESTRATEGIA_DICT[estrategia_vencedora], countador_vitorias[estrategia_vencedora]))

    def mostrar_resultados(self):
        print('------------------------------------------------------------------------------------------')
        self.mostrar_saida_partida_por_tempo()
        self.mostrar_saida_turnos_jogados()
        self.mostra_saida_vitorias_e_vencedor()
        print('------------------------------------------------------------------------------------------')

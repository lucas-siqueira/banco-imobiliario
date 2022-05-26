from random import randint


class Propriedade:

    def __init__(self, id, dono=None, *args, **kwargs):
        self.id = id
        self.dono = dono
        self.aluguel = randint(30, 120)
        self.valor_imovel = randint(30, 120)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"""
            id:{self.id}
            tipo_de_estrategia:{self.dono}
            aluguel:{self.aluguel}
            valor_imovel:{self.valor_imovel}
        """

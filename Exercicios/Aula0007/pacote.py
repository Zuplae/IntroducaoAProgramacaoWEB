
class Pacote:
    def __init__(self, nome, descricao, destino):
        self.nome = nome
        self.descricao = descricao 
        self.destino = destino

    def __str__(self):
        return f'{self.nome};{self.descricao};{self.destino}'
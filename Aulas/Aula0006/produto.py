class Produto():
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f'{self.nome};{self.descricao};{self.valor}'

prod1 = Produto('Trakinas', 'Boa', 99.0)
print(prod1)

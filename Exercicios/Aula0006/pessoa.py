
class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def __str__(self):
        return f'{self.nome};{self.sobrenome};{self.idade}'
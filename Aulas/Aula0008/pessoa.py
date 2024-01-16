#type hint
class Pessoa:
    def __init__(self, nome:str, sobrenome:str, idade:int) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def __str__(self) -> str:
        return f'{self.nome};{self.sobrenome};{self.idade}'


class Produto:
    def __init__(self, nome:str, descricao:str, valor:float, quantidade:int) -> None:
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade 

    def __str__(self) -> str:
        return f'{self.nome};{self.descricao};{self.valor};{self.quantidade}'
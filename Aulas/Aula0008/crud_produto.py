
from typing import List
from produto import Produto


class CrudProduto:
    nome_arquivo = 'Aulas/Aula0008/produto.txt'

    def create(self, produto:Produto) -> None:
        arquivo = open(self.nome_arquivo, 'a')
        arquivo.write(f'{str(produto)}\n')
        arquivo.close()

    def read_by_id(self, id:int) -> Produto:
        pass

    def read_all(self) -> List[Produto]:
        lista = []
        arquivo = open(self.nome_arquivo, 'r')
        for linha in arquivo:
            linha_formatada = linha.strip() #retira espacos em branco e \n, \r
            dados = linha_formatada.split(';')
            model = Produto(dados[0], dados[1], dados[2], dados[3])
            lista.append(model)
        arquivo.close()
        return lista

    def update(self, produto:Produto) -> None:
        pass

    def delete(self, id:int) -> None:
        pass
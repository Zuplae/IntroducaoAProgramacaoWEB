# type hint
from typing import List
from pessoa import Pessoa


class CrudPessoa:
    nome_arquivo = 'Aulas/Aula0008/pessoa.txt'

    def create(self, pessoa:Pessoa) -> None:
        arquivo = open(self.nome_arquivo, 'a')
        arquivo.write(f'{str(pessoa)}\n')
        arquivo.close()

    def read_by_id(self, id:int) -> Pessoa:
        pass

    def read_all(self) -> List[Pessoa]:
        lista_pessoas = []
        arquivo = open(self.nome_arquivo, 'r')
        for linha in arquivo:
            linha_formatada = linha.strip() #retira espacos em branco e \n, \r
            dados_pessoa = linha_formatada.split(';')
            pessoa = Pessoa(dados_pessoa[0], dados_pessoa[1], dados_pessoa[2])
            lista_pessoas.append(pessoa)
        arquivo.close()
        return lista_pessoas

    def update(self, pessoa:Pessoa) -> None:
        pass

    def delete(self, id:int) -> None:
        pass
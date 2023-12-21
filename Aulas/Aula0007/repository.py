from pessoa import Pessoa

def salvar(pessoa):
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(str(pessoa) + '\n')

def listar():
    lista_pessoas = []
    with open('pessoas.txt', 'r') as arquivo:
        for p in arquivo:
            p = p.strip() # retira \n
            dados = p.split(';') # quebra a linha em um lista onde cada possicao é um dado 
            pessoa = Pessoa(dados[0], dados[1]) 
            lista_pessoas.append(pessoa)
    return lista_pessoas
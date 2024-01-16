#CRUD - Cadastro
#C - Create - Criar um dado, recurso
#R - Read - Ler um ou mais dados
#U - Update - Atualizar um dado
#D - Delete - Excluir um dado
# procedimento = funcao sem return 
# funcao = tem retorno
# metodo = funcao e proced em uma classe
#S.O.L.I.D. - Principio 1- Responsabilidade única

def create(pessoa):
    arquivo = open('Aulas/Aula0008/pessoa.txt', 'a')
    arquivo.write(f'{str(pessoa)}\n')
    arquivo.close()

def read_by_id(id):
    pass

def read_all():
    lista_pessoas = []
    arquivo = open('Aulas/Aula0008/pessoa.txt', 'r')
    for linha in arquivo:
        linha_formatada = linha.strip() #retira espacos em branco e \n, \r
        lista_pessoas.append(linha_formatada)
    arquivo.close()
    return lista_pessoas

def update(pessoa):
    pass

def delete(id):
    pass

pessoas = read_all()
for p in pessoas:
    print(p)
from pessoa import Pessoa

print('Bem-vindo')

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))

pessoa1 = Pessoa(nome, sobrenome, idade)

print(f'Dados cadastrados com sucesso: {pessoa1}')
from pessoa import Pessoa
from repository import salvar, listar


p1 = Pessoa('Joao','Silva')
salvar(p1)
for p in listar():
    print(p)

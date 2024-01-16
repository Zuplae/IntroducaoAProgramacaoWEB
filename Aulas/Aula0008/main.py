from crud_pessoa import CrudPessoa
from pessoa import Pessoa

from produto import Produto
from crud_produto import CrudProduto

# crud_pessoa = CrudPessoa()
# pessoa1 = Pessoa("Maria", "Souza", 22)
# crud_pessoa.create(pessoa1)

# for p in crud_pessoa.read_all():
#     print(p)

crud_produto =  CrudProduto()
produto1 = Produto('Biscoito 1', 'Trakinas grande', 19.9, 1000)
crud_produto.create(produto1)
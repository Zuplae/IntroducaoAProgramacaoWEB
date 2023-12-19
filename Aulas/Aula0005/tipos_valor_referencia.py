#tipo por valor
numero1 = 1
numero2 = numero1

# print(numero1)
# print(numero2)

# numero2 = 5
# print(numero1)
# print(numero2)

#tipo por referencia
lista1 = ['joao', 'maria']
lista2 = lista1

print(lista1)
print(lista2)

lista2[0] = 'Jose'
print('alteracao')
print(lista1)
print(lista2)
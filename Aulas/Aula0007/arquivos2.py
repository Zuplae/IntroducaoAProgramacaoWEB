
file = open('arquivo.txt', 'a')
file.write('Teste\n')
file.write('Teste2\n')
file.close()


with open('arquivo.txt', 'a') as file:
    file.write('Teste\n')
    file.write('Teste2\n')


file = open('arquivo.txt', 'r')
for l in file:
    print(l.strip()) 
file.close()

with open('arquivo.txt', 'r') as file:
    for l in file:
        print(l.strip()) 

#w - modo escrita - mas recria o arquivo
#x - modo escrita - mas se o arquivo ja existir da erro
#a - modo escrita - adiciona conteudo ao final do arquivo
#r - modo leitura

file = open('arquivo.txt', 'a')
file.write('Teste\n')
file.write('Teste2\n')
file.close()

file = open('arquivo.txt', 'r')
for l in file:
    print(l.strip()) # strip retira espacos em branco e caracteres especiais \n\r
file.close()
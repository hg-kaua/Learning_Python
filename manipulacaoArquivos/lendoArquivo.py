# abrindo o arquivo para leitura
arq1 = open("manipulaçaoArquivos/arquivo1.txt", "r")

# lendo o arquivo e imprimindo na tela
print(arq1.read(24))

# informa o numero de caracteres do arquivo
print(arq1.tell())

print(arq1.read())

# volta o cursor para o inicio do arquivo
print(arq1.seek(0,0))

print(arq1.read())

# criando um arquivo e editando ele


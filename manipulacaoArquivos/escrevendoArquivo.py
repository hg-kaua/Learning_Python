
arq2 = open("manipulacaoArquivos/arquivo2.txt", "w") # repare que para editar utilizamos o W de write 
# print(arq2.read()) ## gera uma mensagem de erro pq o arquivo nao foi aberto para leitura
arq2.write("fala comigo!!!!! major")
arq2.close()

arq2 = open("manipulacaoArquivos/arquivo2.txt", "r")
print(arq2.read())

arq2 = open("manipulacaoArquivos/arquivo2.txt", "a") # a de append

arq2.write(" all good to you mai friend")


arq2 = open("manipulacaoArquivos/arquivo2.txt", "r")
print(arq2.read())

arq2.seek(0,0)

data = arq2.read()

rows = data.split(" ")

print(rows)
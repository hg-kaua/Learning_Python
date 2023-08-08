
with open("manipulacaoArquivos/arquivo4.txt", "w") as arquivo:
    arquivo.write("Apenas fazendo um teste aqui com o WITH")

with open("manipulacaoArquivos/arquivo4.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    print(len(conteudo))
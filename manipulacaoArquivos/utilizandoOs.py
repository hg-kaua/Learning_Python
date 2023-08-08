import os 

texto = "Estamos aqui para fazer mais um teste \n"
texto = texto + "Nesse teste vamos utilizar a biblioteca os \n"
texto += "Uma famosa biblioteca de python \n"

arquivo = open(os.path.join("manipulacaoArquivos/arquivo3.txt"), "w")

arquivo.write(texto)

for palavra in texto.split():
    arquivo.write(palavra + " ")

arquivo = open("manipulacaoArquivos/arquivo3.txt", "r")

conteudo = arquivo.read()
print(conteudo)
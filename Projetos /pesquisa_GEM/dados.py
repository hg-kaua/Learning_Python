import matplotlib.pyplot as plt


sexo = ["Masculino", "Feminino"]
dados_sexo = [454, 546]
grupos_faixa_etaria = ["18 - 24", "25 - 34", "35 - 44", "45 - 54", "55 - 64"]
dados_faixa_etaria = [16, 28.5, 24.4, 16.1, 15]
status_escolaridade = ['Fundamental incompleto', 'Fundamental completo', "Superior Completo", 'Médio completo']
dados_escolaridade = [131,155,460,255]

# Primeiro grafico: pizza
fig, axes = plt.subplots(2, 2, figsize= (12,6))
axes[0,0].pie(
    x= dados_sexo,
    labels= sexo,
    colors= ['#32CD32', '#215E21'],
    startangle= 90,
    shadow= False,
    explode=(0,0.01),
    autopct= '%1.1f%%',) # deixa os valores dentro do grafico no formato 10.0%
    
axes[0,0].set_title("Empreendedores nascentes - Sexo")

# Segundo gráfico: bar
axes[0,1].bar(
    grupos_faixa_etaria,
    dados_faixa_etaria,
    label= grupos_faixa_etaria,
    color = ["#000066", "#000099", "#3333FF", "#3366FF", "#33CCFF"]
    )

axes[0,1].set_title("Empreendedores nascentes - Faixa Etária")

fig[0, 1].legend(grupos_faixa_etaria, loc = 'outside upper right' )


# Terceiro grafico: pizza
axes[1,0].pie(
    x= dados_escolaridade,
    labels= status_escolaridade,
    colors= ['#00FA9A', '#006400', "m", "r"],
    startangle= 90,
    shadow= False,
    explode=(0.01, 0.01, 0.01, 0.01),
    autopct= '%1.1f%%')

axes[1,0].set_title("Empreendedores nascentes - Escolaridade")


    
plt.show()
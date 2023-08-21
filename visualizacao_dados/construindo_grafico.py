import matplotlib.pyplot as plt
import random

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y = [0, 1, 3, 6, 10, 16, 21, 29, 20, 24, 30, 38, 45, 25, 50]

plt.plot(x,y, label = "Linha")
plt.xlabel("Tempo(d)")
plt.ylabel("Lucro($)")
plt.title("Gráfico Lucro X Tempo")



# Construindo grafico de barras
x2 = []
y2 = []
for i in range(1,10):
    x2.append(random.randint(1,15))
    y2.append(random.randint(1,45))
plt.bar(x2,y2, label= "Prejuizo", color= "red")
    
plt.bar(x,y, label= "Lucro", color="green")
plt.legend()
plt.show()
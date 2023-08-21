import matplotlib.pyplot as plt
import random

x = [1, 2, 4, 6, 8, 10, 12, 14]
y = [0, 1, 3, 6, 10, 16, 21, 29]

plt.plot(x,y, label = "Linha")
plt.xlabel("Tempo(d)")
plt.ylabel("Lucro($)")
plt.title("Gráfico Lucro X Tempo")



# Construindo grafico de barras
# x2 = []
# y2 = []
# for i in range(1,10):
#     x2.append(random.randint(1,30))
#     y2.append(random.randint(1,30))
# plt.bar(x2,y2, label= "Barras")
    
plt.bar(x,y, label= "Barras")
plt.legend()
plt.show()
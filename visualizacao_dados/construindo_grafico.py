import matplotlib.pyplot as plt

x = [1, 2, 4, 6, 8, 10, 12, 14]
y = [0, 1, 3, 6, 10, 16, 21, 29]

plt.plot(x,y)
plt.xlabel("Tempo(d)")
plt.ylabel("Lucro($)")
plt.title("Gráfico Lucro X Tempo")

plt.show()


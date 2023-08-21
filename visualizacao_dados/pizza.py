import matplotlib.pyplot as plt

fatias = [7, 4, 8, 2, 3]
atividades = ["Dormir", "Estudar", "Trabalhar", "Malhar", "Lazer"]
cores = ["r", "b", "c", "m", "y"]

plt.pie(fatias, labels=atividades, colors= cores, startangle= 90, explode=(0,0.1,0,0,0))
plt.show()
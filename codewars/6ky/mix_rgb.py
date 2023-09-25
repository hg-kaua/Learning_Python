from math import ceil
class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
        pass
    
    def mix(self, other):

        # formula = r1 * v1 + r2 * v2 / v1 + v2
        new_color = []
        for i in range(3):
            new_color.append(ceil((self.color[i] * self.volume + other.color[i] * other.volume) / (self.volume + other.volume)))

        new_volume = self.volume + other.volume
        color_tuple = tuple(new_color)
        return Potion(color_tuple, new_volume)
        

potions = [
    Potion((153, 210, 199), 32),
    Potion((135,  34,   0), 17),
    Potion((18,   19,  20), 25),
    Potion((174, 211,  13),  4),
    Potion((255,  23, 148), 19),
    Potion((51,  102,  51),  6)
]
a = potions[0].mix(potions[1])
b = potions[0].mix(potions[2]).mix(potions[4])
c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
d = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[4]).mix(potions[5])
e = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[3]).mix(potions[4]).mix(potions[5])


print(a.color) 
print(a.volume)
print(b.color)
print(c.color)
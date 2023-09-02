class Quark(object):
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1/3
    
    def interact(self, other_quark):
        self.color, other_quark.color = other_quark.color, self.color

q1 = Quark("Red", "Up")
q2 = Quark("Blue", "Strange")

print(q1.color)
print(q1.flavor)
print(q1.baryon_number)

print(q2.color)
print(q2.flavor)
print(q2.baryon_number)

q1.interact(q2)

print(q1.color)
print(q2.color)

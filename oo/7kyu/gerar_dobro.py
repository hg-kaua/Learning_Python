class Class:
    numero = 0
    @staticmethod
    def get_number():
        if Class.numero == 0:
            Class.numero = 1
        else:
            Class.numero *= 2
            
        return Class.numero

c = Class()

print(c.get_number())
print(c.get_number())
print(c.get_number())
print(c.get_number())
print(c.get_number())

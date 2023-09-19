class Person():
    def __init__(self, my_name):
        self.my_name = my_name

    def greet(self, your_name):
        self.your_name = your_name
        return "Hello %s, my name is %s" % (your_name, self.my_name)
    
jack = Person("Jack")
jill = Person("Jill")

print(jack.greet('jill'))
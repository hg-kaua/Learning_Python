class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def age(self):
        return self.age
    
hugo = Person("Hugo", "Medeiros", 20)

print(hugo.full_name())
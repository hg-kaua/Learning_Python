class Student:

    def __init__(self, first_name, last_name, grades = None):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades or []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades)

hugo_grades = [10,10,10,9]
joao_grades = [5,9,2,4]

hugo = Student("Hugo", "Medeiros")
hugo.add_grade(10)

joao = Student("Joao", "Vitor", joao_grades)
joao.add_grade(4)

print(hugo.grades)
print(joao.grades)
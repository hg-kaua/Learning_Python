class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

     
def most_money(students):
    total = []
    for student in students:
        total.append((student.fives*5) + (student.tens*10) + (student.twenties * 20))
    
    if min(total) == max(total) and len(students) > 1:
        return 'all'
    else:
        return students[total.index(max(total))].name
    
phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)
        
print(most_money([phil, cam, geoff]))
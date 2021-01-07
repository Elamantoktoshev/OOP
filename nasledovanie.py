class ShoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(создан ShoolMember: {0})'.format(self.name))

    def tell(self):
        print('name:"{0}" age:"{1}"'.format(self.name, self.age), end=" ")


class teacher(ShoolMember):
    def __init__(self, name, age, salary):
        ShoolMember.__init__(self, name, age)
        self.salary = salary
        print('(создан teacher: {0})'.format(self.name))

    def tell(self):
        ShoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(ShoolMember):
    def __init__(self, name, age, marks):
        ShoolMember.__init__(self, name, age)
        self.marks = marks
        print('(создан Student {0})'.format(self.name))

    def tell(self):
        ShoolMember.tell(self)
        print('оценки: "{0:d}"'.format(self.marks))


t = teacher('Elaman', 25, 50000)
s = Student('Zhazgul', 18, 45000)
print()
members = [t, s]
for member in members:
    member.tell()

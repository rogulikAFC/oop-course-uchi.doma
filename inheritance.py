class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'Человек {self.name}'

    def get_age(self):
        return f'Возраст {self.age}'


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def get_name(self):
        return f'{super().get_name()} ({self.course} класс)'


student = Student(
    input('name: '),
    input('age: '),
    input('course: ')
)

print(student.get_name())

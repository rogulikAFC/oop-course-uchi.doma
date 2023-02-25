class Student:
    def __init__(self, name):
        self.name = name

    def get_action(self):
        return f'Ученик {self.name} учится'

    def __repr__(self):
        return f'Student({self.name})'


class Teacher:
    def __init__(self, name):
        self.name = name

    def get_action(self):
        return f'Учитель {self.name} учит'

    def __repr__(self):
        return f'Teacher({self.name})'


n = input('n: ')
people_list = list()

for i in range(int(n)):
    person_inp = input('person: ').split(': ')
    person_obj = None

    if person_inp[0] == 'Teacher':
        person_obj = Teacher(person_inp[1])

    elif person_inp[0] == 'Student':
        person_obj = Student(person_inp[1])

    people_list.append(person_obj)

print(people_list)

for person in people_list:
    print(person.get_action())

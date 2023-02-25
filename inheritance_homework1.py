class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'Человек: {self.name}'

    def get_age(self):
        return f'Возраст: {self.age}'


class Worker(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def get_name(self):
        return f'Рабочий: {self.name}, должность: {self.job}'


worker = Worker(
    input('name: '),
    input('age: '),
    input('job: ')
)

print(worker.get_name())
print(worker.get_age())

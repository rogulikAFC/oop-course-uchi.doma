class Person:
    def __init__(self, name, age, passport):
        self.__name = name
        self.__age = age
        self.__passport = passport

    def change_age(self):
        self.__age += 1

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, value):
        print(len(str(value)))

        if len(str(value)) != 10:
            print('Неверный номер паспорта')

        else:
            self.__passport = value

    def get_info(self):
        passport_blured = '******' + str(self.__passport)[6:10]
        return f'{self.__name}, возраст: {self.__age}, номер паспорта: {passport_blured}'


name = input('name: ')
age = int(input('age: '))
passport = int(input('passport: '))
method = input('method: ')

person = Person(name, age, passport)

try:
    int(method)
    person.passport = int(method)

except:
    print('exception')
    if method == 'change_age':
        person.change_age()


print(person.get_info())

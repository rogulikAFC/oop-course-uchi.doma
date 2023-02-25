class Student:
    def __init__(self, name, course):
        self.__name = name
        self.__course = course
        self.__status = 'student'

    def next_course(self):
        if self.__course == 11:
            self.__status = 'graduate'
            self.__course = None
            return

        self.__course += 1

    def deduction(self):
        self.__course == None
        self.__status == 'expelled'

    def get_info(self):
        return f'Student: {self.__name}, {self.__course}, status: {self.__status}'


class Point:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value <= 0:
            print('must be greater then 0')
            return

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value <= 0:
            print('must be greater then 0')
            return

        self.__y = value

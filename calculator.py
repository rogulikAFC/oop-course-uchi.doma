class Calculator:
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def calculate(self):
        global result
        result = None

        try:
            if self.operation == '+':
                result = self.num1 + self.num2

            elif self.operation == '-':
                result = self.num1 - self.num2

            elif self.operation == '*':
                result = self.num1 * self.num2

            elif self.operation == '/':
                result = self.num1 / self.num2

            else:
                raise OperationError

            return result

        except TypeError:
            print('Неверный ввод. Ошибка типа данных')

        except OperationError:
            print('Нет такой операции')


class OperationError(Exception):
    pass

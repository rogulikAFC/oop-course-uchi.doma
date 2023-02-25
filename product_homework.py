class Product:
    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount

    def sale(self):
        if self.__amount <= 0:
            print('Нет в наличии')
            return

        self.__amount -= 1

    def refund(self):
        self.__amount += 1

    def get_info(self):
        return f'Товар: {self.__name}, цена: {self.__price}, количество: {self.__amount}'


name = input('name: ')
price = int(input('price: '))
amount = int(input('amount: '))
method = input('do ')

product = Product(name, price, amount)

if method == 'sale':
    product.sale()

elif method == 'refund':
    product.refund()

print(product.get_info())

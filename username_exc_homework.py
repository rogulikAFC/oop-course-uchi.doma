class WrongCharacterError(Exception):
    pass


class FirstCharacterError(Exception):
    pass


username = input('username: ')

try:
    for letter in username:
        if not (letter.isalpha() or letter.isdigit()):
            print('lol')
            raise WrongCharacterError

    if username[0].isdigit():
        raise FirstCharacterError

except WrongCharacterError:
    print('username может содержать только буквы и цифры')

except FirstCharacterError:
    print('username не может начинаться с цифры')

else:
    print('OK')

import string
import random


def password(chars, number=1, letter=1, symbol=1):
    if not number and not letter and not symbol:
        return 'должен быть хотя бы один из: цифр, букв, знаков'
    if chars < 6:
        return 'не меньше 6 символов'
    number = string.digits if number else ''
    letter = string.ascii_letters if letter else ''
    symbol = string.punctuation if symbol else ''
    s = number + letter + symbol
    return ''.join(random.choices(s, k=chars))


if __name__ == '__main__':
    print(password(12, symbol=0))

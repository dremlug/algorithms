# ID 118490491
import string


def decrypt(encrypted: str) -> str:
    """Дешифрование управляющих сообщений Марсохода.
    Входные данные: encrypted - шифровонное сообщение
    Выходные данные: decrypted - дешифрованное сообщение
    """
    multiplier = decrypted = ''
    _stack = []
    for char in encrypted:
        # Получение числа-множителя из строки
        if char in string.digits:
            multiplier += char
        # Добавляем подстроку и множитель в стек
        elif char == '[':
            _stack.append((int(multiplier), decrypted))
            decrypted = ''
            multiplier = ''
        # Вынимаем подстроку и множитель из стека
        elif char == ']':
            _multiplier, _decrypted = _stack.pop()
            decrypted = _decrypted + _multiplier * decrypted
        # Добавлем символ с коэффициентом в подстроку
        else:
            decrypted += char

    return decrypted


if __name__ == '__main__':
    print(decrypt(input()))

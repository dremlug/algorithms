# ID 118492204
import string


def decrypt(encrypted: str) -> str:
    """Дешифрование управляющих сообщений Марсохода.
    Входные данные: encrypted - шифровонное сообщение
    Выходные данные: decrypted - дешифрованное сообщение
    """
    multiplier = decrypted = ''
    stack = []
    for char in encrypted:
        match char:
            # Получение числа-множителя из строки
            case _ if char in string.digits:
                multiplier += char
            # Добавляем подстроку и множитель в стек
            case '[':
                stack.append((int(multiplier), decrypted))
                decrypted = multiplier = ''
            # Вынимаем подстроку и множитель из стека
            case ']':
                _multiplier, _decrypted = stack.pop()
                decrypted = _decrypted + _multiplier * decrypted
            # Добавлем символ с коэффициентом в подстроку
            case _:
                decrypted += char
    return decrypted


if __name__ == '__main__':
    print(decrypt(input()))

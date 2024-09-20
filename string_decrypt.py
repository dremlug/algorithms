# ID 118423710
import string


def decrypt(encrypted: str) -> str:
    """Дешифрование управляющих сообщений Марсохода.
    Входные данные: encrypted - шифровонное сообщение
    Выходные данные: decrypted - дешифрованное сообщение
    """
    index = 0
    multiplier = '1'
    is_previous_digit = False
    decrypted = [[1, '']]
    for char in encrypted:
        # Получение числа-множителя из строки
        if char in string.digits:
            if not is_previous_digit:
                multiplier = char
            else:
                multiplier += char
            is_previous_digit = True
        # Добавляем подстраку и множетель в стек
        elif char == '[':
            decrypted.append([multiplier, ''])
            is_previous_digit = False
            multiplier = '1'
            index += 1
        # Вынимаем подстроку и множетль из стека
        elif char == ']':
            is_previous_digit = False
            index -= 1
            _multiplier, _string = decrypted.pop()
            decrypted[index][1] += int(_multiplier) * _string
        # Добавлем символ с коэффициентом в подстроку
        else:
            is_previous_digit = False
            decrypted[index][1] += int(multiplier) * char
    return decrypted[0][1]


if __name__ == '__main__':
    print(decrypt(input()))

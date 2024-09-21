# ID 118483114
import string


def decrypt(encrypted: str) -> str:
    """Дешифрование управляющих сообщений Марсохода.
    Входные данные: encrypted - шифровонное сообщение
    Выходные данные: current_decryption - дешифрованное сообщение
    """
    multiplier = ''
    decrypted = []
    current_decryption = ''
    for char in encrypted:
        # Получение числа-множителя из строки
        if char in string.digits:
                multiplier += char
                continue
        # Добавляем подстраку и множетель в стек
        elif char == '[':
            decrypted.append((multiplier, current_decryption))
            current_decryption = ''
        # Вынимаем подстроку и множетель из стека
        elif char == ']':
            _multiplier, _string = decrypted.pop()
            current_decryption = _string + int(_multiplier) * current_decryption
        # Добавлем символ с коэффициентом в подстроку
        else:
            if multiplier != '':
                current_decryption += int(multiplier) * char
            else:
                current_decryption += char
        multiplier = ''
    return current_decryption


if __name__ == '__main__':
    print(decrypt(input()))

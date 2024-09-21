# ID 118483749
import string


def decrypt(encrypted: str) -> str:
    """Дешифрование управляющих сообщений Марсохода.
    Входные данные: encrypted - шифровонное сообщение
    Выходные данные: current_decryption - дешифрованное сообщение
    """
    multiplier = ''
    decrypted = []
    current_decrypted = ''
    for char in encrypted:
        # Получение числа-множителя из строки
        if char in string.digits:
                multiplier += char
                continue
        # Добавляем подстроку и множитель в стек
        elif char == '[':
            decrypted.append((multiplier, current_decrypted))
            current_decrypted = ''
        # Вынимаем подстроку и множитель из стека
        elif char == ']':
            _multiplier, _string = decrypted.pop()
            current_decrypted = _string + int(_multiplier) * current_decrypted
        # Добавлем символ с коэффициентом в подстроку
        else:
            if multiplier != '':
                current_decrypted += int(multiplier) * char
            else:
                current_decrypted += char
        multiplier = ''
    return current_decrypted


if __name__ == '__main__':
    print(decrypt(input()))
